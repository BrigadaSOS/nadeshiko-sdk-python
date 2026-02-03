from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from .... import errors
from ....client import AuthenticatedClient, Client
from ....models.error import Error
from ....models.list_remove_item_response_200 import ListRemoveItemResponse200
from ....types import Response


def _get_kwargs(
    id: int,
    media_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/lists/{id}/items/{media_id}".format(
            id=quote(str(id), safe=""),
            media_id=quote(str(media_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | ListRemoveItemResponse200 | None:
    if response.status_code == 200:
        response_200 = ListRemoveItemResponse200.from_dict(response.json())

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
) -> Response[Error | ListRemoveItemResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    media_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Error | ListRemoveItemResponse200]:
    """Remove media from list

     Removes a media entry from the list. Requires admin permissions.

    Args:
        id (int):  Example: 123.
        media_id (int):  Example: 7674.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListRemoveItemResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        media_id=media_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    media_id: int,
    *,
    client: AuthenticatedClient,
) -> Error | ListRemoveItemResponse200 | None:
    """Remove media from list

     Removes a media entry from the list. Requires admin permissions.

    Args:
        id (int):  Example: 123.
        media_id (int):  Example: 7674.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListRemoveItemResponse200
    """

    return sync_detailed(
        id=id,
        media_id=media_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    media_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Error | ListRemoveItemResponse200]:
    """Remove media from list

     Removes a media entry from the list. Requires admin permissions.

    Args:
        id (int):  Example: 123.
        media_id (int):  Example: 7674.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListRemoveItemResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        media_id=media_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    media_id: int,
    *,
    client: AuthenticatedClient,
) -> Error | ListRemoveItemResponse200 | None:
    """Remove media from list

     Removes a media entry from the list. Requires admin permissions.

    Args:
        id (int):  Example: 123.
        media_id (int):  Example: 7674.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListRemoveItemResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            media_id=media_id,
            client=client,
        )
    ).parsed
