from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.affected_count_response import AffectedCountResponse
from ...models.error_400 import Error400
from ...models.error_401 import Error401
from ...models.error_403 import Error403
from ...models.error_404 import Error404
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...models.moderate_episode_segments_request import ModerateEpisodeSegmentsRequest
from ...types import Response


def _get_kwargs(
    media_public_id: str,
    episode_number: int,
    *,
    body: ModerateEpisodeSegmentsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/media/{media_public_id}/episodes/{episode_number}/segments/moderate".format(
            media_public_id=quote(str(media_public_id), safe=""),
            episode_number=quote(str(episode_number), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AffectedCountResponse | Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | None:
    if response.status_code == 200:
        response_200 = AffectedCountResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Error404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = Error429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = Error500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AffectedCountResponse | Error400 | Error401 | Error403 | Error404 | Error429 | Error500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    media_public_id: str,
    episode_number: int,
    *,
    client: AuthenticatedClient,
    body: ModerateEpisodeSegmentsRequest,
) -> Response[
    AffectedCountResponse | Error400 | Error401 | Error403 | Error404 | Error429 | Error500
]:
    """Apply a moderation action to every segment in an episode

     Applies one action across a whole episode. This exists for defects that are
    properties of the episode rather than of any single line — a subtitle file
    offset against the audio, or a bad rip that makes every clip unusable.

    Two actions are supported:

    - `shiftTimings` moves every segment's start and end by `offsetMs`, which may
      be negative. Segments whose start would go below zero are clamped to zero
      rather than skipped, so the episode stays contiguous.
    - `setStatus` sets every segment's status, which is how an episode is hidden
      from search without deleting anything.

    Every affected segment gets its own revision, so this is revertible one segment
    at a time through the restore endpoint, and shows up per segment in the agent
    activity feed.

    **Bounded by `maxAffected`.** If the episode has more segments than that, the
    request is rejected with 400 and nothing is written — no partial application.
    The cap is what keeps an automated caller's mistake to a size a person can
    review, so callers are expected to set it deliberately rather than to the
    largest value they can.

    Args:
        media_public_id (str):
        episode_number (int):
        body (ModerateEpisodeSegmentsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AffectedCountResponse | Error400 | Error401 | Error403 | Error404 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        media_public_id=media_public_id,
        episode_number=episode_number,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    media_public_id: str,
    episode_number: int,
    *,
    client: AuthenticatedClient,
    body: ModerateEpisodeSegmentsRequest,
) -> AffectedCountResponse | Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | None:
    """Apply a moderation action to every segment in an episode

     Applies one action across a whole episode. This exists for defects that are
    properties of the episode rather than of any single line — a subtitle file
    offset against the audio, or a bad rip that makes every clip unusable.

    Two actions are supported:

    - `shiftTimings` moves every segment's start and end by `offsetMs`, which may
      be negative. Segments whose start would go below zero are clamped to zero
      rather than skipped, so the episode stays contiguous.
    - `setStatus` sets every segment's status, which is how an episode is hidden
      from search without deleting anything.

    Every affected segment gets its own revision, so this is revertible one segment
    at a time through the restore endpoint, and shows up per segment in the agent
    activity feed.

    **Bounded by `maxAffected`.** If the episode has more segments than that, the
    request is rejected with 400 and nothing is written — no partial application.
    The cap is what keeps an automated caller's mistake to a size a person can
    review, so callers are expected to set it deliberately rather than to the
    largest value they can.

    Args:
        media_public_id (str):
        episode_number (int):
        body (ModerateEpisodeSegmentsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AffectedCountResponse | Error400 | Error401 | Error403 | Error404 | Error429 | Error500
    """

    return sync_detailed(
        media_public_id=media_public_id,
        episode_number=episode_number,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    media_public_id: str,
    episode_number: int,
    *,
    client: AuthenticatedClient,
    body: ModerateEpisodeSegmentsRequest,
) -> Response[
    AffectedCountResponse | Error400 | Error401 | Error403 | Error404 | Error429 | Error500
]:
    """Apply a moderation action to every segment in an episode

     Applies one action across a whole episode. This exists for defects that are
    properties of the episode rather than of any single line — a subtitle file
    offset against the audio, or a bad rip that makes every clip unusable.

    Two actions are supported:

    - `shiftTimings` moves every segment's start and end by `offsetMs`, which may
      be negative. Segments whose start would go below zero are clamped to zero
      rather than skipped, so the episode stays contiguous.
    - `setStatus` sets every segment's status, which is how an episode is hidden
      from search without deleting anything.

    Every affected segment gets its own revision, so this is revertible one segment
    at a time through the restore endpoint, and shows up per segment in the agent
    activity feed.

    **Bounded by `maxAffected`.** If the episode has more segments than that, the
    request is rejected with 400 and nothing is written — no partial application.
    The cap is what keeps an automated caller's mistake to a size a person can
    review, so callers are expected to set it deliberately rather than to the
    largest value they can.

    Args:
        media_public_id (str):
        episode_number (int):
        body (ModerateEpisodeSegmentsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AffectedCountResponse | Error400 | Error401 | Error403 | Error404 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        media_public_id=media_public_id,
        episode_number=episode_number,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    media_public_id: str,
    episode_number: int,
    *,
    client: AuthenticatedClient,
    body: ModerateEpisodeSegmentsRequest,
) -> AffectedCountResponse | Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | None:
    """Apply a moderation action to every segment in an episode

     Applies one action across a whole episode. This exists for defects that are
    properties of the episode rather than of any single line — a subtitle file
    offset against the audio, or a bad rip that makes every clip unusable.

    Two actions are supported:

    - `shiftTimings` moves every segment's start and end by `offsetMs`, which may
      be negative. Segments whose start would go below zero are clamped to zero
      rather than skipped, so the episode stays contiguous.
    - `setStatus` sets every segment's status, which is how an episode is hidden
      from search without deleting anything.

    Every affected segment gets its own revision, so this is revertible one segment
    at a time through the restore endpoint, and shows up per segment in the agent
    activity feed.

    **Bounded by `maxAffected`.** If the episode has more segments than that, the
    request is rejected with 400 and nothing is written — no partial application.
    The cap is what keeps an automated caller's mistake to a size a person can
    review, so callers are expected to set it deliberately rather than to the
    largest value they can.

    Args:
        media_public_id (str):
        episode_number (int):
        body (ModerateEpisodeSegmentsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AffectedCountResponse | Error400 | Error401 | Error403 | Error404 | Error429 | Error500
    """

    return (
        await asyncio_detailed(
            media_public_id=media_public_id,
            episode_number=episode_number,
            client=client,
            body=body,
        )
    ).parsed
