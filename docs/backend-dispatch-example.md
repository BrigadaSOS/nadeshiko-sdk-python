# Backend Dispatch Example (GitHub Actions)

Trigger Python SDK release workflow from backend release workflow:

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

Notes:
- `release_channel` must be `"stable"` or `"dev"`.
- `backend_sha` is the backend commit SHA to build from.
- The SDK version is derived from the OpenAPI spec's `info.version` at that SHA.
