#!/usr/bin/env python3
"""Check that public SDK outputs do not leak internal-only operations."""

from __future__ import annotations

import argparse
import os
import re
from pathlib import Path
from urllib.request import Request, urlopen

import yaml

ROOT_DIR = Path(__file__).resolve().parent.parent
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


def env_path(name: str) -> Path | None:
    value = os.environ.get(name, "").strip()
    if not value:
        return None
    return Path(value)


def resolve_input_path(path: Path) -> Path:
    if path.is_absolute():
        return path
    return (ROOT_DIR / path).resolve()


def fetch_spec_to_temp(url: str) -> Path:
    request = Request(url, headers={"User-Agent": "nadeshiko-sdk-python-boundary-check"})
    with urlopen(request, timeout=30) as response:  # noqa: S310
        content = response.read()

    import tempfile

    with tempfile.NamedTemporaryFile(
        prefix="nadeshiko-boundary-spec-",
        suffix=".yaml",
        delete=False,
    ) as tmp:
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
            fetched_path = fetch_spec_to_temp(spec_url)
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
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
        "--public-api-dir",
        type=Path,
        default=ROOT_DIR / "sdk" / "src" / "nadeshiko" / "api",
        help="Path to generated public API package directory.",
    )
    parser.add_argument(
        "--internal-api-dir",
        type=Path,
        default=ROOT_DIR / "sdk-internal" / "src" / "nadeshiko_internal" / "api",
        help="Path to generated internal API package directory.",
    )
    return parser.parse_args()


def operation_ids(spec_path: Path) -> set[str]:
    with spec_path.open("r", encoding="utf-8") as file:
        spec = yaml.safe_load(file)

    operation_id_set: set[str] = set()
    for path_item in spec.get("paths", {}).values():
        for method, operation in path_item.items():
            if method in {"parameters", "$ref"}:
                continue
            if not isinstance(operation, dict):
                continue
            operation_id = operation.get("operationId")
            if operation_id:
                operation_id_set.add(operation_id)

    return operation_id_set


def operation_id_to_snake(operation_id: str) -> str:
    step_one = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", operation_id)
    step_two = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", step_one)
    return step_two.lower()


def operation_module_candidates(operation_id: str) -> set[str]:
    base = operation_id_to_snake(operation_id)
    return {base, f"{base}_"}


def api_modules(api_dir: Path) -> set[str]:
    modules: set[str] = set()
    for file_path in api_dir.rglob("*.py"):
        if file_path.name == "__init__.py":
            continue
        modules.add(file_path.stem)
    return modules


def any_candidate_present(operation_id: str, modules: set[str]) -> bool:
    return bool(operation_module_candidates(operation_id) & modules)


def main() -> int:
    args = parse_args()

    temp_files: list[Path] = []

    public_spec_path, public_is_temp = resolve_spec_path(
        spec_name="public",
        explicit_path=args.public_spec_path,
        spec_url=args.public_spec_url.strip(),
        fallback_path=DEFAULT_PUBLIC_LOCAL_SPEC,
    )
    internal_spec_path, internal_is_temp = resolve_spec_path(
        spec_name="internal",
        explicit_path=args.internal_spec_path,
        spec_url=args.internal_spec_url.strip(),
        fallback_path=DEFAULT_INTERNAL_LOCAL_SPEC,
    )
    if public_is_temp:
        temp_files.append(public_spec_path)
    if internal_is_temp:
        temp_files.append(internal_spec_path)

    try:
        public_ops = operation_ids(public_spec_path)
        internal_ops = operation_ids(internal_spec_path)
        internal_only_ops = internal_ops - public_ops

        failures: list[str] = []

        if not args.public_api_dir.exists():
            failures.append(f"Missing public API directory: {args.public_api_dir}")
        if not args.internal_api_dir.exists():
            failures.append(f"Missing internal API directory: {args.internal_api_dir}")

        if failures:
            for failure in failures:
                print(f"Boundary check failed: {failure}")
            return 1

        public_modules = api_modules(args.public_api_dir)
        internal_modules = api_modules(args.internal_api_dir)

        leaked_ops = [
            op for op in sorted(internal_only_ops) if any_candidate_present(op, public_modules)
        ]
        if leaked_ops:
            failures.append(
                f"Public SDK contains internal-only operations: {', '.join(leaked_ops)}"
            )

        missing_public_ops = [
            op for op in sorted(public_ops) if not any_candidate_present(op, public_modules)
        ]
        if missing_public_ops:
            failures.append(
                "Public SDK is missing public operations: " + ", ".join(missing_public_ops)
            )

        missing_internal_only_ops = [
            op
            for op in sorted(internal_only_ops)
            if not any_candidate_present(op, internal_modules)
        ]
        if missing_internal_only_ops:
            failures.append(
                "Internal SDK is missing internal-only operations: "
                + ", ".join(missing_internal_only_ops)
            )

        missing_internal_ops = [
            op for op in sorted(internal_ops) if not any_candidate_present(op, internal_modules)
        ]
        if missing_internal_ops:
            failures.append(
                "Internal SDK is missing operations: " + ", ".join(missing_internal_ops)
            )

        public_internal_dirs = list(args.public_api_dir.rglob("internal"))
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
    finally:
        for file_path in temp_files:
            file_path.unlink(missing_ok=True)


if __name__ == "__main__":
    raise SystemExit(main())
