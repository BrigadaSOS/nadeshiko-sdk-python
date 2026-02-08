# Backend Dispatch Example (GitHub Actions)

Trigger Python SDK release workflow from backend release workflow:

```yaml
- name: Dispatch Python SDK release
  env:
    GH_TOKEN: ${{ secrets.SDK_REPO_DISPATCH_TOKEN }}
    VERSION: ${{ github.event.release.tag_name }}
    RELEASE_TAG: ${{ github.event.release.tag_name }}
    BACKEND_SHA: ${{ github.event.release.target_commitish }}
    BACKEND_REPO: ${{ github.repository }}
    PUBLIC_SPEC_URL: https://raw.githubusercontent.com/BrigadaSOS/Nadeshiko/main-v2/backend/docs/generated/openapi.yaml
    INTERNAL_SPEC_URL: https://raw.githubusercontent.com/BrigadaSOS/Nadeshiko/main-v2/backend/docs/generated/openapi-internal.yaml
  run: |
    VERSION_NO_V="${VERSION#v}"
    gh api repos/BrigadaSOS/nadeshiko-sdk-python/dispatches \
      -f event_type='backend_release' \
      -f client_payload[version]="$VERSION_NO_V" \
      -f client_payload[release_tag]="$RELEASE_TAG" \
      -f client_payload[prerelease]="${{ github.event.release.prerelease }}" \
      -f client_payload[public_spec_url]="$PUBLIC_SPEC_URL" \
      -f client_payload[internal_spec_url]="$INTERNAL_SPEC_URL" \
      -f client_payload[backend_sha]="$BACKEND_SHA" \
      -f client_payload[backend_repo]="$BACKEND_REPO"
```

Notes:
- Use release-pinned immutable spec URLs when available.
- `version` must be semver without a leading `v`.
- `release_tag` must match `v<version>`.
