# Nadeshiko SDK

Python SDK for the [Nadeshiko API](https://nadeshiko.co). Full API reference at [nadeshiko.co/docs/api](https://nadeshiko.co/docs/api/index.html).

## Install

```bash
pip install nadeshiko-sdk
```

## Quick start

```python
from nadeshiko import Nadeshiko
from nadeshiko.models import SearchQuery

client = Nadeshiko(
    api_key=os.environ["NADESHIKO_API_KEY"],
)

data = client.search(query=SearchQuery(search="彼女"))
print(data.segments)
# [
#   Segment(
#     segment_public_id="xK9mP2nQwR4t",
#     media_public_id="steins-gate",
#     episode=1,
#     start_time_ms=62340,
#     end_time_ms=65180,
#     text_ja=SegmentTextJa(content="彼女に会いたい", ...),
#     text_en=SegmentTextEn(content="I want to see her", ...),
#     urls=SegmentUrls(
#       image_url="https://...",
#       audio_url="https://...",
#       video_url="https://...",
#     ),
#   ),
#   # ...
# ]
```

Methods return data directly and accept model objects — pass `SearchQuery`, `SearchFilters`, and other model instances directly.

## Authentication

Pass your API key to `Nadeshiko`. It is sent as `Authorization: Bearer <api_key>` on every request.

```python
client = Nadeshiko(
    api_key=os.environ["NADESHIKO_API_KEY"],
    base_url="PRODUCTION",  # "LOCAL" | "DEVELOPMENT" | "PRODUCTION" | custom URL
    headers={"User-Agent": "MyApp/1.0"},
)
```

## Model objects

All methods accept model objects — body fields are passed as `SearchQuery`, `SearchFilters`, and other model instances:

```python
from nadeshiko.models import SearchQuery, SearchFilters, ContentRating

# POST endpoints — body models
result = client.search(
    query=SearchQuery(search="猫"),
    filters=SearchFilters(content_rating=[ContentRating.SAFE]),
)

# GET with query params — as keyword arguments
media_list = client.list_media(query="naruto", category="ANIME")

# GET with path params — as keyword arguments or positional
collection = client.get_collection("collection-public-id")
episode = client.get_episode(media_public_id="abc", episode_number=5)
```

Single-path-param endpoints also accept the ID as a plain string:

```python
media = client.get_media("some-public-id")
segment = client.get_segment("some-uuid")
context = client.get_segment_context("some-uuid")
```

## Available endpoints

### Search
| Method | Description |
|---|---|
| `search(params?)` | Search segments by query, with filters and sorting |
| `get_search_stats(params?)` | Category counts and media list for filter UI |
| `search_words(params)` | Look up multiple words and get match counts per media |
| `search_media(params)` | Find media by name (autocomplete) |

### Stats
| Method | Description |
|---|---|
| `get_stats_overview()` | Corpus-wide stats: segment count, media count, coverage tiers |

### Media
| Method | Description |
|---|---|
| `list_media(params?)` | Browse the media catalog |
| `get_media(id)` | Get a single media entry by public ID |
| `list_episodes(params)` | List episodes for a media entry |
| `get_episode(params)` | Get a single episode |
| `get_segment(id)` | Get a single segment by UUID |
| `get_segment_context(id)` | Get segments surrounding a given segment |

### User
| Method | Description |
|---|---|
| `get_me()` | Current user profile and API quota |
| `list_user_activity(params?)` | Activity history (searches, plays, exports) |
| `get_user_activity_heatmap(params?)` | Daily activity counts for a heatmap |
| `get_user_activity_stats(params?)` | Aggregate stats over a date range |
| `list_excluded_media()` | Media hidden from search results |
| `add_excluded_media(params)` | Hide a media entry from search results |
| `remove_excluded_media(id)` | Un-hide a media entry |

### Collections
| Method | Description |
|---|---|
| `list_collections(params?)` | List your saved collections |
| `create_collection(params)` | Create a new collection |
| `get_collection(id)` | Get a collection and its segments |
| `delete_collection(id)` | Delete a collection |
| `add_segment_to_collection(params)` | Add a segment to a collection |
| `search_collection_segments(params)` | Search within a collection |
| `remove_segment_from_collection(params)` | Remove a segment from a collection |

## Error handling

Errors throw a `NadeshikoError`. A proper `Exception` subclass with all RFC 7807 Problem Details fields.

```python
from nadeshiko import NadeshikoError
from nadeshiko.models import SearchQuery

try:
    data = client.search(query=SearchQuery(search="食べる"))
    print(data.segments)
except NadeshikoError as err:
    match err.code:
        case "VALIDATION_FAILED":
            print("Validation failed:", err.detail)
            for field, msg in (err.errors or {}).items():
                print(f"  {field}: {msg}")
        case "AUTH_CREDENTIALS_REQUIRED" | "AUTH_CREDENTIALS_INVALID":
            print("Authentication failed:", err.detail)
        case "RATE_LIMIT_EXCEEDED":
            print("Rate limited - slow down")
        case "QUOTA_EXCEEDED":
            print("Monthly quota exhausted")
        case "INTERNAL_SERVER_EXCEPTION":
            print("Server error, trace ID:", err.trace_id)
```

**`NadeshikoError` fields:**

| Field | Type | Description |
|---|---|---|
| `code` | `str` | Machine-readable error code |
| `title` | `str` | Short summary |
| `detail` | `str` | Human-readable explanation |
| `status` | `int` | HTTP status code |
| `trace_id` | `str \| None` | Trace ID - include when reporting issues |
| `errors` | `dict[str, object] \| None` | Per-field messages (`VALIDATION_FAILED` only) |

### Opt out of throwing per-call

Pass `throw_on_error=False` to get a response object instead of throwing:

```python
from nadeshiko.models import SearchQuery

result = client.search(
    throw_on_error=False,
    query=SearchQuery(search="猫"),
)

if result.error is not None:
    print(result.error)
else:
    print(result.data.segments)
```

## Retry and timeout

The client retries automatically on network errors and `408 / 429 / 500 / 502 / 503 / 504` responses. `429` responses with a `Retry-After` header are respected.

```python
from nadeshiko import Nadeshiko, RetryOptions

client = Nadeshiko(
    api_key=os.environ["NADESHIKO_API_KEY"],
    retry_options=RetryOptions(
        max_retries=3,   # default: 2
        initial_delay=1, # default: 0.5 - doubles with each attempt
        max_delay=30,    # default: 30
        timeout=10,      # per-attempt timeout in seconds (default: none)
    ),
)
```

## Pagination

Paginated endpoints have an `iter_*` method that returns an iterator over individual items:

```python
from nadeshiko.models import SearchQuery

for segment in client.iter_search(
    query=SearchQuery(search="猫"),
):
    print(segment.text_ja.content)

for media in client.iter_list_media():
    print(media.name_en)
```

For manual page-by-page control, use the `cursor` field:

```python
from nadeshiko.models import SearchQuery

cursor: str | None = None

while True:
    data = client.search(
        query=SearchQuery(search="犬"),
        take=10,
        cursor=cursor,
    )

    for segment in data.segments:
        print(segment.text_ja.content)

    if not data.pagination.has_more or data.pagination.cursor is None:
        break

    cursor = data.pagination.cursor
```

See [`examples/examples.py`](examples/examples.py) for more usage patterns.
