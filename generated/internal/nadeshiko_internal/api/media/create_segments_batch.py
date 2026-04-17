from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_segments_batch_response_201 import CreateSegmentsBatchResponse201
from ...models.error_400 import Error400
from ...models.error_401 import Error401
from ...models.error_403 import Error403
from ...models.error_404 import Error404
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...models.segment_batch_create_request import SegmentBatchCreateRequest
from ...types import Response


def _get_kwargs(
    media_public_id: str,
    episode_number: int,
    *,
    body: SegmentBatchCreateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/media/{media_public_id}/episodes/{episode_number}/segments/batch".format(
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
) -> (
    CreateSegmentsBatchResponse201
    | Error400
    | Error401
    | Error403
    | Error404
    | Error429
    | Error500
    | None
):
    if response.status_code == 201:
        response_201 = CreateSegmentsBatchResponse201.from_dict(response.json())

        return response_201

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
    CreateSegmentsBatchResponse201 | Error400 | Error401 | Error403 | Error404 | Error429 | Error500
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
    body: SegmentBatchCreateRequest,
) -> Response[
    CreateSegmentsBatchResponse201 | Error400 | Error401 | Error403 | Error404 | Error429 | Error500
]:
    """Batch create segments

     Creates multiple segments for a specific episode in a single request.
    Duplicate segments are silently skipped.

    Args:
        media_public_id (str):
        episode_number (int):
        body (SegmentBatchCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSegmentsBatchResponse201 | Error400 | Error401 | Error403 | Error404 | Error429 | Error500]
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
    body: SegmentBatchCreateRequest,
) -> (
    CreateSegmentsBatchResponse201
    | Error400
    | Error401
    | Error403
    | Error404
    | Error429
    | Error500
    | None
):
    """Batch create segments

     Creates multiple segments for a specific episode in a single request.
    Duplicate segments are silently skipped.

    Args:
        media_public_id (str):
        episode_number (int):
        body (SegmentBatchCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateSegmentsBatchResponse201 | Error400 | Error401 | Error403 | Error404 | Error429 | Error500
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
    body: SegmentBatchCreateRequest,
) -> Response[
    CreateSegmentsBatchResponse201 | Error400 | Error401 | Error403 | Error404 | Error429 | Error500
]:
    """Batch create segments

     Creates multiple segments for a specific episode in a single request.
    Duplicate segments are silently skipped.

    Args:
        media_public_id (str):
        episode_number (int):
        body (SegmentBatchCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSegmentsBatchResponse201 | Error400 | Error401 | Error403 | Error404 | Error429 | Error500]
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
    body: SegmentBatchCreateRequest,
) -> (
    CreateSegmentsBatchResponse201
    | Error400
    | Error401
    | Error403
    | Error404
    | Error429
    | Error500
    | None
):
    """Batch create segments

     Creates multiple segments for a specific episode in a single request.
    Duplicate segments are silently skipped.

    Args:
        media_public_id (str):
        episode_number (int):
        body (SegmentBatchCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateSegmentsBatchResponse201 | Error400 | Error401 | Error403 | Error404 | Error429 | Error500
    """

    return (
        await asyncio_detailed(
            media_public_id=media_public_id,
            episode_number=episode_number,
            client=client,
            body=body,
        )
    ).parsed
