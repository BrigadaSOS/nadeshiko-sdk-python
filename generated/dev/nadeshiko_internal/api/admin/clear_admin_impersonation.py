from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.clear_admin_impersonation_response_200 import ClearAdminImpersonationResponse200
from ...models.error_403 import Error403
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/admin/impersonation",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ClearAdminImpersonationResponse200 | Error403 | Error429 | Error500 | None:
    if response.status_code == 200:
        response_200 = ClearAdminImpersonationResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = Error403.from_dict(response.json())

        return response_403

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
) -> Response[ClearAdminImpersonationResponse200 | Error403 | Error429 | Error500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ClearAdminImpersonationResponse200 | Error403 | Error429 | Error500]:
    """Clear admin impersonation

     Clears the current impersonation session and related cookies.
    This endpoint is only available in local environment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClearAdminImpersonationResponse200 | Error403 | Error429 | Error500]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> ClearAdminImpersonationResponse200 | Error403 | Error429 | Error500 | None:
    """Clear admin impersonation

     Clears the current impersonation session and related cookies.
    This endpoint is only available in local environment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClearAdminImpersonationResponse200 | Error403 | Error429 | Error500
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ClearAdminImpersonationResponse200 | Error403 | Error429 | Error500]:
    """Clear admin impersonation

     Clears the current impersonation session and related cookies.
    This endpoint is only available in local environment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClearAdminImpersonationResponse200 | Error403 | Error429 | Error500]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> ClearAdminImpersonationResponse200 | Error403 | Error429 | Error500 | None:
    """Clear admin impersonation

     Clears the current impersonation session and related cookies.
    This endpoint is only available in local environment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClearAdminImpersonationResponse200 | Error403 | Error429 | Error500
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
