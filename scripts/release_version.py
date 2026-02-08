#!/usr/bin/env python3
"""Set or check SDK package versions."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
PUBLIC_VERSION_FILE = ROOT_DIR / "sdk" / "src" / "nadeshiko" / "_version.py"
INTERNAL_VERSION_FILE = ROOT_DIR / "sdk-internal" / "src" / "nadeshiko_internal" / "_version.py"

VERSION_RE = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-((?:0|[1-9A-Za-z-][0-9A-Za-z-]*)(?:\.(?:0|[1-9A-Za-z-][0-9A-Za-z-]*))*))?"
    r"(?:\+([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?$"
)
FILE_VERSION_RE = re.compile(r'__version__\s*=\s*"([^"]+)"')


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_set = subparsers.add_parser("set", help="Set both package versions to the same value.")
    parser_set.add_argument("version", help="Semver value without leading v, e.g. 1.2.3")

    parser_check = subparsers.add_parser("check", help="Check package versions are aligned.")
    parser_check.add_argument(
        "version",
        nargs="?",
        default="",
        help="Optional expected semver value (without leading v).",
    )

    return parser.parse_args()


def normalize_version(value: str, *, context: str) -> str:
    normalized = value.strip()
    if normalized.startswith("v"):
        normalized = normalized[1:]
    if not VERSION_RE.fullmatch(normalized):
        raise ValueError(f"Invalid semver in {context}: {value}")
    return normalized


def read_version(path: Path) -> str:
    content = path.read_text(encoding="utf-8")
    match = FILE_VERSION_RE.search(content)
    if not match:
        raise ValueError(f"Could not find __version__ assignment in {path}")
    return normalize_version(match.group(1), context=str(path))


def write_version(path: Path, version: str) -> None:
    content = path.read_text(encoding="utf-8")
    if FILE_VERSION_RE.search(content):
        updated = FILE_VERSION_RE.sub(f'__version__ = "{version}"', content, count=1)
    else:
        updated = content.rstrip() + f'\n\n__version__ = "{version}"\n'
    path.write_text(updated, encoding="utf-8")


def cmd_set(version: str) -> int:
    normalized = normalize_version(version, context="CLI argument")
    write_version(PUBLIC_VERSION_FILE, normalized)
    write_version(INTERNAL_VERSION_FILE, normalized)
    print(f"Set sdk and sdk-internal version to {normalized}")
    return 0


def cmd_check(expected: str) -> int:
    public_version = read_version(PUBLIC_VERSION_FILE)
    internal_version = read_version(INTERNAL_VERSION_FILE)

    failures: list[str] = []
    if public_version != internal_version:
        failures.append(
            f"Version mismatch: sdk={public_version} sdk-internal={internal_version}"
        )

    if expected:
        expected_version = normalize_version(expected, context="expected version")
        if public_version != expected_version:
            failures.append(
                "Version does not match expected: "
                f"expected={expected_version} actual={public_version}"
            )

    if failures:
        for failure in failures:
            print(f"Release version check failed: {failure}")
        return 1

    print(f"Release version check passed: {public_version}")
    return 0


def main() -> int:
    args = parse_args()
    if args.command == "set":
        return cmd_set(args.version)
    if args.command == "check":
        return cmd_check(args.version)
    raise ValueError(f"Unknown command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
