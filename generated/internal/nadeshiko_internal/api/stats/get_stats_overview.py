from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_500 import Error500
from ...models.get_stats_overview_response_200 import GetStatsOverviewResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/stats/overview",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error500 | GetStatsOverviewResponse200 | None:
    if response.status_code == 200:
        response_200 = GetStatsOverviewResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 500:
        response_500 = Error500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error500 | GetStatsOverviewResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Error500 | GetStatsOverviewResponse200]:
    """Get corpus statistics overview

     Returns a comprehensive overview of corpus statistics including headline numbers,
    word frequency coverage tiers, and translation availability. This is the primary
    data source for the public /stats page.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error500 | GetStatsOverviewResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Error500 | GetStatsOverviewResponse200 | None:
    """Get corpus statistics overview

     Returns a comprehensive overview of corpus statistics including headline numbers,
    word frequency coverage tiers, and translation availability. This is the primary
    data source for the public /stats page.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error500 | GetStatsOverviewResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Error500 | GetStatsOverviewResponse200]:
    """Get corpus statistics overview

     Returns a comprehensive overview of corpus statistics including headline numbers,
    word frequency coverage tiers, and translation availability. This is the primary
    data source for the public /stats page.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error500 | GetStatsOverviewResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Error500 | GetStatsOverviewResponse200 | None:
    """Get corpus statistics overview

     Returns a comprehensive overview of corpus statistics including headline numbers,
    word frequency coverage tiers, and translation availability. This is the primary
    data source for the public /stats page.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error500 | GetStatsOverviewResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
