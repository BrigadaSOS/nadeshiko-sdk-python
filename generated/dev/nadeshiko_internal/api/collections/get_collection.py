from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.collection_with_segments import CollectionWithSegments
from ...models.error_400 import Error400
from ...models.error_401 import Error401
from ...models.error_403 import Error403
from ...models.error_404 import Error404
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    cursor: str | Unset = UNSET,
    page: int | Unset = 1,
    take: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["page"] = page

    params["take"] = take

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/collections/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CollectionWithSegments | Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | None
):
    if response.status_code == 200:
        response_200 = CollectionWithSegments.from_dict(response.json())

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
    CollectionWithSegments | Error400 | Error401 | Error403 | Error404 | Error429 | Error500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    page: int | Unset = 1,
    take: int | Unset = 20,
) -> Response[
    CollectionWithSegments | Error400 | Error401 | Error403 | Error404 | Error429 | Error500
]:
    """Get collection details

     Returns a collection with paginated segments and their search result data.

    Args:
        id (int):  Example: 123.
        cursor (str | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        take (int | Unset):  Default: 20. Example: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CollectionWithSegments | Error400 | Error401 | Error403 | Error404 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        id=id,
        cursor=cursor,
        page=page,
        take=take,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    page: int | Unset = 1,
    take: int | Unset = 20,
) -> (
    CollectionWithSegments | Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | None
):
    """Get collection details

     Returns a collection with paginated segments and their search result data.

    Args:
        id (int):  Example: 123.
        cursor (str | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        take (int | Unset):  Default: 20. Example: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CollectionWithSegments | Error400 | Error401 | Error403 | Error404 | Error429 | Error500
    """

    return sync_detailed(
        id=id,
        client=client,
        cursor=cursor,
        page=page,
        take=take,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    page: int | Unset = 1,
    take: int | Unset = 20,
) -> Response[
    CollectionWithSegments | Error400 | Error401 | Error403 | Error404 | Error429 | Error500
]:
    """Get collection details

     Returns a collection with paginated segments and their search result data.

    Args:
        id (int):  Example: 123.
        cursor (str | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        take (int | Unset):  Default: 20. Example: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CollectionWithSegments | Error400 | Error401 | Error403 | Error404 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        id=id,
        cursor=cursor,
        page=page,
        take=take,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    page: int | Unset = 1,
    take: int | Unset = 20,
) -> (
    CollectionWithSegments | Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | None
):
    """Get collection details

     Returns a collection with paginated segments and their search result data.

    Args:
        id (int):  Example: 123.
        cursor (str | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        take (int | Unset):  Default: 20. Example: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CollectionWithSegments | Error400 | Error401 | Error403 | Error404 | Error429 | Error500
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            cursor=cursor,
            page=page,
            take=take,
        )
    ).parsed
