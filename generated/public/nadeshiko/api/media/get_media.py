from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400 import Error400
from ...models.error_401 import Error401
from ...models.error_403 import Error403
from ...models.error_404 import Error404
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...models.media import Media
from ...models.media_include_expansion import MediaIncludeExpansion
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    include: list[MediaIncludeExpansion] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_include: list[str] | Unset = UNSET
    if not isinstance(include, Unset):
        json_include = []
        for include_item_data in include:
            include_item = include_item_data.value
            json_include.append(include_item)

    params["include"] = json_include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/media/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | Media | None:
    if response.status_code == 200:
        response_200 = Media.from_dict(response.json())

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
) -> Response[Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | Media]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    include: list[MediaIncludeExpansion] | Unset = UNSET,
) -> Response[Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | Media]:
    """Get single media

     Returns a single media entry by its ID with full metadata.

    **Permissions:** `READ_MEDIA`

    Args:
        id (str):  Example: V1StGXR8_Z5d.
        include (list[MediaIncludeExpansion] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | Media]
    """

    kwargs = _get_kwargs(
        id=id,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    include: list[MediaIncludeExpansion] | Unset = UNSET,
) -> Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | Media | None:
    """Get single media

     Returns a single media entry by its ID with full metadata.

    **Permissions:** `READ_MEDIA`

    Args:
        id (str):  Example: V1StGXR8_Z5d.
        include (list[MediaIncludeExpansion] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | Media
    """

    return sync_detailed(
        id=id,
        client=client,
        include=include,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    include: list[MediaIncludeExpansion] | Unset = UNSET,
) -> Response[Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | Media]:
    """Get single media

     Returns a single media entry by its ID with full metadata.

    **Permissions:** `READ_MEDIA`

    Args:
        id (str):  Example: V1StGXR8_Z5d.
        include (list[MediaIncludeExpansion] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | Media]
    """

    kwargs = _get_kwargs(
        id=id,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    include: list[MediaIncludeExpansion] | Unset = UNSET,
) -> Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | Media | None:
    """Get single media

     Returns a single media entry by its ID with full metadata.

    **Permissions:** `READ_MEDIA`

    Args:
        id (str):  Example: V1StGXR8_Z5d.
        include (list[MediaIncludeExpansion] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | Media
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            include=include,
        )
    ).parsed
