from http import HTTPStatus
from typing import Any, cast
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
from ...types import Response


def _get_kwargs(
    media_id: str,
    episode_number: int,
    id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/media/{media_id}/episodes/{episode_number}/segments/{id}".format(
            media_id=quote(str(media_id), safe=""),
            episode_number=quote(str(episode_number), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Any | Error400 | Error401 | Error403 | Error404 | Error429 | Error500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    media_id: str,
    episode_number: int,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | Error400 | Error401 | Error403 | Error404 | Error429 | Error500]:
    """Delete segment

     Soft-deletes a segment by setting its status to DELETED.

    Args:
        media_id (str):
        episode_number (int):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error400 | Error401 | Error403 | Error404 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        media_id=media_id,
        episode_number=episode_number,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    media_id: str,
    episode_number: int,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Any | Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | None:
    """Delete segment

     Soft-deletes a segment by setting its status to DELETED.

    Args:
        media_id (str):
        episode_number (int):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error400 | Error401 | Error403 | Error404 | Error429 | Error500
    """

    return sync_detailed(
        media_id=media_id,
        episode_number=episode_number,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    media_id: str,
    episode_number: int,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | Error400 | Error401 | Error403 | Error404 | Error429 | Error500]:
    """Delete segment

     Soft-deletes a segment by setting its status to DELETED.

    Args:
        media_id (str):
        episode_number (int):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error400 | Error401 | Error403 | Error404 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        media_id=media_id,
        episode_number=episode_number,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    media_id: str,
    episode_number: int,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Any | Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | None:
    """Delete segment

     Soft-deletes a segment by setting its status to DELETED.

    Args:
        media_id (str):
        episode_number (int):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error400 | Error401 | Error403 | Error404 | Error429 | Error500
    """

    return (
        await asyncio_detailed(
            media_id=media_id,
            episode_number=episode_number,
            id=id,
            client=client,
        )
    ).parsed
