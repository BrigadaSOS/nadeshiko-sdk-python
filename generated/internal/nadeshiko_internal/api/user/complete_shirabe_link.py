from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.complete_shirabe_link_body import CompleteShirabeLinkBody
from ...models.complete_shirabe_link_response_200 import CompleteShirabeLinkResponse200
from ...models.error_400 import Error400
from ...models.error_401 import Error401
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...types import Response


def _get_kwargs(
    *,
    body: CompleteShirabeLinkBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/user/connections/shirabe/callback",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CompleteShirabeLinkResponse200 | Error400 | Error401 | Error429 | Error500 | None:
    if response.status_code == 200:
        response_200 = CompleteShirabeLinkResponse200.from_dict(response.json())

        return response_200

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
) -> Response[CompleteShirabeLinkResponse200 | Error400 | Error401 | Error429 | Error500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CompleteShirabeLinkBody,
) -> Response[CompleteShirabeLinkResponse200 | Error400 | Error401 | Error429 | Error500]:
    """Finish linking a Shirabe account

     Exchanges the one-time code Shirabe redirected back with for a scoped key,
    reads the reader's dictionary stack, and stores the link.

    The `state` must be the one this session started the flow with. It carries
    the account it belongs to, and a mismatch is refused: otherwise somebody who
    completed their own authorization at Shirabe could hand the callback URL to a
    signed-in victim and attach their account to the victim's.

    Args:
        body (CompleteShirabeLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompleteShirabeLinkResponse200 | Error400 | Error401 | Error429 | Error500]
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
    body: CompleteShirabeLinkBody,
) -> CompleteShirabeLinkResponse200 | Error400 | Error401 | Error429 | Error500 | None:
    """Finish linking a Shirabe account

     Exchanges the one-time code Shirabe redirected back with for a scoped key,
    reads the reader's dictionary stack, and stores the link.

    The `state` must be the one this session started the flow with. It carries
    the account it belongs to, and a mismatch is refused: otherwise somebody who
    completed their own authorization at Shirabe could hand the callback URL to a
    signed-in victim and attach their account to the victim's.

    Args:
        body (CompleteShirabeLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompleteShirabeLinkResponse200 | Error400 | Error401 | Error429 | Error500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CompleteShirabeLinkBody,
) -> Response[CompleteShirabeLinkResponse200 | Error400 | Error401 | Error429 | Error500]:
    """Finish linking a Shirabe account

     Exchanges the one-time code Shirabe redirected back with for a scoped key,
    reads the reader's dictionary stack, and stores the link.

    The `state` must be the one this session started the flow with. It carries
    the account it belongs to, and a mismatch is refused: otherwise somebody who
    completed their own authorization at Shirabe could hand the callback URL to a
    signed-in victim and attach their account to the victim's.

    Args:
        body (CompleteShirabeLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompleteShirabeLinkResponse200 | Error400 | Error401 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CompleteShirabeLinkBody,
) -> CompleteShirabeLinkResponse200 | Error400 | Error401 | Error429 | Error500 | None:
    """Finish linking a Shirabe account

     Exchanges the one-time code Shirabe redirected back with for a scoped key,
    reads the reader's dictionary stack, and stores the link.

    The `state` must be the one this session started the flow with. It carries
    the account it belongs to, and a mismatch is refused: otherwise somebody who
    completed their own authorization at Shirabe could hand the callback URL to a
    signed-in victim and attach their account to the victim's.

    Args:
        body (CompleteShirabeLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompleteShirabeLinkResponse200 | Error400 | Error401 | Error429 | Error500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
