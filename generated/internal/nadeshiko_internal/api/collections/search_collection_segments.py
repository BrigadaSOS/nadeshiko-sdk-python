from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400 import Error400
from ...models.error_401 import Error401
from ...models.error_403 import Error403
from ...models.error_404 import Error404
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...models.search_response import SearchResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    cursor: str | Unset = UNSET,
    take: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["take"] = take

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/collections/{id}/search".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SearchResponse | None:
    if response.status_code == 200:
        response_200 = SearchResponse.from_dict(response.json())

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
) -> Response[Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SearchResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    take: int | Unset = 20,
) -> Response[Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SearchResponse]:
    """Search collection segments

     Returns collection segments in search-response format with pagination.
    Reshapes the collection data: extracts segment results, includes media, computes pagination.

    Args:
        id (str):  Example: V1StGXR8_Z5d.
        cursor (str | Unset):  Example: eyJraW5kIjoib2Zmc2V0Iiwic2tpcCI6MjB9.
        take (int | Unset):  Default: 20. Example: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SearchResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        cursor=cursor,
        take=take,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    take: int | Unset = 20,
) -> Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SearchResponse | None:
    """Search collection segments

     Returns collection segments in search-response format with pagination.
    Reshapes the collection data: extracts segment results, includes media, computes pagination.

    Args:
        id (str):  Example: V1StGXR8_Z5d.
        cursor (str | Unset):  Example: eyJraW5kIjoib2Zmc2V0Iiwic2tpcCI6MjB9.
        take (int | Unset):  Default: 20. Example: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SearchResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        cursor=cursor,
        take=take,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    take: int | Unset = 20,
) -> Response[Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SearchResponse]:
    """Search collection segments

     Returns collection segments in search-response format with pagination.
    Reshapes the collection data: extracts segment results, includes media, computes pagination.

    Args:
        id (str):  Example: V1StGXR8_Z5d.
        cursor (str | Unset):  Example: eyJraW5kIjoib2Zmc2V0Iiwic2tpcCI6MjB9.
        take (int | Unset):  Default: 20. Example: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SearchResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        cursor=cursor,
        take=take,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    take: int | Unset = 20,
) -> Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SearchResponse | None:
    """Search collection segments

     Returns collection segments in search-response format with pagination.
    Reshapes the collection data: extracts segment results, includes media, computes pagination.

    Args:
        id (str):  Example: V1StGXR8_Z5d.
        cursor (str | Unset):  Example: eyJraW5kIjoib2Zmc2V0Iiwic2tpcCI6MjB9.
        take (int | Unset):  Default: 20. Example: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SearchResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            cursor=cursor,
            take=take,
        )
    ).parsed
