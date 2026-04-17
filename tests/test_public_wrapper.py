from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path

import httpx
import pytest

PACKAGE_DIR = Path(__file__).resolve().parents[1] / "generated" / "public" / "nadeshiko"

sys.path.insert(0, str(PACKAGE_DIR.parent))

from nadeshiko import AsyncNadeshiko, Nadeshiko, NadeshikoError, RetryOptions  # noqa: E402
from nadeshiko.models import (  # noqa: E402
    ContentRating,
    MediaFilterItem,
    SearchFilters,
    SearchFiltersMedia,
    SearchFiltersSegmentLengthChars,
    SearchQuery,
    SearchSort,
    SearchSortMode,
)


def request_json(request: httpx.Request) -> dict:
    return json.loads(request.content.decode("utf-8"))


def media_payload(public_id: str = "test-media", name_en: str = "Test Media") -> dict:
    return {
        "mediaPublicId": public_id,
        "slug": public_id,
        "externalIds": {"anilist": None, "imdb": None, "tvdb": None, "tmdb": None},
        "nameJa": "テスト",
        "nameRomaji": "Tesuto",
        "nameEn": name_en,
        "airingFormat": "TV",
        "airingStatus": "FINISHED",
        "genres": ["Drama"],
        "coverUrl": "https://cdn.example.com/cover.jpg",
        "bannerUrl": "https://cdn.example.com/banner.jpg",
        "startDate": "2024-01-01",
        "endDate": None,
        "category": "ANIME",
        "segmentCount": 100,
        "episodeCount": 12,
        "studio": None,
        "seasonName": "WINTER",
        "seasonYear": 2024,
    }


def episode_payload(media_public_id: str = "test-media", episode_number: int = 5) -> dict:
    return {
        "mediaPublicId": media_public_id,
        "episodeNumber": episode_number,
        "titleEn": "Episode 5",
        "titleRomaji": None,
        "titleJa": None,
        "description": None,
        "airedAt": None,
        "lengthSeconds": None,
        "thumbnailUrl": None,
        "segmentCount": 42,
    }


def segment_payload(segment_public_id: str, content: str) -> dict:
    return {
        "segmentPublicId": segment_public_id,
        "position": 1,
        "status": "ACTIVE",
        "startTimeMs": 0,
        "endTimeMs": 1000,
        "contentRating": "SAFE",
        "episode": 1,
        "mediaPublicId": "media-1",
        "textJa": {"content": content, "highlight": None, "tokens": None},
        "textEn": {
            "content": "translated",
            "isMachineTranslated": False,
            "highlight": None,
        },
        "textEs": {
            "content": "traducido",
            "isMachineTranslated": False,
            "highlight": None,
        },
        "urls": {
            "imageUrl": "https://cdn.example.com/image.jpg",
            "audioUrl": "https://cdn.example.com/audio.mp3",
            "videoUrl": "https://cdn.example.com/video.mp4",
        },
    }


def make_client(handler, **kwargs):
    transport = httpx.MockTransport(handler)
    return Nadeshiko(
        api_key="test-key",
        base_url="http://testserver",
        retry_options=RetryOptions(max_retries=kwargs.pop("max_retries", 0), initial_delay=0),
        httpx_args={"transport": transport},
        **kwargs,
    )


def make_async_client(handler, **kwargs):
    transport = httpx.MockTransport(handler)
    return AsyncNadeshiko(
        api_key="test-key",
        base_url="http://testserver",
        retry_options=RetryOptions(max_retries=kwargs.pop("max_retries", 0), initial_delay=0),
        httpx_args={"transport": transport},
        **kwargs,
    )


def test_search_accepts_model_objects_and_returns_data() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/v1/search"
        assert request.method == "POST"
        assert request_json(request)["query"]["search"] == "猫"
        return httpx.Response(
            200,
            json={
                "segments": [segment_payload("segment-1", "猫です")],
                "pagination": {"hasMore": False, "cursor": None, "estimatedTotalHits": 1, "estimatedTotalHitsRelation": "EXACT"},
            },
        )

    client = make_client(handler)
    data = client.search(query=SearchQuery(search="猫"))

    assert data.segments[0].text_ja.content == "猫です"


def test_public_package_only_exposes_model_object_type_surface() -> None:
    assert not (PACKAGE_DIR / "inputs.py").exists()
    sdk_stub = (PACKAGE_DIR / "sdk.pyi").read_text(encoding="utf-8")
    assert "from .inputs import" not in sdk_stub
    assert "SearchQueryInput" not in sdk_stub
    assert "SearchFiltersInput" not in sdk_stub


def test_search_accepts_nested_request_models() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        body = request_json(request)
        assert body["query"] == {"search": "おはよう", "exactMatch": True}
        assert body["sort"] == {"mode": "ASC"}
        assert body["filters"] == {
            "contentRating": ["SAFE"],
            "segmentLengthChars": {"min": 3, "max": 30},
            "media": {
                "include": [{"mediaPublicId": "abc", "episodes": [1, 2, 3]}],
            },
        }
        return httpx.Response(
            200,
            json={
                "segments": [segment_payload("segment-1", "おはよう")],
                "pagination": {"hasMore": False, "cursor": None, "estimatedTotalHits": 1, "estimatedTotalHitsRelation": "EXACT"},
            },
        )

    client = make_client(handler)
    data = client.search(
        query=SearchQuery(search="おはよう", exact_match=True),
        sort=SearchSort(mode=SearchSortMode.ASC),
        filters=SearchFilters(
            content_rating=[ContentRating.SAFE],
            segment_length_chars=SearchFiltersSegmentLengthChars(min_=3, max_=30),
            media=SearchFiltersMedia(
                include=[MediaFilterItem(media_public_id="abc", episodes=[1, 2, 3])]
            ),
        ),
    )

    assert data.segments[0].text_ja.content == "おはよう"


