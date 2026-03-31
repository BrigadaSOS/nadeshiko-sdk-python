from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400 import Error400
from ...models.error_401 import Error401
from ...models.error_403 import Error403
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...models.list_media_category import ListMediaCategory
from ...models.media_include_expansion import MediaIncludeExpansion
from ...models.media_list_response import MediaListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    take: int | Unset = 20,
    cursor: str | Unset = UNSET,
    category: ListMediaCategory | Unset = UNSET,
    query: str | Unset = UNSET,
    include: list[MediaIncludeExpansion] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["take"] = take

    params["cursor"] = cursor

    json_category: str | Unset = UNSET
    if not isinstance(category, Unset):
        json_category = category.value

    params["category"] = json_category

    params["query"] = query

    json_include: list[str] | Unset = UNSET
    if not isinstance(include, Unset):
        json_include = []
        for include_item_data in include:
            include_item = include_item_data.value
            json_include.append(include_item)

    params["include"] = json_include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/media",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error400 | Error401 | Error403 | Error429 | Error500 | MediaListResponse | None:
    if response.status_code == 200:
        response_200 = MediaListResponse.from_dict(response.json())

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
) -> Response[Error400 | Error401 | Error403 | Error429 | Error500 | MediaListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    take: int | Unset = 20,
    cursor: str | Unset = UNSET,
    category: ListMediaCategory | Unset = UNSET,
    query: str | Unset = UNSET,
    include: list[MediaIncludeExpansion] | Unset = UNSET,
) -> Response[Error400 | Error401 | Error403 | Error429 | Error500 | MediaListResponse]:
    """List all media

     Returns a paginated list of media with full metadata, including cover/banner images, episode counts,
    and genres.
    Supports filtering by category and text search.

    Args:
        take (int | Unset):  Default: 20.
        cursor (str | Unset):
        category (ListMediaCategory | Unset):  Example: ANIME.
        query (str | Unset):  Example: steins.
        include (list[MediaIncludeExpansion] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error429 | Error500 | MediaListResponse]
    """

    kwargs = _get_kwargs(
        take=take,
        cursor=cursor,
        category=category,
        query=query,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    take: int | Unset = 20,
    cursor: str | Unset = UNSET,
    category: ListMediaCategory | Unset = UNSET,
    query: str | Unset = UNSET,
    include: list[MediaIncludeExpansion] | Unset = UNSET,
) -> Error400 | Error401 | Error403 | Error429 | Error500 | MediaListResponse | None:
    """List all media

     Returns a paginated list of media with full metadata, including cover/banner images, episode counts,
    and genres.
    Supports filtering by category and text search.

    Args:
        take (int | Unset):  Default: 20.
        cursor (str | Unset):
        category (ListMediaCategory | Unset):  Example: ANIME.
        query (str | Unset):  Example: steins.
        include (list[MediaIncludeExpansion] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error403 | Error429 | Error500 | MediaListResponse
    """

    return sync_detailed(
        client=client,
        take=take,
        cursor=cursor,
        category=category,
        query=query,
        include=include,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    take: int | Unset = 20,
    cursor: str | Unset = UNSET,
    category: ListMediaCategory | Unset = UNSET,
    query: str | Unset = UNSET,
    include: list[MediaIncludeExpansion] | Unset = UNSET,
) -> Response[Error400 | Error401 | Error403 | Error429 | Error500 | MediaListResponse]:
    """List all media

     Returns a paginated list of media with full metadata, including cover/banner images, episode counts,
    and genres.
    Supports filtering by category and text search.

    Args:
        take (int | Unset):  Default: 20.
        cursor (str | Unset):
        category (ListMediaCategory | Unset):  Example: ANIME.
        query (str | Unset):  Example: steins.
        include (list[MediaIncludeExpansion] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error429 | Error500 | MediaListResponse]
    """

    kwargs = _get_kwargs(
        take=take,
        cursor=cursor,
        category=category,
        query=query,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    take: int | Unset = 20,
    cursor: str | Unset = UNSET,
    category: ListMediaCategory | Unset = UNSET,
    query: str | Unset = UNSET,
    include: list[MediaIncludeExpansion] | Unset = UNSET,
) -> Error400 | Error401 | Error403 | Error429 | Error500 | MediaListResponse | None:
    """List all media

     Returns a paginated list of media with full metadata, including cover/banner images, episode counts,
    and genres.
    Supports filtering by category and text search.

    Args:
        take (int | Unset):  Default: 20.
        cursor (str | Unset):
        category (ListMediaCategory | Unset):  Example: ANIME.
        query (str | Unset):  Example: steins.
        include (list[MediaIncludeExpansion] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error403 | Error429 | Error500 | MediaListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            take=take,
            cursor=cursor,
            category=category,
            query=query,
            include=include,
        )
    ).parsed
