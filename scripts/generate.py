#!/usr/bin/env python3
"""Generate public and internal Python SDK packages from a single OpenAPI spec."""

from __future__ import annotations

import argparse
import copy
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path
from urllib.request import Request, urlopen

import yaml

from postprocess_wrappers import collect_operations, write_wrapper_files

ROOT_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = ROOT_DIR / "templates"
DEFAULT_SPEC_URL = (
    "https://raw.githubusercontent.com/BrigadaSOS/Nadeshiko/main/"
    "backend/docs/generated/openapi.yaml"
)
DEFAULT_LOCAL_SPEC = (
    ROOT_DIR / ".." / "Nadeshiko" / "backend" / "docs" / "generated" / "openapi.yaml"
)

HTTP_METHODS = {"get", "put", "post", "delete", "options", "head", "patch", "trace"}


@dataclass(frozen=True)
class PackageTarget:
    name: str
    source_dir: Path
    config_path: Path


PUBLIC_TARGET = PackageTarget(
    name="public",
    source_dir=ROOT_DIR / "generated" / "public" / "nadeshiko",
    config_path=ROOT_DIR / "config" / "public.yaml",
)

INTERNAL_TARGET = PackageTarget(
    name="internal",
    source_dir=ROOT_DIR / "generated" / "internal" / "nadeshiko_internal",
    config_path=ROOT_DIR / "config" / "internal.yaml",
)


def _is_url(value: str) -> bool:
    return value.startswith("https://") or value.startswith("http://")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--sdk-type",
        choices=("all", "public", "internal"),
        default="all",
        help="SDK target to generate.",
    )
    parser.add_argument(
        "--spec",
        default=os.environ.get("OPENAPI_SPEC_PATH", "").strip() or None,
        help="OpenAPI spec source: URL or local file path. "
        "Falls back to GitHub main, then local sibling repo.",
    )
    parser.add_argument(
        "--keep-build",
        action="store_true",
        help="Keep temporary generated artifacts for debugging.",
    )
    parser.add_argument(
        "--verify",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Verify public/internal boundaries after generation (default: enabled).",
    )
    return parser.parse_args()


def _fetch_spec(url: str) -> Path:
    request = Request(url, headers={"User-Agent": "nadeshiko-sdk-python-generator"})
    with urlopen(request, timeout=30) as response:  # noqa: S310
        content = response.read()

    with tempfile.NamedTemporaryFile(
        prefix="nadeshiko-spec-", suffix=".yaml", delete=False
    ) as tmp:
        tmp.write(content)
        return Path(tmp.name)


def _resolve_local_path(value: str) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path
    return (ROOT_DIR / path).resolve()


def resolve_spec(spec: str | None) -> tuple[Path, bool]:
    """Resolve spec to a local file path.

    Accepts a URL, a local file path, or None (auto-detect).
    Returns (path, is_temp) where is_temp means the file should be cleaned up.
    """
    # Explicit URL
    if spec and _is_url(spec):
        fetched = _fetch_spec(spec)
        print(f"Fetched spec from: {spec}")
        return fetched, True

    # Explicit local path
    if spec:
        resolved = _resolve_local_path(spec)
        if not resolved.exists():
            raise FileNotFoundError(f"OpenAPI spec not found: {resolved}")
        print(f"Using local spec: {resolved}")
        return resolved, False

    # No explicit spec: try default URL, fall back to local sibling repo
    try:
        fetched = _fetch_spec(DEFAULT_SPEC_URL)
        print(f"Fetched spec from: {DEFAULT_SPEC_URL}")
        return fetched, True
    except Exception as error:  # noqa: BLE001
        fallback = (ROOT_DIR / DEFAULT_LOCAL_SPEC).resolve()
        if fallback.exists():
            print(
                f"Failed to fetch spec ({error}). "
                f"Falling back to local spec: {fallback}"
            )
            return fallback, False
        raise RuntimeError(
            f"Failed to fetch spec from {DEFAULT_SPEC_URL} "
            f"and fallback path is missing: {fallback}"
        ) from error


def resolve_version(version_path: Path, spec_path: Path, target_name: str) -> str:
    """Preserve existing _version.py, or derive from spec info.version on first gen.

    Matches the CI logic in validate_payload.py: internal builds append .dev{utc_ts}
    so versions sort chronologically and PEP 440 .devN is satisfied.
    """
    if version_path.exists():
        return version_path.read_text(encoding="utf-8")

    with spec_path.open("r", encoding="utf-8") as file:
        spec = yaml.safe_load(file)
    base_version = str(spec.get("info", {}).get("version") or "").strip() or "0.1.0"

    if target_name == "internal":
        version = f"{base_version}.dev{int(time.time())}"
    else:
        version = base_version
    return f'__version__ = "{version}"\n'


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


def filter_public_spec(spec_path: Path) -> Path:
    """Create a filtered copy of the spec with x-internal operations removed."""
    with spec_path.open("r", encoding="utf-8") as file:
        spec = yaml.safe_load(file)

    filtered_spec = copy.deepcopy(spec)
    paths = filtered_spec.get("paths", {})
    paths_to_remove: list[str] = []

    for path_key, path_item in paths.items():
        if not isinstance(path_item, dict):
            continue

        methods_to_remove: list[str] = []
        for method in HTTP_METHODS:
            operation = path_item.get(method)
            if not isinstance(operation, dict):
                continue
            if operation.get("x-internal"):
                methods_to_remove.append(method)

        for method in methods_to_remove:
            del path_item[method]

        remaining_methods = [m for m in HTTP_METHODS if m in path_item]
        if not remaining_methods:
            paths_to_remove.append(path_key)

    for path_key in paths_to_remove:
        del paths[path_key]

    with tempfile.NamedTemporaryFile(
        prefix="nadeshiko-spec-public-",
        suffix=".yaml",
        delete=False,
    ) as tmp:
        tmp.write(yaml.safe_dump(filtered_spec, sort_keys=False).encode("utf-8"))
        print(f"Created filtered public spec: {tmp.name}")
        return Path(tmp.name)


