#!/usr/bin/env python3
"""Build a publishable Python package from generated SDK sources.

Creates a staging area under build/<target>/ with the proper layout for
``python -m build``, then invokes it to produce sdist + wheel artifacts.

Usage:
    python scripts/build_package.py <public|internal|dev>
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import textwrap
from pathlib import Path
from typing import Literal

ROOT_DIR = Path(__file__).resolve().parent.parent

BuildTarget = Literal["public", "internal", "dev"]

DEPENDENCIES = [
    "attrs>=23.0",
    "httpx>=0.27.0",
    "python-dateutil>=2.8.0",
]

TARGET_META: dict[BuildTarget, dict[str, str]] = {
    "public": {
        "package_name": "nadeshiko-sdk",
        "import_name": "nadeshiko",
        "description": "Python SDK for Nadeshiko API (public endpoints only)",
        "version_env": "SDK_VERSION",
    },
    "internal": {
        "package_name": "nadeshiko-internal-sdk",
        "import_name": "nadeshiko_internal",
        "description": (
            "Python SDK for Nadeshiko API (internal build - includes internal endpoints)"
        ),
        "version_env": "INTERNAL_VERSION",
    },
    "dev": {
        "package_name": "nadeshiko-internal-sdk",
        "import_name": "nadeshiko_internal",
        "description": (
            "Python SDK for Nadeshiko API (internal build - includes internal endpoints)"
        ),
        "version_env": "INTERNAL_VERSION",
    },
}


def fail(message: str) -> None:
    print(f"Build failed: {message}", file=sys.stderr)
    sys.exit(1)


def resolve_target() -> BuildTarget:
    if len(sys.argv) < 2:
        fail("Usage: python scripts/build_package.py <public|internal|dev>")
    value = sys.argv[1].strip().lower()
    if value not in ("public", "internal", "dev"):
        fail("Usage: python scripts/build_package.py <public|internal|dev>")
    return value  # type: ignore[return-value]


def read_version(version_file: Path, env_var: str) -> str:
    env_version = os.environ.get(env_var, "").strip()
    if env_version:
        return env_version
    if not version_file.exists():
        fail(f"Version file not found: {version_file}")
    text = version_file.read_text(encoding="utf-8")
    match = re.search(r'__version__\s*=\s*"([^"]+)"', text)
    if not match:
        fail(f"Could not parse __version__ from {version_file}")
    return match.group(1)


def generate_pyproject_toml(
    *,
    package_name: str,
    import_name: str,
    description: str,
    version_path: str,
) -> str:
    deps_lines = "\n".join(f'    "{dep}",' for dep in DEPENDENCIES)
    return textwrap.dedent(f"""\
        [build-system]
        requires = ["hatchling"]
        build-backend = "hatchling.build"

        [project]
        name = "{package_name}"
        dynamic = ["version"]
        description = "{description}"
        readme = "README.md"
        license = "MIT"
        requires-python = ">=3.11"
        dependencies = [
        {deps_lines}
        ]

        [tool.hatch.version]
        path = "{version_path}"

        [tool.hatch.build.targets.wheel]
        packages = ["src/{import_name}"]
    """)


def main() -> None:
    target = resolve_target()
    meta = TARGET_META[target]

    package_name: str = meta["package_name"]
    import_name: str = meta["import_name"]
    description: str = meta["description"]
    version_env: str = meta["version_env"]

    source_dir = ROOT_DIR / "generated" / target / import_name
    build_dir = ROOT_DIR / "build" / target
    staging_src = build_dir / "src" / import_name

    if not source_dir.exists():
        fail(f"Missing generated source directory: {source_dir}. Run generation first.")

    version_file = source_dir / "_version.py"
    version = read_version(version_file, version_env)
    print(f"Building {package_name} v{version} ({target})")

    if build_dir.exists():
        shutil.rmtree(build_dir)
    build_dir.mkdir(parents=True, exist_ok=True)

    shutil.copytree(source_dir, staging_src)

    pyproject_content = generate_pyproject_toml(
        package_name=package_name,
        import_name=import_name,
        description=description,
        version_path=f"src/{import_name}/_version.py",
    )
    (build_dir / "pyproject.toml").write_text(pyproject_content, encoding="utf-8")

    readme_src = ROOT_DIR / "README.md"
    license_src = ROOT_DIR / "LICENSE"

    if readme_src.exists():
        shutil.copy2(readme_src, build_dir / "README.md")

    if license_src.exists():
        shutil.copy2(license_src, build_dir / "LICENSE")
    else:
        fail("No LICENSE file found at repository root.")

    dist_dir = build_dir / "dist"
    result = subprocess.run(  # noqa: S603
        [sys.executable, "-m", "build", str(build_dir), "--outdir", str(dist_dir)],
        check=False,
    )

    if result.returncode != 0:
        sys.exit(result.returncode)

    print(f"Built {target} package: {build_dir}")


if __name__ == "__main__":
    main()
