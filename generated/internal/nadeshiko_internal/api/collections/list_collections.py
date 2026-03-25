from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.collection_list_response import CollectionListResponse
from ...models.error_400 import Error400
from ...models.error_401 import Error401
from ...models.error_403 import Error403
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...models.list_collections_visibility import ListCollectionsVisibility
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    visibility: ListCollectionsVisibility | Unset = UNSET,
    cursor: str | Unset = UNSET,
    take: int | Unset = 20,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_visibility: str | Unset = UNSET
    if not isinstance(visibility, Unset):
        json_visibility = visibility.value

    params["visibility"] = json_visibility

    params["cursor"] = cursor

    params["take"] = take

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/collections",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CollectionListResponse | Error400 | Error401 | Error403 | Error429 | Error500 | None:
    if response.status_code == 200:
        response_200 = CollectionListResponse.from_dict(response.json())

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
) -> Response[CollectionListResponse | Error400 | Error401 | Error403 | Error429 | Error500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    visibility: ListCollectionsVisibility | Unset = UNSET,
    cursor: str | Unset = UNSET,
    take: int | Unset = 20,
) -> Response[CollectionListResponse | Error400 | Error401 | Error403 | Error429 | Error500]:
    """List user's collections

     Returns all collections for the authenticated user. Can filter by visibility.

    Args:
        visibility (ListCollectionsVisibility | Unset):  Example: private.
        cursor (str | Unset):  Example: eyJraW5kIjoib2Zmc2V0Iiwic2tpcCI6MjB9.
        take (int | Unset):  Default: 20. Example: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CollectionListResponse | Error400 | Error401 | Error403 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        visibility=visibility,
        cursor=cursor,
        take=take,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    visibility: ListCollectionsVisibility | Unset = UNSET,
    cursor: str | Unset = UNSET,
    take: int | Unset = 20,
) -> CollectionListResponse | Error400 | Error401 | Error403 | Error429 | Error500 | None:
    """List user's collections

     Returns all collections for the authenticated user. Can filter by visibility.

    Args:
        visibility (ListCollectionsVisibility | Unset):  Example: private.
        cursor (str | Unset):  Example: eyJraW5kIjoib2Zmc2V0Iiwic2tpcCI6MjB9.
        take (int | Unset):  Default: 20. Example: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CollectionListResponse | Error400 | Error401 | Error403 | Error429 | Error500
    """

    return sync_detailed(
        client=client,
        visibility=visibility,
        cursor=cursor,
        take=take,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    visibility: ListCollectionsVisibility | Unset = UNSET,
    cursor: str | Unset = UNSET,
    take: int | Unset = 20,
) -> Response[CollectionListResponse | Error400 | Error401 | Error403 | Error429 | Error500]:
    """List user's collections

     Returns all collections for the authenticated user. Can filter by visibility.

    Args:
        visibility (ListCollectionsVisibility | Unset):  Example: private.
        cursor (str | Unset):  Example: eyJraW5kIjoib2Zmc2V0Iiwic2tpcCI6MjB9.
        take (int | Unset):  Default: 20. Example: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CollectionListResponse | Error400 | Error401 | Error403 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        visibility=visibility,
        cursor=cursor,
        take=take,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    visibility: ListCollectionsVisibility | Unset = UNSET,
    cursor: str | Unset = UNSET,
    take: int | Unset = 20,
) -> CollectionListResponse | Error400 | Error401 | Error403 | Error429 | Error500 | None:
    """List user's collections

     Returns all collections for the authenticated user. Can filter by visibility.

    Args:
        visibility (ListCollectionsVisibility | Unset):  Example: private.
        cursor (str | Unset):  Example: eyJraW5kIjoib2Zmc2V0Iiwic2tpcCI6MjB9.
        take (int | Unset):  Default: 20. Example: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CollectionListResponse | Error400 | Error401 | Error403 | Error429 | Error500
    """

    return (
        await asyncio_detailed(
            client=client,
            visibility=visibility,
            cursor=cursor,
            take=take,
        )
    ).parsed
