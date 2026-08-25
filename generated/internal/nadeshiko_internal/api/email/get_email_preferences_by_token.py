from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400 import Error400
from ...models.get_email_preferences_by_token_response_200 import (
    GetEmailPreferencesByTokenResponse200,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    token: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["token"] = token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/email/preferences",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error400 | GetEmailPreferencesByTokenResponse200 | None:
    if response.status_code == 200:
        response_200 = GetEmailPreferencesByTokenResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error400.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error400 | GetEmailPreferencesByTokenResponse200]:
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
) -> Response[Error400 | GetEmailPreferencesByTokenResponse200]:
    """Read email preferences from an unsubscribe token

     What the account the token names currently receives, so the unsubscribe page
    can show the reader their real settings rather than a guess.

    Unauthenticated on purpose, for the same reason the unsubscribe endpoint is:
    the recipient is reading an email, not a signed-in page, and a preference
    screen that first demanded a password is the pattern that turns an opt-out
    into a spam complaint.

    SAFE TO PREFETCH. Mail scanners fetch every link in a message before the
    recipient ever sees it, so this reads and never writes — the change happens
    on the PATCH, which a scanner will not issue.

    Discloses only which categories the account is on, to a holder who already
    has the token from their own inbox.

    Args:
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | GetEmailPreferencesByTokenResponse200]
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
) -> Error400 | GetEmailPreferencesByTokenResponse200 | None:
    """Read email preferences from an unsubscribe token

     What the account the token names currently receives, so the unsubscribe page
    can show the reader their real settings rather than a guess.

    Unauthenticated on purpose, for the same reason the unsubscribe endpoint is:
    the recipient is reading an email, not a signed-in page, and a preference
    screen that first demanded a password is the pattern that turns an opt-out
    into a spam complaint.

    SAFE TO PREFETCH. Mail scanners fetch every link in a message before the
    recipient ever sees it, so this reads and never writes — the change happens
    on the PATCH, which a scanner will not issue.

    Discloses only which categories the account is on, to a holder who already
    has the token from their own inbox.

    Args:
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | GetEmailPreferencesByTokenResponse200
    """

    return sync_detailed(
        client=client,
        token=token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    token: str,
) -> Response[Error400 | GetEmailPreferencesByTokenResponse200]:
    """Read email preferences from an unsubscribe token

     What the account the token names currently receives, so the unsubscribe page
    can show the reader their real settings rather than a guess.

    Unauthenticated on purpose, for the same reason the unsubscribe endpoint is:
    the recipient is reading an email, not a signed-in page, and a preference
    screen that first demanded a password is the pattern that turns an opt-out
    into a spam complaint.

    SAFE TO PREFETCH. Mail scanners fetch every link in a message before the
    recipient ever sees it, so this reads and never writes — the change happens
    on the PATCH, which a scanner will not issue.

    Discloses only which categories the account is on, to a holder who already
    has the token from their own inbox.

    Args:
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | GetEmailPreferencesByTokenResponse200]
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
) -> Error400 | GetEmailPreferencesByTokenResponse200 | None:
    """Read email preferences from an unsubscribe token

     What the account the token names currently receives, so the unsubscribe page
    can show the reader their real settings rather than a guess.

    Unauthenticated on purpose, for the same reason the unsubscribe endpoint is:
    the recipient is reading an email, not a signed-in page, and a preference
    screen that first demanded a password is the pattern that turns an opt-out
    into a spam complaint.

    SAFE TO PREFETCH. Mail scanners fetch every link in a message before the
    recipient ever sees it, so this reads and never writes — the change happens
    on the PATCH, which a scanner will not issue.

    Discloses only which categories the account is on, to a holder who already
    has the token from their own inbox.

    Args:
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | GetEmailPreferencesByTokenResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            token=token,
        )
    ).parsed
