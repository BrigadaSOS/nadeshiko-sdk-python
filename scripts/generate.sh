#!/usr/bin/env bash
set -euo pipefail

# Generate Nadeshiko Python SDK from OpenAPI specs
# Generates a single package with namespaced internal endpoints:
#   - api/{module}/       - Public endpoints
#   - api/{module}/internal/ - Internal endpoints
#
# Usage: ./scripts/generate.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_ROOT"

echo "=== Nadeshiko Python SDK Generation ==="

# Check if openapi-python-client is installed
if ! command -v openapi-python-client &> /dev/null; then
    echo "Error: openapi-python-client not found"
    echo "Install with: pip install openapi-python-client"
    exit 1
fi

# Preserve _version.py
VERSION_CONTENT=$(cat src/nadeshiko/_version.py 2>/dev/null || echo '__version__ = "0.1.0"')

# Build directories
PUBLIC_BUILD_DIR="build/public"
INTERNAL_BUILD_DIR="build/internal"

rm -rf build src/nadeshiko/
mkdir -p "$PUBLIC_BUILD_DIR" "$INTERNAL_BUILD_DIR"

# ===== Generate Public SDK =====
echo ""
echo "--- Generating public SDK ---"
openapi-python-client generate \
    --path openapi-spec/openapi.yaml \
    --output-path "$PUBLIC_BUILD_DIR" \
    --config openapi-client-config.yaml \
    --custom-template-path templates \
    --meta none \
    --overwrite

# ===== Generate Internal SDK =====
echo ""
echo "--- Generating internal SDK ---"
openapi-python-client generate \
    --path openapi-spec/openapi-internal.yaml \
    --output-path "$INTERNAL_BUILD_DIR" \
    --config openapi-client-config.yaml \
    --custom-template-path templates \
    --meta none \
    --overwrite

# ===== Merge and Organize =====
echo ""
echo "--- Merging and organizing endpoints ---"

# Create target directory
mkdir -p src/nadeshiko

