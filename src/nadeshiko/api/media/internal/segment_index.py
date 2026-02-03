from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from .... import errors
from ....client import AuthenticatedClient, Client
from ....models.error import Error
from ....models.segment_list_response import SegmentListResponse
from ....types import UNSET, Response, Unset


def _get_kwargs(
    media_id: int,
    episode_number: int,
    *,
    size: int | Unset = 50,
    cursor: int | Unset = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["size"] = size

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/media/{media_id}/episodes/{episode_number}/segments".format(
            media_id=quote(str(media_id), safe=""),
            episode_number=quote(str(episode_number), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | SegmentListResponse | None:
    if response.status_code == 200:
        response_200 = SegmentListResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | SegmentListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    media_id: int,
    episode_number: int,
    *,
    client: AuthenticatedClient,
    size: int | Unset = 50,
    cursor: int | Unset = 0,
) -> Response[Error | SegmentListResponse]:
    """List segments for an episode

     Get a paginated list of segments for a specific episode

    Args:
        media_id (int):
        episode_number (int):
        size (int | Unset):  Default: 50.
        cursor (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SegmentListResponse]
    """

    kwargs = _get_kwargs(
        media_id=media_id,
        episode_number=episode_number,
        size=size,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    media_id: int,
    episode_number: int,
    *,
    client: AuthenticatedClient,
    size: int | Unset = 50,
    cursor: int | Unset = 0,
) -> Error | SegmentListResponse | None:
    """List segments for an episode

     Get a paginated list of segments for a specific episode

    Args:
        media_id (int):
        episode_number (int):
        size (int | Unset):  Default: 50.
        cursor (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SegmentListResponse
    """

    return sync_detailed(
        media_id=media_id,
        episode_number=episode_number,
        client=client,
        size=size,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    media_id: int,
    episode_number: int,
    *,
    client: AuthenticatedClient,
    size: int | Unset = 50,
    cursor: int | Unset = 0,
) -> Response[Error | SegmentListResponse]:
    """List segments for an episode

     Get a paginated list of segments for a specific episode

    Args:
        media_id (int):
        episode_number (int):
        size (int | Unset):  Default: 50.
        cursor (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SegmentListResponse]
    """

    kwargs = _get_kwargs(
        media_id=media_id,
        episode_number=episode_number,
        size=size,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    media_id: int,
    episode_number: int,
    *,
    client: AuthenticatedClient,
    size: int | Unset = 50,
    cursor: int | Unset = 0,
) -> Error | SegmentListResponse | None:
    """List segments for an episode

     Get a paginated list of segments for a specific episode

    Args:
        media_id (int):
        episode_number (int):
        size (int | Unset):  Default: 50.
        cursor (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SegmentListResponse
    """

    return (
        await asyncio_detailed(
            media_id=media_id,
            episode_number=episode_number,
            client=client,
            size=size,
            cursor=cursor,
        )
    ).parsed
