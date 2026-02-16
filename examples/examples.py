"""
Nadeshiko SDK usage examples.

These snippets are for reference only — they are NOT meant to be executed
as-is. Copy the parts you need into your own project.
"""

from __future__ import annotations

import asyncio
import os

from nadeshiko import Nadeshiko
from nadeshiko.api.lists import list_index, list_show
from nadeshiko.api.media import media_index, media_show
from nadeshiko.api.search import fetch_media_info, fetch_sentence_context, search, search_multiple
from nadeshiko.models import (
    Category,
    Error,
    FetchSentenceContextRequest,
    SearchMultipleRequest,
    SearchRequest,
    SearchRequestContentSort,
    SearchRequestMediaItem,
)
from nadeshiko.types import UNSET

# ---------------------------------------------------------------------------
# Client setup
# ---------------------------------------------------------------------------

client = Nadeshiko(
    base_url=os.getenv("NADESHIKO_BASE_URL", "https://api.nadeshiko.co"),
    token=os.getenv("NADESHIKO_API_KEY", "your-api-key"),
)


# ---------------------------------------------------------------------------
# Basic search
# ---------------------------------------------------------------------------


def basic_search() -> None:
    result = search.sync(
        client=client,
        body=SearchRequest(query="食べる"),
    )

    if isinstance(result, Error):
        print(result.code, result.detail)
        return

    for sentence in result.sentences or []:
        print(sentence.segment_info.content_jp)
        print(sentence.segment_info.content_en)
        print(sentence.basic_info.name_anime_en, f"EP {sentence.basic_info.episode}")
        print("---")


# ---------------------------------------------------------------------------
# Search with filters
# ---------------------------------------------------------------------------


def filtered_search() -> None:
    result = search.sync(
        client=client,
        body=SearchRequest(
            query="おはよう",
            category=[Category.ANIME],
            limit=5,
            content_sort=SearchRequestContentSort.ASC,  # shortest sentences first
            min_length=3,
            max_length=30,
            exact_match=True,  # exact phrase matching
            excluded_anime_ids=[42, 99],  # exclude specific media
        ),
    )

    if isinstance(result, Error):
        return

    print(f"Found {len(result.sentences or [])} results")

    for sentence in result.sentences or []:
        print(sentence.segment_info.content_jp)

        # Highlighted version (search terms wrapped in <em>)
        if sentence.segment_info.content_jp_highlight is not UNSET:
            print("Highlight:", sentence.segment_info.content_jp_highlight)


# ---------------------------------------------------------------------------
# Paginated search with cursor
# ---------------------------------------------------------------------------


def paginated_search() -> None:
    cursor = UNSET
    page = 0

    while True:
        result = search.sync(
            client=client,
            body=SearchRequest(
                query="猫",
                limit=10,
                cursor=cursor,
            ),
        )

        if isinstance(result, Error):
            print(result.detail)
            break

        page += 1
        print(f"Page {page}:")
        for sentence in result.sentences or []:
            print(f" - {sentence.segment_info.content_jp}")

        if isinstance(result.cursor, list):
            cursor = result.cursor
        else:
            break


# ---------------------------------------------------------------------------
# Search filtered to specific media + episodes
# ---------------------------------------------------------------------------


def media_filtered_search() -> None:
    result = search.sync(
        client=client,
        body=SearchRequest(
            query="ありがとう",
            media=[
                SearchRequestMediaItem.from_dict({"media_id": 123, "episodes": [1, 2, 3]}),
                SearchRequestMediaItem.from_dict({"media_id": 456, "episodes": [5]}),
            ],
        ),
    )

    if isinstance(result, Error):
        return
    print(len(result.sentences or []), "results")


# ---------------------------------------------------------------------------
# Search multiple words at once
# ---------------------------------------------------------------------------


def multi_word_search() -> None:
    result = search_multiple.sync(
        client=client,
        body=SearchMultipleRequest(
            words=["猫", "犬", "鳥"],
            exact_match=True,
        ),
    )

    if isinstance(result, Error):
        return

    for match in result.results or []:
        print(f"{match.word}: {match.total_matches} total matches, found in {len(match.media or [])} media")

        for m in match.media or []:
            print(f"  {m.name_anime_en} — {m.match_count} hits")


# ---------------------------------------------------------------------------
# Get search filter stats (for building UI filters)
# ---------------------------------------------------------------------------


