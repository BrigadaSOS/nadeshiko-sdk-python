# Publishing to PyPI

This guide covers how to publish the nadeshiko-sdk package to PyPI.

## Prerequisites

1. **Install build tools**
   ```bash
   pip install --upgrade build twine
   ```

2. **Create PyPI accounts**
   - Production: https://pypi.org/account/register/
   - Test (recommended first): https://test.pypi.org/account/register/

3. **Configure authentication** (recommended)

   Create `~/.pypirc`:
   ```ini
   [distutils]
   index-servers =
       pypi
       testpypi

   [pypi]
   username = __token__
   password = <your-pypi-api-token>

   [testpypi]
   username = __token__
   password = <your-testpypi-api-token>
   ```

   Get API tokens from:
   - Production: https://pypi.org/manage/account/token/
   - Test: https://test.pypi.org/manage/account/token/

## Quick Publish

Use the provided script:

```bash
# Test PyPI (default)
./scripts/publish.sh

# Production PyPI
./scripts/publish.sh prod
```

## Manual Steps

If you prefer to do it manually:

### 1. Build the package

```bash
python -m build
```

This creates `dist/nadeshiko-sdk-<version>.tar.gz` and `dist/nadeshiko_sdk-<version>-py3-none-any.whl`.

### 2. Check the package

```bash
twine check dist/*
```

### 3. Upload

To TestPyPI:
```bash
twine upload --repository testpypi dist/*
```

To production PyPI:
```bash
twine upload dist/*
```

### 4. Verify installation

TestPyPI:
```bash
pip install --index-url https://test.pypi.org/simple/ nadeshiko-sdk
```

Production:
```bash
pip install nadeshiko-sdk
```

## Pre-Publish Checklist

- [ ] Version updated in `src/nadeshiko/_version.py`
- [ ] `pyproject.toml` has correct metadata
- [ ] README.md is up to date
- [ ] Tests pass (if applicable)
- [ ] Tested locally with `pip install -e .`

## Version Bumping

To release a new version:

1. Update `src/nadeshiko/_version.py`
2. Commit the change
3. Optionally create a git tag
4. Run the publish script

## Troubleshooting

**"403 Forbidden" or "Invalid or non-existent authentication"**
- Check your API token in `~/.pypirc`
- Ensure the token has correct permissions

**"Package already exists"**
- Increment the version in `src/nadeshiko/_version.py`
- Run `python -m build` again

**Build fails**
- Ensure `build` and `twine` are up to date
- Check that all dependencies in `pyproject.toml` are valid
