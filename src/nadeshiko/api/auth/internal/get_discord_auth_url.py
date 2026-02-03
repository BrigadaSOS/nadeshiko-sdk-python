from http import HTTPStatus
from typing import Any

import httpx

from .... import errors
from ....client import AuthenticatedClient, Client
from ....models.discord_auth_url_response import DiscordAuthUrlResponse
from ....models.error import Error
from ....types import UNSET, Response, Unset


def _get_kwargs(
    *,
    referer: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(referer, Unset):
        headers["Referer"] = referer

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/auth/discord/url",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DiscordAuthUrlResponse | Error | None:
    if response.status_code == 200:
        response_200 = DiscordAuthUrlResponse.from_dict(response.json())

        return response_200

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
) -> Response[DiscordAuthUrlResponse | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    referer: str | Unset = UNSET,
) -> Response[DiscordAuthUrlResponse | Error]:
    """(OAuth) Get Discord Login URL

     Get the Discord OAuth authorization URL for login

    Args:
        referer (str | Unset):  Example: http://localhost:3000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DiscordAuthUrlResponse | Error]
    """

    kwargs = _get_kwargs(
        referer=referer,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    referer: str | Unset = UNSET,
) -> DiscordAuthUrlResponse | Error | None:
    """(OAuth) Get Discord Login URL

     Get the Discord OAuth authorization URL for login

    Args:
        referer (str | Unset):  Example: http://localhost:3000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DiscordAuthUrlResponse | Error
    """

    return sync_detailed(
        client=client,
        referer=referer,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    referer: str | Unset = UNSET,
) -> Response[DiscordAuthUrlResponse | Error]:
    """(OAuth) Get Discord Login URL

     Get the Discord OAuth authorization URL for login

    Args:
        referer (str | Unset):  Example: http://localhost:3000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DiscordAuthUrlResponse | Error]
    """

    kwargs = _get_kwargs(
        referer=referer,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    referer: str | Unset = UNSET,
) -> DiscordAuthUrlResponse | Error | None:
    """(OAuth) Get Discord Login URL

     Get the Discord OAuth authorization URL for login

    Args:
        referer (str | Unset):  Example: http://localhost:3000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DiscordAuthUrlResponse | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            referer=referer,
        )
    ).parsed
