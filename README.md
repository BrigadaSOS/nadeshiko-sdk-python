# Nadeshiko Python SDK

Python SDK for the [Nadeshiko API](https://nadeshiko.co).

## Install

Public package:

```bash
pip install nadeshiko-sdk
```

Internal package:

```bash
pip install nadeshiko-internal-sdk
```

## Usage

```python
import os
from nadeshiko import Nadeshiko
from nadeshiko.api.search import search

client = Nadeshiko(
    base_url=os.getenv("NADESHIKO_BASE_URL", "https://api.nadeshiko.co"),
    token=os.getenv("NADESHIKO_API_KEY", "your-api-key"),
)

result = search.sync(client=client, body={"query": "彼女", "limit": 5})
```

## Development

```bash
python -m pip install -e '.[dev]'
```

### Generate SDKs

```bash
python scripts/generate.py --sdk-type all
```

Spec source (`--spec` or `OPENAPI_SPEC_PATH` env var): accepts a URL or local file path.
When omitted, fetches from GitHub `main-v2` with local fallback to `../Nadeshiko/backend/docs/generated/openapi.yaml`.

The single spec uses `x-internal` flags on operations to split public/internal SDKs.
Generation automatically verifies that `x-internal` operations never leak into the public SDK (disable with `--no-verify`).

### Build Packages

```bash
python scripts/build_package.py public
python scripts/build_package.py internal
```

Outputs wheels and sdists to `build/public/dist/` and `build/internal/dist/`.

## Project Layout

```
generated/
  public/nadeshiko/          # Filtered (no x-internal ops)
  internal/nadeshiko_internal/ # Full spec (all ops)
build/                        # .gitignored
  public/                     # Staging + dist (wheel, sdist)
  internal/
config/
  public.yaml                 # openapi-python-client config
  internal.yaml
templates/
  package_init.py.jinja
examples/
  usage.py
  usage_internal.py
scripts/
  generate.py
  build_package.py
  release/validate_payload.py
```

## CI and Release

- `.github/workflows/ci.yml` — lint, generate, build, smoke test
- `.github/workflows/release.yml` — triggered by `repository_dispatch` (`backend_release`) or manual dispatch

### Backend Dispatch Payload

```yaml
- name: Dispatch Python SDK release
  env:
    GH_TOKEN: ${{ secrets.SDK_REPO_DISPATCH_TOKEN }}
  run: |
    gh api repos/BrigadaSOS/nadeshiko-sdk-python/dispatches \
      -f event_type='backend_release' \
      -f client_payload[release_channel]="stable" \
      -f client_payload[backend_sha]="${{ github.sha }}"
```

See `docs/backend-dispatch-example.md`.

## Authentication

SDK clients use `Authorization: Bearer <token>` by default.