def categorize_operations(spec: dict) -> tuple[set[str], set[str]]:
    """Return (public_ops, internal_only_ops) from a parsed spec."""
    public_ops: set[str] = set()
    internal_only_ops: set[str] = set()
    for path_item in spec.get("paths", {}).values():
        for method, operation in path_item.items():
            if method in {"parameters", "$ref"}:
                continue
            if not isinstance(operation, dict):
                continue
            op_id = operation.get("operationId")
            if not op_id:
                continue
            if operation.get("x-internal"):
                internal_only_ops.add(op_id)
            else:
                public_ops.add(op_id)
    return public_ops, internal_only_ops


def _operation_id_to_snake(operation_id: str) -> str:
    step_one = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", operation_id)
    step_two = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", step_one)
    return step_two.lower()


def _api_modules(api_dir: Path) -> set[str]:
    modules: set[str] = set()
    for file_path in api_dir.rglob("*.py"):
        if file_path.name == "__init__.py":
            continue
        modules.add(file_path.stem)
    return modules


def _any_candidate_present(operation_id: str, modules: set[str]) -> bool:
    base = _operation_id_to_snake(operation_id)
    return bool({base, f"{base}_"} & modules)


def verify_boundaries(spec: dict) -> int:
    """Check that public SDK outputs do not leak internal-only operations.

    Returns 0 on success, 1 on failure.
    """
    public_ops, internal_only_ops = categorize_operations(spec)
    all_ops = public_ops | internal_only_ops

    failures: list[str] = []

    public_api_dir = PUBLIC_TARGET.source_dir / "api"
    internal_api_dir = INTERNAL_TARGET.source_dir / "api"

    if not public_api_dir.exists():
        failures.append(f"Missing public API directory: {public_api_dir}")
    if not internal_api_dir.exists():
        failures.append(f"Missing internal API directory: {internal_api_dir}")

    if failures:
        for failure in failures:
            print(f"Boundary check failed: {failure}")
        return 1

    public_modules = _api_modules(public_api_dir)
    internal_modules = _api_modules(internal_api_dir)

    leaked_ops = [
        op for op in sorted(internal_only_ops) if _any_candidate_present(op, public_modules)
    ]
    if leaked_ops:
        failures.append(
            f"Public SDK contains internal-only operations: {', '.join(leaked_ops)}"
        )

    missing_public_ops = [
        op for op in sorted(public_ops) if not _any_candidate_present(op, public_modules)
    ]
    if missing_public_ops:
        failures.append(
            "Public SDK is missing public operations: " + ", ".join(missing_public_ops)
        )

    missing_internal_ops = [
        op for op in sorted(all_ops) if not _any_candidate_present(op, internal_modules)
    ]
    if missing_internal_ops:
        failures.append(
            "Internal SDK is missing operations: " + ", ".join(missing_internal_ops)
        )

    public_internal_dirs = list(public_api_dir.rglob("internal"))
    if public_internal_dirs:
        failures.append(
            "Public SDK should not contain internal namespace directories: "
            + ", ".join(str(path) for path in public_internal_dirs)
        )

    if failures:
        for failure in failures:
            print(f"Boundary check failed: {failure}")
        return 1

    print(
        "Boundary check passed: "
        f"{len(public_ops)} public operations, "
        f"{len(internal_only_ops)} internal-only operations."
    )
    return 0


def run_codegen(target: PackageTarget, spec_path: Path, keep_build: bool) -> None:
    version_path = target.source_dir / "_version.py"
    version_content = resolve_version(version_path, spec_path, target.name)

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

    temp_files: list[Path] = []

    try:
        spec_path, is_temp = resolve_spec(args.spec)
        if is_temp:
            temp_files.append(spec_path)

        normalized_spec, normalized_is_temp = normalize_openapi_for_codegen(spec_path)
        if normalized_is_temp:
            print(f"Normalized OpenAPI spec for code generation: {normalized_spec}")
            temp_files.append(normalized_spec)

        # Load spec once for generation and optional verification
        with normalized_spec.open("r", encoding="utf-8") as f:
            parsed_spec = yaml.safe_load(f)

        # Generate internal SDK: use the full (normalized) spec directly
        if args.sdk_type in {"all", "internal"}:
            run_codegen(INTERNAL_TARGET, normalized_spec, keep_build=args.keep_build)
            write_wrapper_files(
                INTERNAL_TARGET.source_dir,
                collect_operations(parsed_spec, INTERNAL_TARGET.source_dir),
                user_agent_name="nadeshiko-internal-sdk-python",
            )

        # Generate public SDK: filter out x-internal operations first
        if args.sdk_type in {"all", "public"}:
            public_spec = filter_public_spec(normalized_spec)
            temp_files.append(public_spec)
            with public_spec.open("r", encoding="utf-8") as f:
                parsed_public_spec = yaml.safe_load(f)
            run_codegen(PUBLIC_TARGET, public_spec, keep_build=args.keep_build)
            write_wrapper_files(
                PUBLIC_TARGET.source_dir,
                collect_operations(parsed_public_spec, PUBLIC_TARGET.source_dir),
                user_agent_name="nadeshiko-sdk-python",
            )

    finally:
        for file_path in temp_files:
            file_path.unlink(missing_ok=True)

    print("Generation complete.")

    if args.verify and args.sdk_type == "all":
        return verify_boundaries(parsed_spec)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
