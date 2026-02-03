#!/bin/bash
# Publish script for nadeshiko-sdk to PyPI
# Usage: ./scripts/publish.sh [test|prod]

set -e

ENVIRONMENT="${1:-test}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
VENV_DIR="${XDG_CACHE_HOME:-$HOME/.cache}/nadeshiko-sdk-python/publish-venv"

cd "$PROJECT_ROOT"

echo "================================================"
echo "  Nadeshiko SDK PyPI Publishing Script"
echo "================================================"
echo ""

# Create or use existing venv
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating build virtual environment at $VENV_DIR..."
    python -m venv "$VENV_DIR"
fi
PYTHON="$VENV_DIR/bin/python"
TWINE="$VENV_DIR/bin/twine"

echo "Using virtual environment: $VENV_DIR"
echo ""

# Install build dependencies
echo "Ensuring build dependencies are installed..."
$VENV_DIR/bin/pip install --quiet --upgrade build twine
echo ""

# Clean previous builds
echo "Cleaning previous builds..."
rm -rf dist/ build/ *.egg-info
echo "Done."
echo ""

# Build the package
echo "Building package..."
$PYTHON -m build
echo "Build complete!"
echo ""

# Check the package
echo "Checking package with twine..."
$TWINE check dist/*
echo ""

# List what will be uploaded
echo "Files to upload:"
ls -lh dist/
echo ""

if [ "$ENVIRONMENT" = "prod" ]; then
    echo "================================================"
    echo "  UPLOADING TO PRODUCTION PyPI"
    echo "================================================"
    echo ""
    echo "This will upload to https://pypi.org/p/nadeshiko-sdk"
    echo ""
    read -p "Are you sure you want to continue? (yes/no): " confirm
    if [ "$confirm" != "yes" ]; then
        echo "Aborted."
        exit 1
    fi
    echo ""
    echo "Uploading to PyPI..."
    $TWINE upload dist/*
    echo ""
    echo "================================================"
    echo "  Package published to PyPI!"
    echo "  Install with: pip install nadeshiko-sdk"
    echo "================================================"
else
    echo "================================================"
    echo "  UPLOADING TO TestPyPI"
    echo "================================================"
    echo ""
    echo "This will upload to https://test.pypi.org/p/nadeshiko-sdk"
    echo ""
    read -p "Continue? (yes/no): " confirm
    if [ "$confirm" != "yes" ]; then
        echo "Aborted."
        exit 1
    fi
    echo ""
    echo "Uploading to TestPyPI..."
    $TWINE upload --repository testpypi dist/*
    echo ""
    echo "================================================"
    echo "  Package published to TestPyPI!"
    echo "  Test install with:"
    echo "  pip install --index-url https://test.pypi.org/simple/ nadeshiko-sdk"
    echo "================================================"
fi
