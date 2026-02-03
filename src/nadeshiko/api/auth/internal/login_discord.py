from http import HTTPStatus
from typing import Any

import httpx

from .... import errors
from ....client import AuthenticatedClient, Client
from ....models.discord_login_request import DiscordLoginRequest
from ....models.error import Error
from ....models.login_response import LoginResponse
from ....types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: DiscordLoginRequest,
    referer: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(referer, Unset):
        headers["Referer"] = referer

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/auth/discord",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | LoginResponse | None:
    if response.status_code == 200:
        response_200 = LoginResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())

        return response_409

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
) -> Response[Error | LoginResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DiscordLoginRequest,
    referer: str | Unset = UNSET,
) -> Response[Error | LoginResponse]:
    """(OAuth) Login with Discord

     Receive the callback from Discord OAuth2 and authenticate or register the user properly.

    Args:
        referer (str | Unset):  Example: http://localhost:3000.
        body (DiscordLoginRequest): Discord OAuth Login Request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | LoginResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        referer=referer,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: DiscordLoginRequest,
    referer: str | Unset = UNSET,
) -> Error | LoginResponse | None:
    """(OAuth) Login with Discord

     Receive the callback from Discord OAuth2 and authenticate or register the user properly.

    Args:
        referer (str | Unset):  Example: http://localhost:3000.
        body (DiscordLoginRequest): Discord OAuth Login Request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | LoginResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        referer=referer,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DiscordLoginRequest,
    referer: str | Unset = UNSET,
) -> Response[Error | LoginResponse]:
    """(OAuth) Login with Discord

     Receive the callback from Discord OAuth2 and authenticate or register the user properly.

    Args:
        referer (str | Unset):  Example: http://localhost:3000.
        body (DiscordLoginRequest): Discord OAuth Login Request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | LoginResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        referer=referer,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DiscordLoginRequest,
    referer: str | Unset = UNSET,
) -> Error | LoginResponse | None:
    """(OAuth) Login with Discord

     Receive the callback from Discord OAuth2 and authenticate or register the user properly.

    Args:
        referer (str | Unset):  Example: http://localhost:3000.
        body (DiscordLoginRequest): Discord OAuth Login Request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | LoginResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            referer=referer,
        )
    ).parsed
