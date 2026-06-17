"""
Nadeshiko SDK usage examples.

These snippets are for reference only - they are NOT meant to be executed
as-is. Copy the parts you need into your own project.
"""

from __future__ import annotations

import os

from nadeshiko import Nadeshiko, NadeshikoError, RetryOptions
from nadeshiko.models import (
    AddExcludedMediaBody,
    Category,
    CollectionCreateRequest,
    CollectionVisibility,
    ContentRating,
    MediaFilterItem,
    SearchFilters,
    SearchFiltersMedia,
    SearchFiltersSegmentLengthChars,
    SearchMultipleQuery,
    SearchQuery,
    SearchSort,
    SearchSortMode,
)

# Client setup

client = Nadeshiko(
    api_key=os.environ["NADESHIKO_API_KEY"],
    base_url="PRODUCTION",  # "LOCAL" | "DEVELOPMENT" | "STAGING" | "PRODUCTION" | custom URL
)

# With retry + timeout + custom headers
client_with_retry = Nadeshiko(
    api_key=os.environ["NADESHIKO_API_KEY"],
    headers={"User-Agent": "MyApp/1.0"},
    retry_options=RetryOptions(
        max_retries=3,
        timeout=10,
    ),
)


# Basic search - model objects


def basic_search() -> None:
    data = client.search(
        query=SearchQuery(search="食べる"),
    )

    for segment in data.segments:
        print(segment.text_ja.content)
        print(segment.text_en.content)
        print(f"{segment.media_public_id} EP {segment.episode}")


# Search with filters

def filtered_search() -> None:
    data = client.search(
        query=SearchQuery(search="おはよう", exact_match=True),
        take=5,
        sort=SearchSort(mode=SearchSortMode.ASC),
        filters=SearchFilters(
            category=[Category.ANIME],
            content_rating=[ContentRating.SAFE],
            segment_length_chars=SearchFiltersSegmentLengthChars(min_=3, max_=30),
        ),
    )

    print(f"~{data.pagination.estimated_total_hits} results")

    for segment in data.segments:
        print(segment.text_ja.content)
        if segment.text_ja.highlight:
            print("Highlight:", segment.text_ja.highlight)

# Search filtered to specific media + episodes

def media_filtered_search() -> None:
    data = client.search(
        query=SearchQuery(search="ありがとう"),
        filters=SearchFilters(
            media=SearchFiltersMedia(
                include=[
                    MediaFilterItem(media_public_id="abc", episodes=[1, 2, 3]),
                    MediaFilterItem(media_public_id="xyz", episodes=[5]),
                ]
            )
        ),
    )

    print(len(data.segments), "results")


# Search multiple words at once

def multi_word_search() -> None:
    data = client.search_words(
        query=SearchMultipleQuery(words=["猫", "犬", "鳥"]),
    )

    for entry in data.results:
        print(f"{entry.word}: {entry.match_count} occurrences across {len(entry.media)} media")


# Find media by name (autocomplete-style search)

def find_media() -> None:
    data = client.search_media(
        query="steins",
        take=5,
    )

    for media in data.media:
        print(f"[{media.media_public_id}] {media.name_en}")


# Get corpus statistics overview (powers the /stats page)

def stats_overview() -> None:
    data = client.get_stats_overview()

    print(f"Total segments: {data.total_segments}")
    print(f"Total media: {data.total_media}")


# Get current user profile and quota

def current_user() -> None:
    data = client.get_me()

    print(f"User: {data.user.username} ({data.user.role})")
    print(f"Quota used: {data.quota.used} / {data.quota.limit}")

# Excluded media - hide media from search results


def excluded_media() -> None:
    # List currently excluded media
    listed = client.list_excluded_media()
    print(f"Excluding {len(listed.excluded_media)} media")

    # Exclude a media entry
    client.add_excluded_media(AddExcludedMediaBody(media_public_id="some-public-id"))

    # Re-include it
    client.remove_excluded_media("some-public-id")


