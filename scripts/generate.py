#!/usr/bin/env python3
"""Generate public and internal Python SDK packages for the monorepo."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from urllib.request import Request, urlopen

import yaml

ROOT_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = ROOT_DIR / "templates"
DEFAULT_PUBLIC_SPEC_URL = (
    "https://raw.githubusercontent.com/BrigadaSOS/Nadeshiko/main-v2/"
    "backend/docs/generated/openapi.yaml"
)
DEFAULT_INTERNAL_SPEC_URL = (
    "https://raw.githubusercontent.com/BrigadaSOS/Nadeshiko/main-v2/"
    "backend/docs/generated/openapi-internal.yaml"
)
DEFAULT_PUBLIC_LOCAL_SPEC = (
    ROOT_DIR / ".." / "Nadeshiko" / "backend" / "docs" / "generated" / "openapi.yaml"
)
DEFAULT_INTERNAL_LOCAL_SPEC = (
    ROOT_DIR / ".." / "Nadeshiko" / "backend" / "docs" / "generated" / "openapi-internal.yaml"
)


@dataclass(frozen=True)
class PackageTarget:
    name: str
    source_dir: Path
    config_path: Path


PUBLIC_TARGET = PackageTarget(
    name="public",
    source_dir=ROOT_DIR / "sdk" / "src" / "nadeshiko",
    config_path=ROOT_DIR / "sdk" / "openapi-client-config.yaml",
)

INTERNAL_TARGET = PackageTarget(
    name="internal",
    source_dir=ROOT_DIR / "sdk-internal" / "src" / "nadeshiko_internal",
    config_path=ROOT_DIR / "sdk-internal" / "openapi-client-config.yaml",
)


def env_path(name: str) -> Path | None:
    value = os.environ.get(name, "").strip()
    if not value:
        return None
    return Path(value)


def resolve_input_path(path: Path) -> Path:
    if path.is_absolute():
        return path
    return (ROOT_DIR / path).resolve()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--sdk-type",
        choices=("all", "public", "internal"),
        default="all",
        help="SDK target to generate.",
    )
    parser.add_argument(
        "--public-spec-path",
        type=Path,
        default=env_path("NADESHIKO_PUBLIC_SPEC_PATH"),
        help="Optional local path to the public OpenAPI spec.",
    )
    parser.add_argument(
        "--internal-spec-path",
        type=Path,
        default=env_path("NADESHIKO_INTERNAL_SPEC_PATH"),
        help="Optional local path to the internal OpenAPI spec.",
    )
    parser.add_argument(
        "--public-spec-url",
        default=os.environ.get("NADESHIKO_PUBLIC_SPEC_URL", DEFAULT_PUBLIC_SPEC_URL),
        help="URL source for the public spec (default: GitHub main-v2).",
    )
    parser.add_argument(
        "--internal-spec-url",
        default=os.environ.get("NADESHIKO_INTERNAL_SPEC_URL", DEFAULT_INTERNAL_SPEC_URL),
        help="URL source for the internal spec (default: GitHub main-v2).",
    )
    parser.add_argument(
        "--keep-build",
        action="store_true",
        help="Keep temporary generated artifacts for debugging.",
    )
    return parser.parse_args()


def fetch_spec_file(url: str) -> Path:
    request = Request(url, headers={"User-Agent": "nadeshiko-sdk-python-generator"})
    with urlopen(request, timeout=30) as response:  # noqa: S310
        content = response.read()

    with tempfile.NamedTemporaryFile(prefix="nadeshiko-spec-", suffix=".yaml", delete=False) as tmp:
        tmp.write(content)
        return Path(tmp.name)


def resolve_spec_path(
    *,
    spec_name: str,
    explicit_path: Path | None,
    spec_url: str,
    fallback_path: Path,
) -> tuple[Path, bool]:
    if explicit_path is not None:
        resolved_path = resolve_input_path(explicit_path)
        if not resolved_path.exists():
            raise FileNotFoundError(f"{spec_name} OpenAPI spec not found: {resolved_path}")
        print(f"Using local {spec_name} spec: {resolved_path}")
        return resolved_path, False

    if spec_url:
        try:
            fetched_path = fetch_spec_file(spec_url)
            print(f"Fetched {spec_name} spec from: {spec_url}")
            return fetched_path, True
        except Exception as error:  # noqa: BLE001
            resolved_fallback = resolve_input_path(fallback_path)
            if resolved_fallback.exists():
                print(
                    f"Failed to fetch {spec_name} spec from {spec_url} ({error}). "
                    f"Falling back to local spec: {resolved_fallback}"
                )
                return resolved_fallback, False
            raise RuntimeError(
                f"Failed to fetch {spec_name} spec from {spec_url} "
                f"and fallback path is missing: {resolved_fallback}"
            ) from error

    resolved_fallback = resolve_input_path(fallback_path)
    if not resolved_fallback.exists():
        raise FileNotFoundError(
            f"No {spec_name} spec URL provided and fallback path is missing: {resolved_fallback}"
        )
    print(f"Using fallback local {spec_name} spec: {resolved_fallback}")
    return resolved_fallback, False


def preserve_version(version_path: Path) -> str:
    if version_path.exists():
        return version_path.read_text(encoding="utf-8")
    return '__version__ = "0.1.0"\n'


def normalize_openapi_for_codegen(spec_path: Path) -> tuple[Path, bool]:
    with spec_path.open("r", encoding="utf-8") as file:
        spec = yaml.safe_load(file)

    changed = False

    def patch_response_dict(response_obj: object) -> None:
        nonlocal changed
        if not isinstance(response_obj, dict):
            return
        if "$ref" in response_obj:
            return
        if "description" not in response_obj:
            response_obj["description"] = ""
            changed = True

    for path_item in spec.get("paths", {}).values():
        if not isinstance(path_item, dict):
            continue
        for method, operation in path_item.items():
            if method in {"parameters", "$ref"}:
                continue
            if not isinstance(operation, dict):
                continue
            responses = operation.get("responses", {})
            if not isinstance(responses, dict):
                continue
            for response in responses.values():
                patch_response_dict(response)

    component_responses = spec.get("components", {}).get("responses", {})
    if isinstance(component_responses, dict):
        for response in component_responses.values():
            patch_response_dict(response)

    if not changed:
        return spec_path, False

    with tempfile.NamedTemporaryFile(
        prefix="nadeshiko-spec-normalized-",
        suffix=".yaml",
        delete=False,
    ) as tmp:
        tmp.write(yaml.safe_dump(spec, sort_keys=False).encode("utf-8"))
        return Path(tmp.name), True


def run_codegen(target: PackageTarget, spec_path: Path, keep_build: bool) -> None:
    version_path = target.source_dir / "_version.py"
    version_content = preserve_version(version_path)

    shutil.rmtree(target.source_dir, ignore_errors=True)
    target.source_dir.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        sys.executable,
        "-m",
        "openapi_python_client",
        "generate",
        "--path",
        str(spec_path),
        "--output-path",
        str(target.source_dir),
        "--config",
        str(target.config_path),
        "--custom-template-path",
        str(TEMPLATES_DIR),
        "--meta",
        "none",
        "--overwrite",
    ]

    print(f"Generating {target.name} SDK from: {spec_path}")
    env = os.environ.copy()
    executable_dir = str(Path(sys.executable).resolve().parent)
    env["PATH"] = (
        executable_dir if not env.get("PATH") else f"{executable_dir}{os.pathsep}{env['PATH']}"
    )
    subprocess.run(cmd, check=True, cwd=ROOT_DIR, env=env)  # noqa: S603

    version_path.write_text(version_content, encoding="utf-8")

    if not keep_build:
        shutil.rmtree(target.source_dir / ".ruff_cache", ignore_errors=True)


def main() -> int:
    args = parse_args()

    targets: list[tuple[PackageTarget, str, Path | None, str, Path]] = []
    if args.sdk_type in {"all", "public"}:
        targets.append(
            (
                PUBLIC_TARGET,
                "public",
                args.public_spec_path,
                args.public_spec_url.strip(),
                DEFAULT_PUBLIC_LOCAL_SPEC,
            )
        )
    if args.sdk_type in {"all", "internal"}:
        targets.append(
            (
                INTERNAL_TARGET,
                "internal",
                args.internal_spec_path,
                args.internal_spec_url.strip(),
                DEFAULT_INTERNAL_LOCAL_SPEC,
            )
        )

    temp_files: list[Path] = []

    try:
        for target, spec_name, explicit_path, spec_url, fallback_path in targets:
            resolved_spec, is_temp = resolve_spec_path(
                spec_name=spec_name,
                explicit_path=explicit_path,
                spec_url=spec_url,
                fallback_path=fallback_path,
            )
            if is_temp:
                temp_files.append(resolved_spec)
            normalized_spec, normalized_is_temp = normalize_openapi_for_codegen(resolved_spec)
            if normalized_is_temp:
                print(
                    f"Normalized {spec_name} OpenAPI spec for code generation: {normalized_spec}"
                )
                temp_files.append(normalized_spec)
            run_codegen(target, normalized_spec, keep_build=args.keep_build)
    finally:
        for file_path in temp_files:
            file_path.unlink(missing_ok=True)

    print("Generation complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
