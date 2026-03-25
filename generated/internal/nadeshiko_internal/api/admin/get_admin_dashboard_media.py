from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_401 import Error401
from ...models.error_403 import Error403
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...models.get_admin_dashboard_media_response_200 import GetAdminDashboardMediaResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/admin/dashboard/media",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error401 | Error403 | Error429 | Error500 | GetAdminDashboardMediaResponse200 | None:
    if response.status_code == 200:
        response_200 = GetAdminDashboardMediaResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error401.from_dict(response.json())

        return response_401

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
) -> Response[Error401 | Error403 | Error429 | Error500 | GetAdminDashboardMediaResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Error401 | Error403 | Error429 | Error500 | GetAdminDashboardMediaResponse200]:
    """Get media breakdown statistics

     Returns media breakdowns by category, format, status, genre, studio,
    segment content ratings, segment statuses, and top media by interaction.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error401 | Error403 | Error429 | Error500 | GetAdminDashboardMediaResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Error401 | Error403 | Error429 | Error500 | GetAdminDashboardMediaResponse200 | None:
    """Get media breakdown statistics

     Returns media breakdowns by category, format, status, genre, studio,
    segment content ratings, segment statuses, and top media by interaction.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error401 | Error403 | Error429 | Error500 | GetAdminDashboardMediaResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Error401 | Error403 | Error429 | Error500 | GetAdminDashboardMediaResponse200]:
    """Get media breakdown statistics

     Returns media breakdowns by category, format, status, genre, studio,
    segment content ratings, segment statuses, and top media by interaction.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error401 | Error403 | Error429 | Error500 | GetAdminDashboardMediaResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Error401 | Error403 | Error429 | Error500 | GetAdminDashboardMediaResponse200 | None:
    """Get media breakdown statistics

     Returns media breakdowns by category, format, status, genre, studio,
    segment content ratings, segment statuses, and top media by interaction.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error401 | Error403 | Error429 | Error500 | GetAdminDashboardMediaResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
