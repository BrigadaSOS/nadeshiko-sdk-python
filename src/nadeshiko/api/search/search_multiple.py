from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.search_multiple_request import SearchMultipleRequest
from ...models.search_multiple_response import SearchMultipleResponse
from ...types import Response


def _get_kwargs(
    *,
    body: SearchMultipleRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/search/media/match/words",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | SearchMultipleResponse | None:
    if response.status_code == 200:
        response_200 = SearchMultipleResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | SearchMultipleResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchMultipleRequest,
) -> Response[Error | SearchMultipleResponse]:
    """Search by multiple queries

     Searches for multiple words simultaneously and aggregates results by media.

    Unlike the main search endpoint, this returns a summary of matches per media rather than individual
    sentence segments.

    **Use Cases**
    - Vocabulary discovery across media library
    - Finding anime/dramas that use specific words
    - Comparing word usage across different titles

    **Requirements:**
    - Required Scopes: `READ_MEDIA`

    Args:
        body (SearchMultipleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SearchMultipleResponse]
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
    client: AuthenticatedClient | Client,
    body: SearchMultipleRequest,
) -> Error | SearchMultipleResponse | None:
    """Search by multiple queries

     Searches for multiple words simultaneously and aggregates results by media.

    Unlike the main search endpoint, this returns a summary of matches per media rather than individual
    sentence segments.

    **Use Cases**
    - Vocabulary discovery across media library
    - Finding anime/dramas that use specific words
    - Comparing word usage across different titles

    **Requirements:**
    - Required Scopes: `READ_MEDIA`

    Args:
        body (SearchMultipleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SearchMultipleResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchMultipleRequest,
) -> Response[Error | SearchMultipleResponse]:
    """Search by multiple queries

     Searches for multiple words simultaneously and aggregates results by media.

    Unlike the main search endpoint, this returns a summary of matches per media rather than individual
    sentence segments.

    **Use Cases**
    - Vocabulary discovery across media library
    - Finding anime/dramas that use specific words
    - Comparing word usage across different titles

    **Requirements:**
    - Required Scopes: `READ_MEDIA`

    Args:
        body (SearchMultipleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SearchMultipleResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchMultipleRequest,
) -> Error | SearchMultipleResponse | None:
    """Search by multiple queries

     Searches for multiple words simultaneously and aggregates results by media.

    Unlike the main search endpoint, this returns a summary of matches per media rather than individual
    sentence segments.

    **Use Cases**
    - Vocabulary discovery across media library
    - Finding anime/dramas that use specific words
    - Comparing word usage across different titles

    **Requirements:**
    - Required Scopes: `READ_MEDIA`

    Args:
        body (SearchMultipleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SearchMultipleResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
