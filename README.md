> This repository is still in WIP and not ready for production use

# Nadeshiko Python SDK

[![PyPI](https://img.shields.io/pypi/v/nadeshiko-sdk)](https://pypi.org/project/nadeshiko-sdk/)


Python SDK for the [Nadeshiko API](https://nadeshiko.co)

## Quick Start

```python
from nadeshiko import Nadeshiko, Environment
from nadeshiko.api.search import search

# Configure your client
client = Nadeshiko(
    api_key='your-api-key-here',
    base_url=Environment.PRODUCTION,  # or Environment.LOCAL, or custom URL
)

# Use API methods (names match OpenAPI operationIds)
result = search.sync(
    client=client,
    body={
        'query': '彼女',
        'limit': 10,
    },
)

if isinstance(result, Error):
    print(result.code, result.detail)
else:
    print(result.sentences)
```

## API Methods

All methods are organized under `nadeshiko.api.{module}` and match the OpenAPI operationIds exactly:

You can check the full specification from the [OpenAPI spec page](https://nadeshiko.co/api/v1/docs).

## Error Handling

All methods return a union type: `Response | Error | None`.

**Check for errors:**
```python
from nadeshiko import Nadeshiko, Environment
from nadeshiko.api.search import search
from nadeshiko.models import Error

client = Nadeshiko(api_key='your-api-key', base_url=Environment.PRODUCTION)
result = search.sync(client=client, body={'query': '彼女'})

if isinstance(result, Error):
    # Error type is fully generated from OpenAPI spec
    print(result.code)    # e.g., 'RATE_LIMIT_EXCEEDED'
    print(result.title)   # e.g., 'Rate Limit Exceeded'
    print(result.detail)  # Detailed message
    print(result.status)  # HTTP status code
else:
    print(result.sentences)
```

In general, all SDK methods return typed errors generated from the OpenAPI spec:

```python
class Error:
    code: str                 # e.g., 'RATE_LIMIT_EXCEEDED', 'AUTH_CREDENTIALS_INVALID'
    title: str                # Short summary
    detail: str               # Detailed explanation
    status: int               # HTTP status code
    type_: str | Unset        # URI to error documentation
    instance: str | Unset     # Trace ID
    errors: dict | Unset      # Validation errors
```

Handle each error independently based on the error code returned by the API.

```python
from nadeshiko import Nadeshiko, Environment
from nadeshiko.api.search import search
from nadeshiko.models import Error

client = Nadeshiko(api_key='your-api-key')
result = search.sync(client=client, body={'query': '彼女'})

if isinstance(result, Error):
    # All error fields are typed
    match result.code:
        case 'RATE_LIMIT_EXCEEDED':
            print('Wait before retrying')
        case 'AUTH_CREDENTIALS_INVALID':
            print('Check your API key')
        case 'VALIDATION_FAILED':
            print('Field errors:', result.errors)
        case _:
            print(result.detail)
```

You can check the full list of errors codes for each endpoint from the [OpenAPI spec page](https://nadeshiko.co/api/v1/docs).

## Type Support

All types are auto-generated from the OpenAPI spec.

```python
from nadeshiko.models import (
    SearchRequest,
    SearchResponse,
    Sentence,
    MediaInfoData,
)

request: SearchRequest = {
    'query': '彼女',
    'limit': 10,
}

sentence: Sentence = {
    'basic_info': { # ... },
    'segment_info': { # ... },
    'media_info': { # ... },
}
```

## Examples

See `examples/usage.py` for more usage examples.

## References

- [Nadeshiko Website](https://nadeshiko.co)
- [API Documentation](https://nadeshiko.co/settings/api)
