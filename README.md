# Nadeshiko Python SDK Monorepo

Monorepo for the Nadeshiko Python SDKs.

## Packages

- `sdk`: public SDK (`nadeshiko-sdk`, import `nadeshiko`)
- `sdk-internal`: internal SDK (`nadeshiko-internal-sdk`, import `nadeshiko_internal`)

## Development

```bash
python -m pip install -e '.[dev]'
```

### Generate SDKs

```bash
python scripts/generate.py --sdk-type all
```

Spec resolution order (per SDK):
- `--public-spec-path` / `--internal-spec-path` when passed
- `--public-spec-url` / `--internal-spec-url` (default: GitHub `main-v2`)
- local fallback: `../Nadeshiko/backend/docs/generated/`

Common options:
- `--sdk-type public`
- `--sdk-type internal`
- `--public-spec-path ...`
- `--internal-spec-path ...`
- `--public-spec-url ...`
- `--internal-spec-url ...`

Local backend example:

```bash
python scripts/generate.py --sdk-type all \
  --public-spec-path ../Nadeshiko/backend/docs/generated/openapi.yaml \
  --internal-spec-path ../Nadeshiko/backend/docs/generated/openapi-internal.yaml
```

### Boundary Check

```bash
python scripts/check_boundaries.py
```

This validates that internal-only operations never appear in the public SDK.

### Build Packages

```bash
python -m build sdk
python -m build sdk-internal
```

## Version Contract

- `sdk/src/nadeshiko/_version.py` and `sdk-internal/src/nadeshiko_internal/_version.py` must match.
- Use:
  - `python scripts/release_version.py set <version>`
  - `python scripts/release_version.py check [version]`

## CI and Release Workflows

- `.github/workflows/ci.yml`
  - lint scripts
  - generate SDKs
  - boundary checks
  - build both packages
  - smoke-install built wheels
- `.github/workflows/release.yml`
  - triggers on tags (`v*`), `repository_dispatch` (`backend_release`), or manual dispatch
  - validates payload with `scripts/release/validate_payload.py`
  - sets aligned versions
  - generates and validates SDKs
  - builds artifacts
  - publishes public package to PyPI when `PYPI_API_TOKEN` is configured
  - publishes internal package to private index when internal publish secrets are configured
- `.github/workflows/consumer-smoke.yml`
  - manual post-release verification from package indexes

## Backend Dispatch Payload

`repository_dispatch` type: `backend_release`

Supported payload fields:
- `version` (semver, no leading `v`)
- `release_tag` (optional, defaults to `v<version>`)
- `prerelease` (`true`/`false`)
- `public_spec_url` (optional; defaults to `main-v2` URL)
- `internal_spec_url` (optional; defaults to `main-v2` URL)
- `backend_sha` (optional metadata)
- `backend_repo` (optional metadata)
- `force` (optional)

See `docs/backend-dispatch-example.md`.

## Consuming From Other Repos

Public package:

```bash
pip install nadeshiko-sdk
```

Internal package (from your private index):

```bash
pip install nadeshiko-internal-sdk
```

Direct from git (fallback):

```bash
pip install "nadeshiko-sdk @ git+https://github.com/BrigadaSOS/nadeshiko-sdk-python.git@main#subdirectory=sdk"
pip install "nadeshiko-internal-sdk @ git+https://github.com/BrigadaSOS/nadeshiko-sdk-python.git@main#subdirectory=sdk-internal"
```

## Authentication

SDK clients use `Authorization: Bearer <token>` by default.
Do not override this to `X-API-Key` unless your backend explicitly expects it.

## Package Examples

- `sdk/examples/usage.py`
- `sdk-internal/examples/usage.py`
