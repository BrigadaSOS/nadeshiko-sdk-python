from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400 import Error400
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...models.unsubscribe_receipt import UnsubscribeReceipt
from ...types import UNSET, Response


def _get_kwargs(
    *,
    token: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["token"] = token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/email/unsubscribe",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error400 | Error429 | Error500 | UnsubscribeReceipt | None:
    if response.status_code == 200:
        response_200 = UnsubscribeReceipt.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error400.from_dict(response.json())

        return response_400

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
) -> Response[Error400 | Error429 | Error500 | UnsubscribeReceipt]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    token: str,
) -> Response[Error400 | Error429 | Error500 | UnsubscribeReceipt]:
    """Turn off lifecycle email

     Stops the day-7 note, the feedback ask and the monthly recap for the account
    the token names. Transactional mail — sign-in links, address verification —
    is unaffected, because a reader must not be able to lock themselves out of
    their own account by unsubscribing from a newsletter.

    Unauthenticated on purpose. The recipient is reading an email, not a signed-in
    page, and an opt-out that first demanded a password is the pattern that turns
    an unsubscribe into a spam complaint. The token carries the account, sealed,
    so no session is needed and none is trusted.

    THE TOKEN IS A QUERY PARAMETER BECAUSE RFC 8058 LEAVES NO CHOICE. This is the
    target of `List-Unsubscribe-Post`, and a one-click unsubscribe posts a fixed
    body — `List-Unsubscribe=One-Click` — to the URI verbatim. Nothing the sender
    puts in a request body survives that, so anything identifying the recipient
    has to travel in the URI. Any body sent is ignored rather than rejected, for
    the same reason.

    Idempotent: mailbox providers fire this with nobody present and may retry.

    Args:
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error429 | Error500 | UnsubscribeReceipt]
    """

    kwargs = _get_kwargs(
        token=token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    token: str,
) -> Error400 | Error429 | Error500 | UnsubscribeReceipt | None:
    """Turn off lifecycle email

     Stops the day-7 note, the feedback ask and the monthly recap for the account
    the token names. Transactional mail — sign-in links, address verification —
    is unaffected, because a reader must not be able to lock themselves out of
    their own account by unsubscribing from a newsletter.

    Unauthenticated on purpose. The recipient is reading an email, not a signed-in
    page, and an opt-out that first demanded a password is the pattern that turns
    an unsubscribe into a spam complaint. The token carries the account, sealed,
    so no session is needed and none is trusted.

    THE TOKEN IS A QUERY PARAMETER BECAUSE RFC 8058 LEAVES NO CHOICE. This is the
    target of `List-Unsubscribe-Post`, and a one-click unsubscribe posts a fixed
    body — `List-Unsubscribe=One-Click` — to the URI verbatim. Nothing the sender
    puts in a request body survives that, so anything identifying the recipient
    has to travel in the URI. Any body sent is ignored rather than rejected, for
    the same reason.

    Idempotent: mailbox providers fire this with nobody present and may retry.

    Args:
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error429 | Error500 | UnsubscribeReceipt
    """

    return sync_detailed(
        client=client,
        token=token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    token: str,
) -> Response[Error400 | Error429 | Error500 | UnsubscribeReceipt]:
    """Turn off lifecycle email

     Stops the day-7 note, the feedback ask and the monthly recap for the account
    the token names. Transactional mail — sign-in links, address verification —
    is unaffected, because a reader must not be able to lock themselves out of
    their own account by unsubscribing from a newsletter.

    Unauthenticated on purpose. The recipient is reading an email, not a signed-in
    page, and an opt-out that first demanded a password is the pattern that turns
    an unsubscribe into a spam complaint. The token carries the account, sealed,
    so no session is needed and none is trusted.

    THE TOKEN IS A QUERY PARAMETER BECAUSE RFC 8058 LEAVES NO CHOICE. This is the
    target of `List-Unsubscribe-Post`, and a one-click unsubscribe posts a fixed
    body — `List-Unsubscribe=One-Click` — to the URI verbatim. Nothing the sender
    puts in a request body survives that, so anything identifying the recipient
    has to travel in the URI. Any body sent is ignored rather than rejected, for
    the same reason.

    Idempotent: mailbox providers fire this with nobody present and may retry.

    Args:
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error429 | Error500 | UnsubscribeReceipt]
    """

    kwargs = _get_kwargs(
        token=token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    token: str,
) -> Error400 | Error429 | Error500 | UnsubscribeReceipt | None:
    """Turn off lifecycle email

     Stops the day-7 note, the feedback ask and the monthly recap for the account
    the token names. Transactional mail — sign-in links, address verification —
    is unaffected, because a reader must not be able to lock themselves out of
    their own account by unsubscribing from a newsletter.

    Unauthenticated on purpose. The recipient is reading an email, not a signed-in
    page, and an opt-out that first demanded a password is the pattern that turns
    an unsubscribe into a spam complaint. The token carries the account, sealed,
    so no session is needed and none is trusted.

    THE TOKEN IS A QUERY PARAMETER BECAUSE RFC 8058 LEAVES NO CHOICE. This is the
    target of `List-Unsubscribe-Post`, and a one-click unsubscribe posts a fixed
    body — `List-Unsubscribe=One-Click` — to the URI verbatim. Nothing the sender
    puts in a request body survives that, so anything identifying the recipient
    has to travel in the URI. Any body sent is ignored rather than rejected, for
    the same reason.

    Idempotent: mailbox providers fire this with nobody present and may retry.

    Args:
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error429 | Error500 | UnsubscribeReceipt
    """

    return (
        await asyncio_detailed(
            client=client,
            token=token,
        )
    ).parsed
