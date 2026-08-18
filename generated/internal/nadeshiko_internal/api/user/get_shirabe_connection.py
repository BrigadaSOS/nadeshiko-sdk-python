from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_401 import Error401
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...models.get_shirabe_connection_response_200 import GetShirabeConnectionResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/user/connections/shirabe",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error401 | Error429 | Error500 | GetShirabeConnectionResponse200 | None:
    if response.status_code == 200:
        response_200 = GetShirabeConnectionResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error401.from_dict(response.json())

        return response_401

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
) -> Response[Error401 | Error429 | Error500 | GetShirabeConnectionResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Error401 | Error429 | Error500 | GetShirabeConnectionResponse200]:
    """Read the linked Shirabe account

     Whether the signed-in reader has linked a Shirabe account, and what it is
    shaped like: who they are over there, which dictionaries their stack names,
    and when we last re-read it.

    Never returns the stored key. Nothing the browser is shown can be used to
    act on their Shirabe account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error401 | Error429 | Error500 | GetShirabeConnectionResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Error401 | Error429 | Error500 | GetShirabeConnectionResponse200 | None:
    """Read the linked Shirabe account

     Whether the signed-in reader has linked a Shirabe account, and what it is
    shaped like: who they are over there, which dictionaries their stack names,
    and when we last re-read it.

    Never returns the stored key. Nothing the browser is shown can be used to
    act on their Shirabe account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error401 | Error429 | Error500 | GetShirabeConnectionResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Error401 | Error429 | Error500 | GetShirabeConnectionResponse200]:
    """Read the linked Shirabe account

     Whether the signed-in reader has linked a Shirabe account, and what it is
    shaped like: who they are over there, which dictionaries their stack names,
    and when we last re-read it.

    Never returns the stored key. Nothing the browser is shown can be used to
    act on their Shirabe account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error401 | Error429 | Error500 | GetShirabeConnectionResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Error401 | Error429 | Error500 | GetShirabeConnectionResponse200 | None:
    """Read the linked Shirabe account

     Whether the signed-in reader has linked a Shirabe account, and what it is
    shaped like: who they are over there, which dictionaries their stack names,
    and when we last re-read it.

    Never returns the stored key. Nothing the browser is shown can be used to
    act on their Shirabe account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error401 | Error429 | Error500 | GetShirabeConnectionResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
