from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.episode import Episode
from ...models.episode_create_request import EpisodeCreateRequest
from ...models.error_400 import Error400
from ...models.error_401 import Error401
from ...models.error_403 import Error403
from ...models.error_404 import Error404
from ...models.error_409 import Error409
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...types import Response


def _get_kwargs(
    media_public_id: str,
    *,
    body: EpisodeCreateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/media/{media_public_id}/episodes".format(
            media_public_id=quote(str(media_public_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Episode | Error400 | Error401 | Error403 | Error404 | Error409 | Error429 | Error500 | None:
    if response.status_code == 201:
        response_201 = Episode.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = Error409.from_dict(response.json())

        return response_409

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
) -> Response[Episode | Error400 | Error401 | Error403 | Error404 | Error409 | Error429 | Error500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    media_public_id: str,
    *,
    client: AuthenticatedClient,
    body: EpisodeCreateRequest,
) -> Response[Episode | Error400 | Error401 | Error403 | Error404 | Error409 | Error429 | Error500]:
    """Create episode

     Creates a new episode for a specific media.

    Args:
        media_public_id (str):
        body (EpisodeCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Episode | Error400 | Error401 | Error403 | Error404 | Error409 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        media_public_id=media_public_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    media_public_id: str,
    *,
    client: AuthenticatedClient,
    body: EpisodeCreateRequest,
) -> Episode | Error400 | Error401 | Error403 | Error404 | Error409 | Error429 | Error500 | None:
    """Create episode

     Creates a new episode for a specific media.

    Args:
        media_public_id (str):
        body (EpisodeCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Episode | Error400 | Error401 | Error403 | Error404 | Error409 | Error429 | Error500
    """

    return sync_detailed(
        media_public_id=media_public_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    media_public_id: str,
    *,
    client: AuthenticatedClient,
    body: EpisodeCreateRequest,
) -> Response[Episode | Error400 | Error401 | Error403 | Error404 | Error409 | Error429 | Error500]:
    """Create episode

     Creates a new episode for a specific media.

    Args:
        media_public_id (str):
        body (EpisodeCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Episode | Error400 | Error401 | Error403 | Error404 | Error409 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        media_public_id=media_public_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    media_public_id: str,
    *,
    client: AuthenticatedClient,
    body: EpisodeCreateRequest,
) -> Episode | Error400 | Error401 | Error403 | Error404 | Error409 | Error429 | Error500 | None:
    """Create episode

     Creates a new episode for a specific media.

    Args:
        media_public_id (str):
        body (EpisodeCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Episode | Error400 | Error401 | Error403 | Error404 | Error409 | Error429 | Error500
    """

    return (
        await asyncio_detailed(
            media_public_id=media_public_id,
            client=client,
            body=body,
        )
    ).parsed
