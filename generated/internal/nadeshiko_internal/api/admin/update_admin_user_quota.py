from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.account_quota_state import AccountQuotaState
from ...models.error_400 import Error400
from ...models.error_401 import Error401
from ...models.error_403 import Error403
from ...models.error_404 import Error404
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...models.update_account_quota_request import UpdateAccountQuotaRequest
from ...types import Response


def _get_kwargs(
    user_id: int,
    *,
    body: UpdateAccountQuotaRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/admin/users/{user_id}/quota".format(
            user_id=quote(str(user_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AccountQuotaState | Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | None:
    if response.status_code == 200:
        response_200 = AccountQuotaState.from_dict(response.json())

        return response_200

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
) -> Response[AccountQuotaState | Error400 | Error401 | Error403 | Error404 | Error429 | Error500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateAccountQuotaRequest,
) -> Response[AccountQuotaState | Error400 | Error401 | Error403 | Error404 | Error429 | Error500]:
    """Move an account to a tier, or give it an override

     Replaces the hand-edit against production that raising a quota used to
    require. Writes an audit log line naming the actor, the account, the before
    and after values, and the reason given.

    Args:
        user_id (int):
        body (UpdateAccountQuotaRequest): At least one property must be present. Send
            `quotaOverride: null` to clear an
            override and fall back to the tier.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountQuotaState | Error400 | Error401 | Error403 | Error404 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateAccountQuotaRequest,
) -> AccountQuotaState | Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | None:
    """Move an account to a tier, or give it an override

     Replaces the hand-edit against production that raising a quota used to
    require. Writes an audit log line naming the actor, the account, the before
    and after values, and the reason given.

    Args:
        user_id (int):
        body (UpdateAccountQuotaRequest): At least one property must be present. Send
            `quotaOverride: null` to clear an
            override and fall back to the tier.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountQuotaState | Error400 | Error401 | Error403 | Error404 | Error429 | Error500
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateAccountQuotaRequest,
) -> Response[AccountQuotaState | Error400 | Error401 | Error403 | Error404 | Error429 | Error500]:
    """Move an account to a tier, or give it an override

     Replaces the hand-edit against production that raising a quota used to
    require. Writes an audit log line naming the actor, the account, the before
    and after values, and the reason given.

    Args:
        user_id (int):
        body (UpdateAccountQuotaRequest): At least one property must be present. Send
            `quotaOverride: null` to clear an
            override and fall back to the tier.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountQuotaState | Error400 | Error401 | Error403 | Error404 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateAccountQuotaRequest,
) -> AccountQuotaState | Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | None:
    """Move an account to a tier, or give it an override

     Replaces the hand-edit against production that raising a quota used to
    require. Writes an audit log line naming the actor, the account, the before
    and after values, and the reason given.

    Args:
        user_id (int):
        body (UpdateAccountQuotaRequest): At least one property must be present. Send
            `quotaOverride: null` to clear an
            override and fall back to the tier.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountQuotaState | Error400 | Error401 | Error403 | Error404 | Error429 | Error500
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            body=body,
        )
    ).parsed
