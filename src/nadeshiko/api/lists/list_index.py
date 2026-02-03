from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.list_ import List
from ...models.list_index_type import ListIndexType
from ...models.list_index_visibility import ListIndexVisibility
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    visibility: ListIndexVisibility | Unset = UNSET,
    type_: ListIndexType | Unset = UNSET,
    user_id: int | Unset = UNSET,
    media_id: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_visibility: str | Unset = UNSET
    if not isinstance(visibility, Unset):
        json_visibility = visibility.value

    params["visibility"] = json_visibility

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params["userId"] = user_id

    params["mediaId"] = media_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/lists",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | list[List] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = List.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Error | list[List]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    visibility: ListIndexVisibility | Unset = UNSET,
    type_: ListIndexType | Unset = UNSET,
    user_id: int | Unset = UNSET,
    media_id: int | Unset = UNSET,
) -> Response[Error | list[List]]:
    """List all lists

     Returns all lists matching the query filters. Can filter by media ID to find lists containing a
    specific media. Public lists are visible to all users.

    Args:
        visibility (ListIndexVisibility | Unset):  Example: public.
        type_ (ListIndexType | Unset):  Example: SERIES.
        user_id (int | Unset):  Example: 1.
        media_id (int | Unset):  Example: 12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[List]]
    """

    kwargs = _get_kwargs(
        visibility=visibility,
        type_=type_,
        user_id=user_id,
        media_id=media_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    visibility: ListIndexVisibility | Unset = UNSET,
    type_: ListIndexType | Unset = UNSET,
    user_id: int | Unset = UNSET,
    media_id: int | Unset = UNSET,
) -> Error | list[List] | None:
    """List all lists

     Returns all lists matching the query filters. Can filter by media ID to find lists containing a
    specific media. Public lists are visible to all users.

    Args:
        visibility (ListIndexVisibility | Unset):  Example: public.
        type_ (ListIndexType | Unset):  Example: SERIES.
        user_id (int | Unset):  Example: 1.
        media_id (int | Unset):  Example: 12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[List]
    """

    return sync_detailed(
        client=client,
        visibility=visibility,
        type_=type_,
        user_id=user_id,
        media_id=media_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    visibility: ListIndexVisibility | Unset = UNSET,
    type_: ListIndexType | Unset = UNSET,
    user_id: int | Unset = UNSET,
    media_id: int | Unset = UNSET,
) -> Response[Error | list[List]]:
    """List all lists

     Returns all lists matching the query filters. Can filter by media ID to find lists containing a
    specific media. Public lists are visible to all users.

    Args:
        visibility (ListIndexVisibility | Unset):  Example: public.
        type_ (ListIndexType | Unset):  Example: SERIES.
        user_id (int | Unset):  Example: 1.
        media_id (int | Unset):  Example: 12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[List]]
    """

    kwargs = _get_kwargs(
        visibility=visibility,
        type_=type_,
        user_id=user_id,
        media_id=media_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    visibility: ListIndexVisibility | Unset = UNSET,
    type_: ListIndexType | Unset = UNSET,
    user_id: int | Unset = UNSET,
    media_id: int | Unset = UNSET,
) -> Error | list[List] | None:
    """List all lists

     Returns all lists matching the query filters. Can filter by media ID to find lists containing a
    specific media. Public lists are visible to all users.

    Args:
        visibility (ListIndexVisibility | Unset):  Example: public.
        type_ (ListIndexType | Unset):  Example: SERIES.
        user_id (int | Unset):  Example: 1.
        media_id (int | Unset):  Example: 12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[List]
    """

    return (
        await asyncio_detailed(
            client=client,
            visibility=visibility,
            type_=type_,
            user_id=user_id,
            media_id=media_id,
        )
    ).parsed