# Get search filter stats

def search_stats() -> None:
    data = client.get_search_stats(
        query=SearchQuery(search="学校"),
        filters=SearchFilters(category=[Category.ANIME]),
    )

    for category in data.categories:
        print(f"{category.category}: {category.count} hits")

# Get a single media - string shorthand or keyword args


def get_media_details() -> None:
    # Shorthand: pass the ID directly
    data = client.get_media("some-public-id")

    # Equivalent keyword form:
    # data = client.get_media(media_public_id="some-public-id")

    print(data.name_en, data.name_ja)
    print(f"Episodes: {data.episode_count}, Segments: {data.segment_count}")


# Get segment context - string shorthand

def segment_context() -> None:
    data = client.get_segment_context("some-segment-uuid")

    for segment in data.segments:
        print(f"[{segment.start_time_ms}ms] {segment.text_ja.content}")

# Browse media catalog - query params as keyword args


def browse_media_catalog() -> None:
    data = client.list_media(
        query="naruto",
        category="ANIME",
        take=20,
    )

    for media in data.media:
        print(f"[{media.media_public_id}] {media.name_en} ({media.airing_status})")
        print(f"  Genres: {', '.join(media.genres)}")
        print(f"  Episodes: {media.episode_count}")


# Get episode - path params as keyword args

def get_episode_details() -> None:
    data = client.get_episode(
        media_public_id="some-media-id",
        episode_number=5,
    )

    print(data.title_en)


# Access media URLs

def media_urls() -> None:
    data = client.search(
        query=SearchQuery(search="桜"),
    )

    for segment in data.segments:
        print("Image:", segment.urls.image_url)
        print("Audio:", segment.urls.audio_url)
        print("Video:", segment.urls.video_url)


# Morpheme / token analysis

def morpheme_analysis() -> None:
    data = client.search(
        query=SearchQuery(search="彼女は毎日学校に行く"),
    )

    segment = data.segments[0]
    tokens = segment.text_ja.tokens
    if not tokens:
        return

    for token in tokens:
        print(f"{token.s} [{token.r}] - {token.p} (dict: {token.d})")


# Paginated search - built-in auto-pagination

def paginated_search() -> None:
    for segment in client.iter_search(
        query=SearchQuery(search="猫"),
        take=20,
    ):
        print(segment.text_ja.content)


# Browse all media with pagination

def paginated_media_browse() -> None:
    for media in client.iter_list_media(
        category="ANIME",
    ):
        print(media.name_en)


# Manual cursor pagination

def manual_pagination() -> None:
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


# Error handling

def error_handling() -> None:
    try:
        data = client.search(
            query=SearchQuery(search="test"),
        )
        print(len(data.segments), "results")
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
            case _:
                print(f"[{err.status}] {err.code}: {err.detail}")


# Opt out of throwing for a single call

def opt_out_of_throwing() -> None:
    result = client.search(
        throw_on_error=False,
        query=SearchQuery(search="猫"),
    )

    if result.error is not None:
        print("Search failed:", result.error)
    else:
        print(len(result.data.segments), "results")


# Collections


def collections() -> None:
    from nadeshiko.models import AddSegmentToCollectionRequest

    # Create a collection
    collection = client.create_collection(
        CollectionCreateRequest(name="Favorites", visibility=CollectionVisibility.PRIVATE)
    )
    print(f"Created: {collection.public_id}")

    # Add segment to collection
    client.add_segment_to_collection(
        collection.public_id,
        AddSegmentToCollectionRequest(segment_public_id="segment-uuid", note="Great line"),
    )

    # List collections
    collections = client.list_collections()
    for c in collections.collections:
        print(f"[{c.public_id}] {c.name} ({len(c.segments)} segments)")

    # Search within a collection
    results = client.search_collection_segments(
        collection.public_id,
        query=SearchQuery(search="ありがとう"),
    )
    for segment in results.segments:
        print(segment.text_ja.content)
