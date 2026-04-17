from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400 import Error400
from ...models.error_401 import Error401
from ...models.error_403 import Error403
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...models.search_stats_request import SearchStatsRequest
from ...models.search_stats_response import SearchStatsResponse
from ...types import Response


def _get_kwargs(
    *,
    body: SearchStatsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/search/stats",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error400 | Error401 | Error403 | Error429 | Error500 | SearchStatsResponse | None:
    if response.status_code == 200:
        response_200 = SearchStatsResponse.from_dict(response.json())

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
) -> Response[Error400 | Error401 | Error403 | Error429 | Error500 | SearchStatsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SearchStatsRequest,
) -> Response[Error400 | Error401 | Error403 | Error429 | Error500 | SearchStatsResponse]:
    """Get search statistics

     Returns filter statistics for a query without returning segment results. Useful for populating
    filter UIs:
    - `media`: media matching the query, with per-episode hit counts
    - `categories`: segment counts grouped by media category

    Stats are scoped by the query and category filters but are not narrowed by a selected media/episode
    — so selecting a media in the UI doesn't zero out other media from the list.

    Args:
        body (SearchStatsRequest): Stats request. All fields are optional — omit `query` to get
            filter counts for the full corpus.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error429 | Error500 | SearchStatsResponse]
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
    body: SearchStatsRequest,
) -> Error400 | Error401 | Error403 | Error429 | Error500 | SearchStatsResponse | None:
    """Get search statistics

     Returns filter statistics for a query without returning segment results. Useful for populating
    filter UIs:
    - `media`: media matching the query, with per-episode hit counts
    - `categories`: segment counts grouped by media category

    Stats are scoped by the query and category filters but are not narrowed by a selected media/episode
    — so selecting a media in the UI doesn't zero out other media from the list.

    Args:
        body (SearchStatsRequest): Stats request. All fields are optional — omit `query` to get
            filter counts for the full corpus.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error403 | Error429 | Error500 | SearchStatsResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SearchStatsRequest,
) -> Response[Error400 | Error401 | Error403 | Error429 | Error500 | SearchStatsResponse]:
    """Get search statistics

     Returns filter statistics for a query without returning segment results. Useful for populating
    filter UIs:
    - `media`: media matching the query, with per-episode hit counts
    - `categories`: segment counts grouped by media category

    Stats are scoped by the query and category filters but are not narrowed by a selected media/episode
    — so selecting a media in the UI doesn't zero out other media from the list.

    Args:
        body (SearchStatsRequest): Stats request. All fields are optional — omit `query` to get
            filter counts for the full corpus.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error429 | Error500 | SearchStatsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SearchStatsRequest,
) -> Error400 | Error401 | Error403 | Error429 | Error500 | SearchStatsResponse | None:
    """Get search statistics

     Returns filter statistics for a query without returning segment results. Useful for populating
    filter UIs:
    - `media`: media matching the query, with per-episode hit counts
    - `categories`: segment counts grouped by media category

    Stats are scoped by the query and category filters but are not narrowed by a selected media/episode
    — so selecting a media in the UI doesn't zero out other media from the list.

    Args:
        body (SearchStatsRequest): Stats request. All fields are optional — omit `query` to get
            filter counts for the full corpus.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error403 | Error429 | Error500 | SearchStatsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
