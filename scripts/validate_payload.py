#!/usr/bin/env python3
"""Validate release payload and export normalized values for GitHub Actions."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from urllib.request import Request, urlopen

import yaml

BACKEND_REPO = "BrigadaSOS/Nadeshiko"
SPEC_PATH = "backend/docs/generated/openapi.yaml"

SEMVER_REGEX = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-((?:0|[1-9A-Za-z-][0-9A-Za-z-]*)(?:\.(?:0|[1-9A-Za-z-][0-9A-Za-z-]*))*))?"
    r"(?:\+([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?$"
)


@dataclass(frozen=True)
class DerivedVersions:
    spec_version: str
    public_version: str
    internal_version: str
    internal_only: bool


def fail(message: str) -> None:
    print(f"Payload validation failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def to_string(value: object, default: str = "") -> str:
    if value is None:
        return default
    return str(value).strip()


def write_output(name: str, value: str) -> None:
    output_path = os.environ.get("GITHUB_OUTPUT", "")
    if not output_path:
        print(f"{name}={value}")
        return
    delimiter = f"EOF_{name}_{int(time.time())}"
    with Path(output_path).open("a", encoding="utf-8") as f:
        f.write(f"{name}<<{delimiter}\n{value}\n{delimiter}\n")


def parse_event_payload() -> dict[str, object]:
    event_name = os.environ.get("GITHUB_EVENT_NAME", "")
    event_path = os.environ.get("GITHUB_EVENT_PATH", "")

    if event_path and Path(event_path).exists():
        event_data = json.loads(Path(event_path).read_text(encoding="utf-8"))
        if event_name == "repository_dispatch":
            return dict(event_data.get("client_payload", {}))
        if event_name == "workflow_dispatch":
            return dict(event_data.get("inputs", {}))

    # Local fallback for manual testing.
    return {
        "release_channel": os.environ.get("INPUT_RELEASE_CHANNEL", ""),
        "backend_sha": os.environ.get("INPUT_BACKEND_SHA", ""),
    }


def resolve_channel(raw: object) -> str:
    value = to_string(raw).lower()
    if value == "dev":
        return "dev"
    if value == "stable" or not value:
        return "stable"
    fail(f'`release_channel` must be "dev" or "stable". Received: "{value}"')
    return "stable"  # unreachable, satisfies type checker


def load_spec_version(spec_url: str) -> str:
    if spec_url.startswith("file://"):
        file_path = spec_url.removeprefix("file://")
        source = Path(file_path).read_text(encoding="utf-8")
    else:
        request = Request(spec_url)  # noqa: S310
        with urlopen(request) as response:  # noqa: S310
            if response.status != 200:
                fail(
                    f"Failed to fetch spec_url ({spec_url}):"
                    f" {response.status} {response.reason}"
                )
            source = response.read().decode("utf-8")

    spec = yaml.safe_load(source)
    spec_version = to_string(spec.get("info", {}).get("version"))
    if not spec_version:
        fail("OpenAPI spec is missing `info.version`.")
    return spec_version


def derive_versions(
    spec_version: str, channel: str, backend_sha: str
) -> DerivedVersions:
    semver_match = SEMVER_REGEX.match(spec_version)
    if not semver_match:
        fail(f'Spec info.version must be semver compatible. Received: "{spec_version}"')
        raise AssertionError("unreachable")

    build_metadata = semver_match.group(5) or ""
    if build_metadata:
        fail(
            "Spec info.version must not include build metadata (+...)."
            f' Received: "{spec_version}"'
        )

    base_version = f"{semver_match.group(1)}.{semver_match.group(2)}.{semver_match.group(3)}"

    if channel == "dev":
        short_sha = backend_sha[:7]
        return DerivedVersions(
            spec_version=spec_version,
            public_version=base_version,
            internal_version=f"{base_version}.dev{short_sha}",
            internal_only=True,
        )

    # Stable channel
    return DerivedVersions(
        spec_version=spec_version,
        public_version=base_version,
        internal_version=base_version,
        internal_only=False,
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
    raw_payload = parse_event_payload()

    channel = resolve_channel(raw_payload.get("release_channel"))

    backend_sha = to_string(raw_payload.get("backend_sha"))
    if not backend_sha:
        fail("`backend_sha` is required.")

    spec_url = f"https://raw.githubusercontent.com/{BACKEND_REPO}/{backend_sha}/{SPEC_PATH}"
    backend_repo = BACKEND_REPO

    spec_version = load_spec_version(spec_url)
    derived = derive_versions(spec_version, channel, backend_sha)

    release_tag = f"v{derived.spec_version}" if channel == "stable" else ""
    prerelease = channel == "dev"

    if args.print_json:
        print(
            json.dumps(
                {
                    "release_channel": channel,
                    "spec_version": derived.spec_version,
                    "public_version": derived.public_version,
                    "internal_version": derived.internal_version,
                    "internal_only": derived.internal_only,
                    "release_tag": release_tag,
                    "prerelease": prerelease,
                    "spec_url": spec_url,
                    "backend_sha": backend_sha,
                    "backend_repo": backend_repo,
                },
                indent=2,
            )
        )
        return 0

    print(
        f"Release payload OK: channel={channel}"
        f" from {backend_repo}@{backend_sha} (spec={derived.spec_version})"
    )
    print(
        f"Publish plan: public={derived.public_version}"
        f" internal={derived.internal_version} internal_only={derived.internal_only}"
    )

    write_output("release_channel", channel)
    write_output("spec_version", derived.spec_version)
    write_output("public_version", derived.public_version)
    write_output("internal_version", derived.internal_version)
    write_output("internal_only", str(derived.internal_only).lower())
    write_output("release_tag", release_tag)
    write_output("prerelease", str(prerelease).lower())
    write_output("spec_url", spec_url)
    write_output("backend_sha", backend_sha)
    write_output("backend_repo", backend_repo)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