# Copy base structure (client.py, __init__.py, models, etc.) from internal
cp -r "$INTERNAL_BUILD_DIR"/* "src/nadeshiko/"

# Restore _version.py
echo "$VERSION_CONTENT" > src/nadeshiko/_version.py

# Get list of all API modules in internal build (directories only, not __init__.py)
INTERNAL_MODULES=$(find "$INTERNAL_BUILD_DIR/api/" -mindepth 1 -maxdepth 1 -type d -exec basename {} \; 2>/dev/null || true)

# Modules that exist in public spec
PUBLIC_MODULES="search media lists"

echo "Public modules: $PUBLIC_MODULES"
echo "Internal modules: $INTERNAL_MODULES"

# For each public module, we need to split into public and internal
for module in $PUBLIC_MODULES; do
    if [ ! -d "$INTERNAL_BUILD_DIR/api/$module" ]; then
        continue
    fi

    echo ""
    echo "Processing $module..."

    # Get list of all functions in internal module
    INTERNAL_FUNCS=$(find "$INTERNAL_BUILD_DIR/api/$module/" -maxdepth 1 -name "*.py" -exec basename {} .py \; 2>/dev/null | grep -v __init__ || true)

    # Get list of functions in public module (if exists)
    PUBLIC_FUNCS=""
    if [ -d "$PUBLIC_BUILD_DIR/api/$module" ]; then
        PUBLIC_FUNCS=$(find "$PUBLIC_BUILD_DIR/api/$module/" -maxdepth 1 -name "*.py" -exec basename {} .py \; 2>/dev/null | grep -v __init__ || true)
    fi

    echo "  Internal functions: $INTERNAL_FUNCS"
    echo "  Public functions: $PUBLIC_FUNCS"

    # Create internal subdirectory
    mkdir -p "src/nadeshiko/api/$module/internal"

    # Move internal-only functions to internal subdirectory
    for func in $INTERNAL_FUNCS; do
        # Check if this function is NOT in public list
        is_internal="yes"
        for pub_func in $PUBLIC_FUNCS; do
            if [ "$func" = "$pub_func" ]; then
                is_internal="no"
                break
            fi
        done

        if [ "$is_internal" = "yes" ]; then
            # This is an internal-only function
            if [ -f "src/nadeshiko/api/$module/$func.py" ]; then
                mv "src/nadeshiko/api/$module/$func.py" "src/nadeshiko/api/$module/internal/$func.py"
                echo "  - Moved $func to $module/internal/"
            fi
        fi
    done

    # Update __init__.py in internal subdirectory
    cat > "src/nadeshiko/api/$module/internal/__init__.py" << 'EOF'
from typing import Any
import httpx
from .... import errors
from ....client import AuthenticatedClient, Client
from ....types import Response

EOF

    # Add imports for internal functions
    for func_py in "src/nadeshiko/api/$module/internal"/*.py; do
        if [ -f "$func_py" ]; then
            func_name=$(basename "$func_py" .py)
            if [ "$func_name" != "__init__" ]; then
                echo "from . import $func_name" >> "src/nadeshiko/api/$module/internal/__init__.py"
                # Fix relative imports in the moved file (add 2 more dots for internal/ subdirectory)
                sed -i 's/from \.\.\./from ..../g' "$func_py"
            fi
        fi
    done
done

# For internal-only modules, we need a different approach
# Since they're not in public spec, we create the parent dir with internal/ subdirectory
for module in $INTERNAL_MODULES; do
    if ! echo " $PUBLIC_MODULES " | grep -q " $module "; then
        echo ""
        echo "Processing internal-only module: $module..."

        # Create parent directory with internal subdirectory
        mkdir -p "src/nadeshiko/api/$module/internal"

        # Move all functions to internal subdirectory
        for func_py in "src/nadeshiko/api/$module"/*.py; do
            if [ -f "$func_py" ]; then
                func_name=$(basename "$func_py")
                if [ "$func_name" != "__init__.py" ]; then
                    mv "$func_py" "src/nadeshiko/api/$module/internal/"
                fi
            fi
        done

        echo "  - Moved $module to $module/internal/"

        # Create empty __init__.py in parent (no public exports)
        cat > "src/nadeshiko/api/$module/__init__.py" << 'EOF'
# This module has no public endpoints.
# Internal endpoints are available in the .internal submodule.

EOF

        # Update __init__.py in internal subdirectory
        cat > "src/nadeshiko/api/$module/internal/__init__.py" << 'EOF'
from typing import Any
import httpx
from .... import errors
from ....client import AuthenticatedClient, Client
from ....types import Response

EOF

        # Add imports for internal functions
        for func_py in "src/nadeshiko/api/$module/internal"/*.py; do
            if [ -f "$func_py" ]; then
                func_name=$(basename "$func_py" .py)
                if [ "$func_name" != "__init__" ]; then
                    echo "from . import $func_name" >> "src/nadeshiko/api/$module/internal/__init__.py"
                    # Fix relative imports in the moved file (add 2 more dots for internal/ subdirectory)
                    sed -i 's/from \.\.\./from ..../g' "$func_py"
                fi
            fi
        done
    fi
done

# Update module __init__.py files to only export public functions
for module in $PUBLIC_MODULES; do
    if [ -d "src/nadeshiko/api/$module" ]; then
        cat > "src/nadeshiko/api/$module/__init__.py" << 'EOF'
from typing import Any
import httpx
from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response

EOF
        # Add imports for remaining (public) functions
        for func_py in "src/nadeshiko/api/$module"/*.py; do
            if [ -f "$func_py" ]; then
                func_name=$(basename "$func_py" .py)
                if [ "$func_name" != "__init__" ]; then
                    echo "from . import $func_name" >> "src/nadeshiko/api/$module/__init__.py"
                fi
            fi
        done
    fi
done

# Clean up
rm -rf "$PUBLIC_BUILD_DIR" "$INTERNAL_BUILD_DIR" build
rm -rf src/nadeshiko/.ruff_cache

echo ""
echo "=== Generation Complete ==="
echo "Single client: Nadeshiko"
echo "  - api/search/        - Public search endpoints"
echo "  - api/media/         - Public media endpoints"
echo "  - api/lists/         - Public lists endpoints"
echo "  - api/media/internal/ - Internal media endpoints"
echo "  - api/lists/internal/ - Internal lists endpoints"
echo "  - api/user/internal/  - Internal user endpoints"
echo "  - api/auth/internal/  - Internal auth endpoints"
echo "  - api/auth_jwt/internal/ - Internal auth_jwt endpoints"
