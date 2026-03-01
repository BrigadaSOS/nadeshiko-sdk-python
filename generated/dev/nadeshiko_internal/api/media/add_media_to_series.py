from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_media_to_series_body import AddMediaToSeriesBody
from ...models.error_400 import Error400
from ...models.error_401 import Error401
from ...models.error_403 import Error403
from ...models.error_404 import Error404
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: AddMediaToSeriesBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/media/series/{id}/media".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Any | Error400 | Error401 | Error403 | Error404 | Error429 | Error500]:
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
    body: AddMediaToSeriesBody,
) -> Response[Any | Error400 | Error401 | Error403 | Error404 | Error429 | Error500]:
    """Add media to series

     Adds a media entry to a series at a specific position.

    **Permissions:** `UPDATE_MEDIA`

    Args:
        id (str):  Example: V1StGXR8_Z5d.
        body (AddMediaToSeriesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error400 | Error401 | Error403 | Error404 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: AddMediaToSeriesBody,
) -> Any | Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | None:
    """Add media to series

     Adds a media entry to a series at a specific position.

    **Permissions:** `UPDATE_MEDIA`

    Args:
        id (str):  Example: V1StGXR8_Z5d.
        body (AddMediaToSeriesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error400 | Error401 | Error403 | Error404 | Error429 | Error500
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: AddMediaToSeriesBody,
) -> Response[Any | Error400 | Error401 | Error403 | Error404 | Error429 | Error500]:
    """Add media to series

     Adds a media entry to a series at a specific position.

    **Permissions:** `UPDATE_MEDIA`

    Args:
        id (str):  Example: V1StGXR8_Z5d.
        body (AddMediaToSeriesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error400 | Error401 | Error403 | Error404 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: AddMediaToSeriesBody,
) -> Any | Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | None:
    """Add media to series

     Adds a media entry to a series at a specific position.

    **Permissions:** `UPDATE_MEDIA`

    Args:
        id (str):  Example: V1StGXR8_Z5d.
        body (AddMediaToSeriesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error400 | Error401 | Error403 | Error404 | Error429 | Error500
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