def test_body_only_endpoint_accepts_model_objects() -> None:
    from nadeshiko.models import AddExcludedMediaBody

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/v1/user/excluded-media"
        assert request_json(request) == {"mediaPublicId": "some-public-id"}
        return httpx.Response(
            204,
        )

    client = make_client(handler)
    client.add_excluded_media(AddExcludedMediaBody(media_public_id="some-public-id"))


def test_string_and_positional_path_params_work() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/v1/media/test-media":
            return httpx.Response(200, json=media_payload())
        if request.url.path == "/v1/media/test-media/episodes/5":
            return httpx.Response(200, json=episode_payload())
        raise AssertionError(f"unexpected path: {request.url.path}")

    client = make_client(handler)

    media = client.get_media("test-media")
    episode = client.get_episode("test-media", 5)

    assert media.media_public_id == "test-media"
    assert episode.episode_number == 5


def test_throw_on_error_false_returns_sdk_response() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            429,
            json={
                "code": "RATE_LIMIT_EXCEEDED",
                "title": "Too Many Requests",
                "detail": "Slow down",
                "status": 429,
                "instance": "trace-123",
            },
        )

    client = make_client(handler)
    result = client.search(query=SearchQuery(search="猫"), throw_on_error=False)

    assert result.data is None
    assert result.error is not None
    assert result.error.code == "RATE_LIMIT_EXCEEDED"
    assert result.error.trace_id == "trace-123"


def test_non_2xx_raises_nadeshiko_error_by_default() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            404,
            json={
                "code": "NOT_FOUND",
                "title": "Not Found",
                "detail": "Missing media",
                "status": 404,
            },
        )

    client = make_client(handler)

    with pytest.raises(NadeshikoError) as exc_info:
        client.get_media("missing")

    assert exc_info.value.code == "NOT_FOUND"
    assert exc_info.value.status == 404


def test_iter_search_paginates_using_cursor() -> None:
    seen_bodies: list[dict] = []

    def handler(request: httpx.Request) -> httpx.Response:
        body = request_json(request)
        seen_bodies.append(body)
        if body.get("cursor") == "cursor-2":
            return httpx.Response(
                200,
                json={
                    "segments": [segment_payload("segment-2", "page2")],
                    "pagination": {"hasMore": False, "cursor": None, "estimatedTotalHits": 2, "estimatedTotalHitsRelation": "EXACT"},
                },
            )

        return httpx.Response(
            200,
            json={
                "segments": [segment_payload("segment-1", "page1")],
                "pagination": {"hasMore": True, "cursor": "cursor-2", "estimatedTotalHits": 2, "estimatedTotalHitsRelation": "EXACT"},
            },
        )

    client = make_client(handler)
    items = list(client.iter_search(query=SearchQuery(search="猫")))

    assert [item.text_ja.content for item in items] == ["page1", "page2"]
    assert seen_bodies[0]["query"]["search"] == "猫"
    assert seen_bodies[1]["cursor"] == "cursor-2"


def test_retry_retries_retryable_responses() -> None:
    attempts = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            return httpx.Response(
                429,
                headers={"Retry-After": "0"},
                json={
                    "code": "RATE_LIMIT_EXCEEDED",
                    "title": "Too Many Requests",
                    "detail": "Slow down",
                    "status": 429,
                },
            )
        return httpx.Response(
            200,
            json={
                "media": [],
                "pagination": {"hasMore": False, "cursor": None},
                "stats": {"totalMedia": 0, "totalSegments": 0, "totalEpisodes": 0},
            },
        )

    client = make_client(handler, max_retries=1)
    data = client.list_media()

    assert attempts == 2
    assert data.media == []


def test_user_agent_header_defaults_and_can_be_overridden() -> None:
    headers_seen: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        headers_seen.append(request.headers["user-agent"])
        return httpx.Response(
            200,
            json={"categories": [], "media": []},
        )

    default_client = make_client(handler)
    default_client.get_search_stats(query=SearchQuery(search="test"))

    custom_client = make_client(handler, headers={"User-Agent": "MyApp/1.0"})
    custom_client.get_search_stats(query=SearchQuery(search="test"))

    assert headers_seen[0].startswith("nadeshiko-sdk-python/")
    assert headers_seen[1] == "MyApp/1.0"


def test_async_client_works() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            json={
                "media": [media_payload(public_id="media-1", name_en="Async Media")],
                "pagination": {"hasMore": False, "cursor": None},
                "stats": {"totalMedia": 1, "totalSegments": 100, "totalEpisodes": 12},
            },
        )

    async def run() -> None:
        client = make_async_client(handler)
        data = await client.list_media()
        assert data.media[0].name_en == "Async Media"

    asyncio.run(run())
