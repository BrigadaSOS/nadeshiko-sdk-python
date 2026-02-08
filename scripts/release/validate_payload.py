#!/usr/bin/env python3
"""Validate release payload and export normalized values for GitHub Actions."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse

DEFAULT_PUBLIC_SPEC_URL = (
    "https://raw.githubusercontent.com/BrigadaSOS/Nadeshiko/main-v2/"
    "backend/docs/generated/openapi.yaml"
)
DEFAULT_INTERNAL_SPEC_URL = (
    "https://raw.githubusercontent.com/BrigadaSOS/Nadeshiko/main-v2/"
    "backend/docs/generated/openapi-internal.yaml"
)
VERSION_RE = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-((?:0|[1-9A-Za-z-][0-9A-Za-z-]*)(?:\.(?:0|[1-9A-Za-z-][0-9A-Za-z-]*))*))?"
    r"(?:\+([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?$"
)


@dataclass(frozen=True)
class NormalizedPayload:
    version: str
    release_tag: str
    prerelease: bool
    public_spec_url: str
    internal_spec_url: str
    backend_sha: str
    backend_repo: str
    force: bool


def fail(message: str) -> None:
    print(f"Payload validation failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def to_string(value: object, default: str = "") -> str:
    if value is None:
        return default
    return str(value).strip()


def to_bool(value: object, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value
    normalized = to_string(value).lower()
    if not normalized:
        return default
    if normalized in {"true", "1", "yes"}:
        return True
    if normalized in {"false", "0", "no"}:
        return False
    fail(f"Invalid boolean value: {value}")
    return default


def write_output(name: str, value: str) -> None:
    output_path = os.environ.get("GITHUB_OUTPUT", "")
    if not output_path:
        print(f"{name}={value}")
        return
    with Path(output_path).open("a", encoding="utf-8") as file:
        file.write(f"{name}={value}\n")


def parse_event_payload() -> dict[str, object]:
    event_name = os.environ.get("GITHUB_EVENT_NAME", "")
    event_path = os.environ.get("GITHUB_EVENT_PATH", "")

    if event_path and Path(event_path).exists():
        event_data = json.loads(Path(event_path).read_text(encoding="utf-8"))
        if event_name == "repository_dispatch":
            return dict(event_data.get("client_payload", {}))
        if event_name == "workflow_dispatch":
            return dict(event_data.get("inputs", {}))
        if event_name == "push":
            return {}

    # Local fallback for manual testing.
    return {
        "version": os.environ.get("INPUT_VERSION", ""),
        "release_tag": os.environ.get("INPUT_RELEASE_TAG", ""),
        "prerelease": os.environ.get("INPUT_PRERELEASE", ""),
        "public_spec_url": os.environ.get("INPUT_PUBLIC_SPEC_URL", ""),
        "internal_spec_url": os.environ.get("INPUT_INTERNAL_SPEC_URL", ""),
        "backend_sha": os.environ.get("INPUT_BACKEND_SHA", ""),
        "backend_repo": os.environ.get("INPUT_BACKEND_REPO", ""),
        "force": os.environ.get("INPUT_FORCE", ""),
    }


def parse_version_from_ref() -> str:
    ref_name = os.environ.get("GITHUB_REF_NAME", "").strip()
    if not ref_name:
        return ""
    if ref_name.startswith("v"):
        ref_name = ref_name[1:]
    return ref_name


def normalize_version(raw_version: str) -> str:
    version = raw_version.strip()
    if version.startswith("v"):
        version = version[1:]
    if not version:
        fail("`version` is required.")
    if not VERSION_RE.fullmatch(version):
        fail(f"`version` must be semver-compatible. Received: {raw_version}")
    return version


def normalize_release_tag(raw_release_tag: str, version: str) -> str:
    candidate = raw_release_tag.strip() or f"v{version}"
    candidate = candidate.replace("refs/tags/", "")
    if not candidate.startswith("v"):
        candidate = f"v{candidate}"
    if candidate[1:] != version:
        fail(f"release_tag ({candidate}) must match version ({version}).")
    return candidate


def normalize_url(raw_url: str, field_name: str, default_url: str) -> str:
    value = raw_url.strip() or default_url
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        fail(f"`{field_name}` must be a valid http(s) URL. Received: {raw_url}")
    return value


def normalize_payload(raw: dict[str, object]) -> NormalizedPayload:
    version_input = to_string(raw.get("version")) or parse_version_from_ref()
    version = normalize_version(version_input)

    release_tag = normalize_release_tag(to_string(raw.get("release_tag")), version)
    prerelease_by_version = "-" in version
    prerelease = to_bool(raw.get("prerelease"), default=prerelease_by_version)
    if prerelease != prerelease_by_version:
        fail(
            f"`prerelease` ({prerelease}) does not match version ({version})."
        )

    public_spec_url = normalize_url(
        to_string(raw.get("public_spec_url")),
        field_name="public_spec_url",
        default_url=DEFAULT_PUBLIC_SPEC_URL,
    )
    internal_spec_url = normalize_url(
        to_string(raw.get("internal_spec_url")),
        field_name="internal_spec_url",
        default_url=DEFAULT_INTERNAL_SPEC_URL,
    )

    backend_sha = to_string(raw.get("backend_sha")) or "unknown"
    backend_repo = to_string(raw.get("backend_repo")) or "unknown"
    force = to_bool(raw.get("force"), default=False)

    return NormalizedPayload(
        version=version,
        release_tag=release_tag,
        prerelease=prerelease,
        public_spec_url=public_spec_url,
        internal_spec_url=internal_spec_url,
        backend_sha=backend_sha,
        backend_repo=backend_repo,
        force=force,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--print-json",
        action="store_true",
        help="Print normalized payload as JSON to stdout.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    normalized = normalize_payload(parse_event_payload())

    if args.print_json:
        print(
            json.dumps(
                {
                    "version": normalized.version,
                    "release_tag": normalized.release_tag,
                    "prerelease": normalized.prerelease,
                    "public_spec_url": normalized.public_spec_url,
                    "internal_spec_url": normalized.internal_spec_url,
                    "backend_sha": normalized.backend_sha,
                    "backend_repo": normalized.backend_repo,
                    "force": normalized.force,
                },
                indent=2,
            )
        )
        return 0

    print(
        "Release payload OK: "
        f"{normalized.release_tag} (backend {normalized.backend_repo}@{normalized.backend_sha})"
    )
    write_output("version", normalized.version)
    write_output("release_tag", normalized.release_tag)
    write_output("prerelease", str(normalized.prerelease).lower())
    write_output("public_spec_url", normalized.public_spec_url)
    write_output("internal_spec_url", normalized.internal_spec_url)
    write_output("backend_sha", normalized.backend_sha)
    write_output("backend_repo", normalized.backend_repo)
    write_output("force", str(normalized.force).lower())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
