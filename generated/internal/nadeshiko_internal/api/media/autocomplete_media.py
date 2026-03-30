from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.autocomplete_media_category import AutocompleteMediaCategory
from ...models.error_400 import Error400
from ...models.error_401 import Error401
from ...models.error_403 import Error403
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...models.media_autocomplete_response import MediaAutocompleteResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: str,
    take: int | Unset = 10,
    category: AutocompleteMediaCategory | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["query"] = query

    params["take"] = take

    json_category: str | Unset = UNSET
    if not isinstance(category, Unset):
        json_category = category.value

    params["category"] = json_category

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/media/autocomplete",
        "params": params,
    }

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
    query: str,
    take: int | Unset = 10,
    category: AutocompleteMediaCategory | Unset = UNSET,
) -> Response[Error400 | Error401 | Error403 | Error429 | Error500 | MediaAutocompleteResponse]:
    """Autocomplete media by name

     Returns a short list of media matching a name prefix or substring.
    Results are ranked by exact match, then prefix match, then contains match,
    and further sorted by name length.

    Args:
        query (str):  Example: steins.
        take (int | Unset):  Default: 10.
        category (AutocompleteMediaCategory | Unset):  Example: ANIME.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error429 | Error500 | MediaAutocompleteResponse]
    """

    kwargs = _get_kwargs(
        query=query,
        take=take,
        category=category,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    query: str,
    take: int | Unset = 10,
    category: AutocompleteMediaCategory | Unset = UNSET,
) -> Error400 | Error401 | Error403 | Error429 | Error500 | MediaAutocompleteResponse | None:
    """Autocomplete media by name

     Returns a short list of media matching a name prefix or substring.
    Results are ranked by exact match, then prefix match, then contains match,
    and further sorted by name length.

    Args:
        query (str):  Example: steins.
        take (int | Unset):  Default: 10.
        category (AutocompleteMediaCategory | Unset):  Example: ANIME.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error403 | Error429 | Error500 | MediaAutocompleteResponse
    """

    return sync_detailed(
        client=client,
        query=query,
        take=take,
        category=category,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    query: str,
    take: int | Unset = 10,
    category: AutocompleteMediaCategory | Unset = UNSET,
) -> Response[Error400 | Error401 | Error403 | Error429 | Error500 | MediaAutocompleteResponse]:
    """Autocomplete media by name

     Returns a short list of media matching a name prefix or substring.
    Results are ranked by exact match, then prefix match, then contains match,
    and further sorted by name length.

    Args:
        query (str):  Example: steins.
        take (int | Unset):  Default: 10.
        category (AutocompleteMediaCategory | Unset):  Example: ANIME.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error429 | Error500 | MediaAutocompleteResponse]
    """

    kwargs = _get_kwargs(
        query=query,
        take=take,
        category=category,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    query: str,
    take: int | Unset = 10,
    category: AutocompleteMediaCategory | Unset = UNSET,
) -> Error400 | Error401 | Error403 | Error429 | Error500 | MediaAutocompleteResponse | None:
    """Autocomplete media by name

     Returns a short list of media matching a name prefix or substring.
    Results are ranked by exact match, then prefix match, then contains match,
    and further sorted by name length.

    Args:
        query (str):  Example: steins.
        take (int | Unset):  Default: 10.
        category (AutocompleteMediaCategory | Unset):  Example: ANIME.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error403 | Error429 | Error500 | MediaAutocompleteResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            take=take,
            category=category,
        )
    ).parsed
