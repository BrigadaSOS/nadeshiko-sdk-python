from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400 import Error400
from ...models.error_500 import Error500
from ...models.get_covered_words_filter import GetCoveredWordsFilter
from ...models.get_covered_words_response_200 import GetCoveredWordsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    tier: int,
    min_rank: int | Unset = 0,
    filter_: GetCoveredWordsFilter | Unset = GetCoveredWordsFilter.ALL,
    cursor: int | Unset = 0,
    take: int | Unset = 200,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["tier"] = tier

    params["minRank"] = min_rank

    json_filter_: str | Unset = UNSET
    if not isinstance(filter_, Unset):
        json_filter_ = filter_.value

    params["filter"] = json_filter_

    params["cursor"] = cursor

    params["take"] = take

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/stats/covered-words",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error400 | Error500 | GetCoveredWordsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetCoveredWordsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error400.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error400 | Error500 | GetCoveredWordsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    tier: int,
    min_rank: int | Unset = 0,
    filter_: GetCoveredWordsFilter | Unset = GetCoveredWordsFilter.ALL,
    cursor: int | Unset = 0,
    take: int | Unset = 200,
) -> Response[Error400 | Error500 | GetCoveredWordsResponse200]:
    """List words with coverage information

     Returns a paginated list of words from the frequency list within a given
    tier, with optional filtering by coverage status.

    Args:
        tier (int):
        min_rank (int | Unset):  Default: 0.
        filter_ (GetCoveredWordsFilter | Unset):  Default: GetCoveredWordsFilter.ALL.
        cursor (int | Unset):  Default: 0.
        take (int | Unset):  Default: 200.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error500 | GetCoveredWordsResponse200]
    """

    kwargs = _get_kwargs(
        tier=tier,
        min_rank=min_rank,
        filter_=filter_,
        cursor=cursor,
        take=take,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    tier: int,
    min_rank: int | Unset = 0,
    filter_: GetCoveredWordsFilter | Unset = GetCoveredWordsFilter.ALL,
    cursor: int | Unset = 0,
    take: int | Unset = 200,
) -> Error400 | Error500 | GetCoveredWordsResponse200 | None:
    """List words with coverage information

     Returns a paginated list of words from the frequency list within a given
    tier, with optional filtering by coverage status.

    Args:
        tier (int):
        min_rank (int | Unset):  Default: 0.
        filter_ (GetCoveredWordsFilter | Unset):  Default: GetCoveredWordsFilter.ALL.
        cursor (int | Unset):  Default: 0.
        take (int | Unset):  Default: 200.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error500 | GetCoveredWordsResponse200
    """

    return sync_detailed(
        client=client,
        tier=tier,
        min_rank=min_rank,
        filter_=filter_,
        cursor=cursor,
        take=take,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    tier: int,
    min_rank: int | Unset = 0,
    filter_: GetCoveredWordsFilter | Unset = GetCoveredWordsFilter.ALL,
    cursor: int | Unset = 0,
    take: int | Unset = 200,
) -> Response[Error400 | Error500 | GetCoveredWordsResponse200]:
    """List words with coverage information

     Returns a paginated list of words from the frequency list within a given
    tier, with optional filtering by coverage status.

    Args:
        tier (int):
        min_rank (int | Unset):  Default: 0.
        filter_ (GetCoveredWordsFilter | Unset):  Default: GetCoveredWordsFilter.ALL.
        cursor (int | Unset):  Default: 0.
        take (int | Unset):  Default: 200.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error500 | GetCoveredWordsResponse200]
    """

    kwargs = _get_kwargs(
        tier=tier,
        min_rank=min_rank,
        filter_=filter_,
        cursor=cursor,
        take=take,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    tier: int,
    min_rank: int | Unset = 0,
    filter_: GetCoveredWordsFilter | Unset = GetCoveredWordsFilter.ALL,
    cursor: int | Unset = 0,
    take: int | Unset = 200,
) -> Error400 | Error500 | GetCoveredWordsResponse200 | None:
    """List words with coverage information

     Returns a paginated list of words from the frequency list within a given
    tier, with optional filtering by coverage status.

    Args:
        tier (int):
        min_rank (int | Unset):  Default: 0.
        filter_ (GetCoveredWordsFilter | Unset):  Default: GetCoveredWordsFilter.ALL.
        cursor (int | Unset):  Default: 0.
        take (int | Unset):  Default: 200.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error500 | GetCoveredWordsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            tier=tier,
            min_rank=min_rank,
            filter_=filter_,
            cursor=cursor,
            take=take,
        )
    ).parsed
