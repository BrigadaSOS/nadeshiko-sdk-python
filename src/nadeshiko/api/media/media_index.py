from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.media_index_category import MediaIndexCategory
from ...models.media_list_response import MediaListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 20,
    cursor: int | Unset = 0,
    category: MediaIndexCategory | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    json_category: str | Unset = UNSET
    if not isinstance(category, Unset):
        json_category = category.value

    params["category"] = json_category

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/media",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | MediaListResponse | None:
    if response.status_code == 200:
        response_200 = MediaListResponse.from_dict(response.json())

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
) -> Response[Error | MediaListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 20,
    cursor: int | Unset = 0,
    category: MediaIndexCategory | Unset = UNSET,
) -> Response[Error | MediaListResponse]:
    """List all media

     Returns a paginated list of media with full metadata, including cover/banner images, episode counts,
    and genres.

    Args:
        limit (int | Unset):  Default: 20.
        cursor (int | Unset):  Default: 0.
        category (MediaIndexCategory | Unset):  Example: ANIME.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MediaListResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        category=category,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 20,
    cursor: int | Unset = 0,
    category: MediaIndexCategory | Unset = UNSET,
) -> Error | MediaListResponse | None:
    """List all media

     Returns a paginated list of media with full metadata, including cover/banner images, episode counts,
    and genres.

    Args:
        limit (int | Unset):  Default: 20.
        cursor (int | Unset):  Default: 0.
        category (MediaIndexCategory | Unset):  Example: ANIME.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MediaListResponse
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        category=category,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 20,
    cursor: int | Unset = 0,
    category: MediaIndexCategory | Unset = UNSET,
) -> Response[Error | MediaListResponse]:
    """List all media

     Returns a paginated list of media with full metadata, including cover/banner images, episode counts,
    and genres.

    Args:
        limit (int | Unset):  Default: 20.
        cursor (int | Unset):  Default: 0.
        category (MediaIndexCategory | Unset):  Example: ANIME.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MediaListResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        category=category,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 20,
    cursor: int | Unset = 0,
    category: MediaIndexCategory | Unset = UNSET,
) -> Error | MediaListResponse | None:
    """List all media

     Returns a paginated list of media with full metadata, including cover/banner images, episode counts,
    and genres.

    Args:
        limit (int | Unset):  Default: 20.
        cursor (int | Unset):  Default: 0.
        category (MediaIndexCategory | Unset):  Example: ANIME.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MediaListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            category=category,
        )
    ).parsed
