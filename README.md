# Nadeshiko SDK

Python SDK for the [Nadeshiko API](https://nadeshiko.co).

## Install

```bash
pip install nadeshiko-sdk
```

## Use the public SDK

The client sends your API key as `Authorization: Bearer <apiKey>`.

```python
import os

from nadeshiko import Nadeshiko
from nadeshiko.api.search import search
from nadeshiko.models import Error, SearchRequest

client = Nadeshiko(
    base_url=os.getenv("NADESHIKO_BASE_URL", "https://api.nadeshiko.co"),
    token=os.getenv("NADESHIKO_API_KEY", "your-api-key"),
)

result = search.sync(
    client=client,
    body=SearchRequest(query="彼女"),
)

if isinstance(result, Error):
    print(result.code, result.detail)
else:
    for sentence in result.sentences:
        print(sentence.segment_info.content_jp)
```

### Error handling

Every response returns either a typed response object or an `Error`. The `Error` object follows the [RFC 7807](https://tools.ietf.org/html/rfc7807) Problem Details format, so you always get a machine-readable `code` and a human-readable `detail`.

```python
import os

from nadeshiko import Nadeshiko
from nadeshiko.api.search import search
from nadeshiko.models import Error, SearchRequest

client = Nadeshiko(
    base_url=os.getenv("NADESHIKO_BASE_URL", "https://api.nadeshiko.co"),
    token=os.getenv("NADESHIKO_API_KEY", "your-api-key"),
)

result = search.sync(
    client=client,
    body=SearchRequest(query="食べる"),
)

if isinstance(result, Error):
    match result.code:
        # 400 — Bad Request
        case "VALIDATION_FAILED":
            print("Validation failed:", result.detail)
        case "INVALID_JSON":
            print("Malformed JSON body:", result.detail)
        case "INVALID_REQUEST":
            print("Invalid request:", result.detail)

        # 401 — Unauthorized
        case "AUTH_CREDENTIALS_REQUIRED":
            print("Missing API key or session token")
        case "AUTH_CREDENTIALS_INVALID":
            print("API key is invalid")
        case "AUTH_CREDENTIALS_EXPIRED":
            print("Token has expired, re-authenticate")
        case "EMAIL_NOT_VERIFIED":
            print("Email verification required")

        # 403 — Forbidden
        case "ACCESS_DENIED":
            print("Access denied")
        case "INSUFFICIENT_PERMISSIONS":
            print("API key lacks the required scope")

        # 429 — Too Many Requests
        case "RATE_LIMIT_EXCEEDED":
            print("Rate limit hit, slow down")
        case "QUOTA_EXCEEDED":
            print("Monthly quota exhausted")

        # 500 — Internal Server Error
        case "INTERNAL_SERVER_EXCEPTION":
            print("Server error, trace ID:", result.instance)
else:
    for sentence in result.sentences:
        print(sentence.segment_info.content_jp, "—", sentence.basic_info.name_anime_en)
```

See [`examples/examples.py`](examples/examples.py) for more usage patterns.