def search_stats() -> None:
    result = search.sync(
        client=client,
        body=SearchRequest(
            query="学校",
            category=[Category.ANIME],
        ),
    )

    if isinstance(result, Error):
        return

    # Category tab counts
    for cat in result.category_statistics or []:
        print(f"{cat.category}: {cat.count} hits")

    # Per-media breakdown
    for media in result.statistics or []:
        print(f"{media.name_anime_en}: {media.segment_count} segments")


# ---------------------------------------------------------------------------
# Get surrounding context for a segment
# ---------------------------------------------------------------------------


def segment_context() -> None:
    result = fetch_sentence_context.sync(
        client=client,
        body=FetchSentenceContextRequest(
            media_id=123,
            season=1,
            episode=1,
            segment_position=42,
            limit=3,  # 3 segments before + after
        ),
    )

    if isinstance(result, Error):
        return

    for sentence in result.sentences:
        print(f"[{sentence.segment_info.start_time}] {sentence.segment_info.content_jp}")


# ---------------------------------------------------------------------------
# Browse media catalog
# ---------------------------------------------------------------------------


def browse_media_catalog() -> None:
    result = fetch_media_info.sync(
        client=client,
        query="naruto",
        type_="anime",
        size=20,
        cursor=0,
    )

    if isinstance(result, Error):
        return

    for media in result.data or []:
        print(f"[{media.id}] {media.name_anime_en}")


# ---------------------------------------------------------------------------
# List all media (paginated)
# ---------------------------------------------------------------------------


def list_all_media() -> None:
    result = media_index.sync(
        client=client,
        limit=20,
        cursor=0,
    )

    if isinstance(result, Error):
        return

    for media in result.media or []:
        print(f"[{media.id}] {media.english_name} ({media.airing_status})")
        print(f"  Genres: {', '.join(media.genres or [])}")
        print(f"  Episodes: {media.episode_count}")


# ---------------------------------------------------------------------------
# Get a single media's details
# ---------------------------------------------------------------------------


def get_media_details() -> None:
    result = media_show.sync(
        123,
        client=client,
    )

    if isinstance(result, Error):
        if result.status == 404:
            print("Media not found")
        return

    print(result.english_name, result.japanese_name)
    print(f"Category: {result.category}")
    print(f"Episodes: {result.episode_count}")
    print(f"Segments: {result.segment_count}")


# ---------------------------------------------------------------------------
# Working with lists
# ---------------------------------------------------------------------------


def list_examples() -> None:
    # Fetch all public lists
    lists = list_index.sync(
        client=client,
        visibility="public",
        type_="SERIES",
    )

    if isinstance(lists, Error):
        return

    for lst in lists or []:
        print(f"[{lst.id}] {lst.name} — {lst.segment_count} segments")

    # Get a single list with its media
    detail = list_show.sync(
        1,
        client=client,
    )

    if isinstance(detail, Error):
        return

    print(f"List: {detail.name}")
    for media_item in detail.media or []:
        print(f"  {media_item.name_anime_en}")


# ---------------------------------------------------------------------------
# Error handling patterns
# ---------------------------------------------------------------------------


def error_handling_exhaustive() -> None:
    result = search.sync(
        client=client,
        body=SearchRequest(query="test"),
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
        return

    print(result)


# ---------------------------------------------------------------------------
# Async usage
# ---------------------------------------------------------------------------


async def async_search() -> None:
    result = await search.asyncio(
        client=client,
        body=SearchRequest(query="彼女"),
    )

    if isinstance(result, Error):
        print(result.code, result.detail)
        return

    for sentence in result.sentences or []:
        print(sentence.segment_info.content_jp)


# ---------------------------------------------------------------------------
# Accessing media URLs (images, audio, video)
# ---------------------------------------------------------------------------


def media_urls() -> None:
    result = search.sync(
        client=client,
        body=SearchRequest(query="桜"),
    )

    if isinstance(result, Error):
        return

    for sentence in result.sentences or []:
        if sentence.media_info.path_image is not UNSET:
            print("Image:", sentence.media_info.path_image)
        if sentence.media_info.path_audio is not UNSET:
            print("Audio:", sentence.media_info.path_audio)
        if sentence.media_info.path_video is not UNSET:
            print("Video:", sentence.media_info.path_video)
