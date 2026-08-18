from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_401 import Error401
from ...models.error_403 import Error403
from ...models.error_404 import Error404
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...models.get_shirabe_credential_response_200 import GetShirabeCredentialResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/user/connections/shirabe/credential",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error401 | Error403 | Error404 | Error429 | Error500 | GetShirabeCredentialResponse200 | None:
    if response.status_code == 200:
        response_200 = GetShirabeCredentialResponse200.from_dict(response.json())

        return response_200

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
) -> Response[
    Error401 | Error403 | Error404 | Error429 | Error500 | GetShirabeCredentialResponse200
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    Error401 | Error403 | Error404 | Error429 | Error500 | GetShirabeCredentialResponse200
]:
    """The reader's Shirabe key, for our own server only

     Hands the stored Shirabe key to our frontend server so a word lookup can be
    made AS the reader, which is the entire point of linking an account.

    Refused unless the request came through our own Nitro proxy (the shared
    internal secret). A session alone is not enough, even the reader's own: a key
    that reaches a browser is a key that has been given away, and this one is a
    live credential on somebody else's service. The reader has no need for it
    here — it is already listed, and revocable, on their Shirabe account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error401 | Error403 | Error404 | Error429 | Error500 | GetShirabeCredentialResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Error401 | Error403 | Error404 | Error429 | Error500 | GetShirabeCredentialResponse200 | None:
    """The reader's Shirabe key, for our own server only

     Hands the stored Shirabe key to our frontend server so a word lookup can be
    made AS the reader, which is the entire point of linking an account.

    Refused unless the request came through our own Nitro proxy (the shared
    internal secret). A session alone is not enough, even the reader's own: a key
    that reaches a browser is a key that has been given away, and this one is a
    live credential on somebody else's service. The reader has no need for it
    here — it is already listed, and revocable, on their Shirabe account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error401 | Error403 | Error404 | Error429 | Error500 | GetShirabeCredentialResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    Error401 | Error403 | Error404 | Error429 | Error500 | GetShirabeCredentialResponse200
]:
    """The reader's Shirabe key, for our own server only

     Hands the stored Shirabe key to our frontend server so a word lookup can be
    made AS the reader, which is the entire point of linking an account.

    Refused unless the request came through our own Nitro proxy (the shared
    internal secret). A session alone is not enough, even the reader's own: a key
    that reaches a browser is a key that has been given away, and this one is a
    live credential on somebody else's service. The reader has no need for it
    here — it is already listed, and revocable, on their Shirabe account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error401 | Error403 | Error404 | Error429 | Error500 | GetShirabeCredentialResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Error401 | Error403 | Error404 | Error429 | Error500 | GetShirabeCredentialResponse200 | None:
    """The reader's Shirabe key, for our own server only

     Hands the stored Shirabe key to our frontend server so a word lookup can be
    made AS the reader, which is the entire point of linking an account.

    Refused unless the request came through our own Nitro proxy (the shared
    internal secret). A session alone is not enough, even the reader's own: a key
    that reaches a browser is a key that has been given away, and this one is a
    live credential on somebody else's service. The reader has no need for it
    here — it is already listed, and revocable, on their Shirabe account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error401 | Error403 | Error404 | Error429 | Error500 | GetShirabeCredentialResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
