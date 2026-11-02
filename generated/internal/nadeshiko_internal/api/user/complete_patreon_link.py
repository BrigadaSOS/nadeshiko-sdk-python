from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.complete_patreon_link_body import CompletePatreonLinkBody
from ...models.complete_patreon_link_response_200 import CompletePatreonLinkResponse200
from ...models.error_400 import Error400
from ...models.error_401 import Error401
from ...models.error_500 import Error500
from ...types import Response


def _get_kwargs(
    *,
    body: CompletePatreonLinkBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/user/connections/patreon/callback",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CompletePatreonLinkResponse200 | Error400 | Error401 | Error500 | None:
    if response.status_code == 200:
        response_200 = CompletePatreonLinkResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error401.from_dict(response.json())

        return response_401

    if response.status_code == 500:
        response_500 = Error500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CompletePatreonLinkResponse200 | Error400 | Error401 | Error500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CompletePatreonLinkBody,
) -> Response[CompletePatreonLinkResponse200 | Error400 | Error401 | Error500]:
    """Complete Patreon OAuth linking

     Exchanges a one-time OAuth code and verifies membership in the configured Nadeshiko campaign.

    Args:
        body (CompletePatreonLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompletePatreonLinkResponse200 | Error400 | Error401 | Error500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CompletePatreonLinkBody,
) -> CompletePatreonLinkResponse200 | Error400 | Error401 | Error500 | None:
    """Complete Patreon OAuth linking

     Exchanges a one-time OAuth code and verifies membership in the configured Nadeshiko campaign.

    Args:
        body (CompletePatreonLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompletePatreonLinkResponse200 | Error400 | Error401 | Error500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CompletePatreonLinkBody,
) -> Response[CompletePatreonLinkResponse200 | Error400 | Error401 | Error500]:
    """Complete Patreon OAuth linking

     Exchanges a one-time OAuth code and verifies membership in the configured Nadeshiko campaign.

    Args:
        body (CompletePatreonLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompletePatreonLinkResponse200 | Error400 | Error401 | Error500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CompletePatreonLinkBody,
) -> CompletePatreonLinkResponse200 | Error400 | Error401 | Error500 | None:
    """Complete Patreon OAuth linking

     Exchanges a one-time OAuth code and verifies membership in the configured Nadeshiko campaign.

    Args:
        body (CompletePatreonLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompletePatreonLinkResponse200 | Error400 | Error401 | Error500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
