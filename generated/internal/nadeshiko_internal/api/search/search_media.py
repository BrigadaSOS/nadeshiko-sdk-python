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
from ...models.media_autocomplete_response import MediaAutocompleteResponse
from ...models.search_media_request import SearchMediaRequest
from ...types import Response


def _get_kwargs(
    *,
    body: SearchMediaRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/search/media",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error400 | Error401 | Error403 | Error429 | Error500 | MediaAutocompleteResponse | None:
    if response.status_code == 200:
        response_200 = MediaAutocompleteResponse.from_dict(response.json())

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
) -> Response[Error400 | Error401 | Error403 | Error429 | Error500 | MediaAutocompleteResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SearchMediaRequest,
) -> Response[Error400 | Error401 | Error403 | Error429 | Error500 | MediaAutocompleteResponse]:
    """Find media by name

     Returns a short list of media matching a name prefix or substring.
    Results are ranked by exact match, then prefix match, then contains match,
    and further sorted by name length.

    Args:
        body (SearchMediaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error429 | Error500 | MediaAutocompleteResponse]
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
    body: SearchMediaRequest,
) -> Error400 | Error401 | Error403 | Error429 | Error500 | MediaAutocompleteResponse | None:
    """Find media by name

     Returns a short list of media matching a name prefix or substring.
    Results are ranked by exact match, then prefix match, then contains match,
    and further sorted by name length.

    Args:
        body (SearchMediaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error403 | Error429 | Error500 | MediaAutocompleteResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SearchMediaRequest,
) -> Response[Error400 | Error401 | Error403 | Error429 | Error500 | MediaAutocompleteResponse]:
    """Find media by name

     Returns a short list of media matching a name prefix or substring.
    Results are ranked by exact match, then prefix match, then contains match,
    and further sorted by name length.

    Args:
        body (SearchMediaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error429 | Error500 | MediaAutocompleteResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SearchMediaRequest,
) -> Error400 | Error401 | Error403 | Error429 | Error500 | MediaAutocompleteResponse | None:
    """Find media by name

     Returns a short list of media matching a name prefix or substring.
    Results are ranked by exact match, then prefix match, then contains match,
    and further sorted by name length.

    Args:
        body (SearchMediaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error403 | Error429 | Error500 | MediaAutocompleteResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
