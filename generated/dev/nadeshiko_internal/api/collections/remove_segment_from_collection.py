from http import HTTPStatus
from typing import Any, cast
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
from ...types import Response


def _get_kwargs(
    id: int,
    uuid: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/collections/{id}/segments/{uuid}".format(
            id=quote(str(id), safe=""),
            uuid=quote(str(uuid), safe=""),
        ),
    }

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
    id: int,
    uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | Error400 | Error401 | Error403 | Error404 | Error429 | Error500]:
    """Remove segment from collection

     Removes a segment from a collection. Requires collection ownership.

    Args:
        id (int):  Example: 123.
        uuid (str):  Example: 3fd94cef-a3e1-31ae-bc8d-e743f03e9c7e.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error400 | Error401 | Error403 | Error404 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        id=id,
        uuid=uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    uuid: str,
    *,
    client: AuthenticatedClient,
) -> Any | Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | None:
    """Remove segment from collection

     Removes a segment from a collection. Requires collection ownership.

    Args:
        id (int):  Example: 123.
        uuid (str):  Example: 3fd94cef-a3e1-31ae-bc8d-e743f03e9c7e.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error400 | Error401 | Error403 | Error404 | Error429 | Error500
    """

    return sync_detailed(
        id=id,
        uuid=uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | Error400 | Error401 | Error403 | Error404 | Error429 | Error500]:
    """Remove segment from collection

     Removes a segment from a collection. Requires collection ownership.

    Args:
        id (int):  Example: 123.
        uuid (str):  Example: 3fd94cef-a3e1-31ae-bc8d-e743f03e9c7e.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error400 | Error401 | Error403 | Error404 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        id=id,
        uuid=uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    uuid: str,
    *,
    client: AuthenticatedClient,
) -> Any | Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | None:
    """Remove segment from collection

     Removes a segment from a collection. Requires collection ownership.

    Args:
        id (int):  Example: 123.
        uuid (str):  Example: 3fd94cef-a3e1-31ae-bc8d-e743f03e9c7e.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error400 | Error401 | Error403 | Error404 | Error429 | Error500
    """

    return (
        await asyncio_detailed(
            id=id,
            uuid=uuid,
            client=client,
        )
    ).parsed
