from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400 import Error400
from ...models.error_401 import Error401
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...models.start_shirabe_link_response_201 import StartShirabeLinkResponse201
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/user/connections/shirabe",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error400 | Error401 | Error429 | Error500 | StartShirabeLinkResponse201 | None:
    if response.status_code == 201:
        response_201 = StartShirabeLinkResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = Error400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error401.from_dict(response.json())

        return response_401

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
) -> Response[Error400 | Error401 | Error429 | Error500 | StartShirabeLinkResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Error400 | Error401 | Error429 | Error500 | StartShirabeLinkResponse201]:
    """Begin linking a Shirabe account

     Starts an OAuth 2.0 authorization-code flow (PKCE) against Shirabe and
    returns where to send the reader. Nothing is stored until they approve.

    The `state` is the pending flow itself, sealed with a server-side key rather
    than a handle into server memory: the request that starts the link and the
    one that finishes it are minutes apart and nothing routes them to the same
    process.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error429 | Error500 | StartShirabeLinkResponse201]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Error400 | Error401 | Error429 | Error500 | StartShirabeLinkResponse201 | None:
    """Begin linking a Shirabe account

     Starts an OAuth 2.0 authorization-code flow (PKCE) against Shirabe and
    returns where to send the reader. Nothing is stored until they approve.

    The `state` is the pending flow itself, sealed with a server-side key rather
    than a handle into server memory: the request that starts the link and the
    one that finishes it are minutes apart and nothing routes them to the same
    process.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error429 | Error500 | StartShirabeLinkResponse201
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Error400 | Error401 | Error429 | Error500 | StartShirabeLinkResponse201]:
    """Begin linking a Shirabe account

     Starts an OAuth 2.0 authorization-code flow (PKCE) against Shirabe and
    returns where to send the reader. Nothing is stored until they approve.

    The `state` is the pending flow itself, sealed with a server-side key rather
    than a handle into server memory: the request that starts the link and the
    one that finishes it are minutes apart and nothing routes them to the same
    process.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error429 | Error500 | StartShirabeLinkResponse201]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Error400 | Error401 | Error429 | Error500 | StartShirabeLinkResponse201 | None:
    """Begin linking a Shirabe account

     Starts an OAuth 2.0 authorization-code flow (PKCE) against Shirabe and
    returns where to send the reader. Nothing is stored until they approve.

    The `state` is the pending flow itself, sealed with a server-side key rather
    than a handle into server memory: the request that starts the link and the
    one that finishes it are minutes apart and nothing routes them to the same
    process.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error429 | Error500 | StartShirabeLinkResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
