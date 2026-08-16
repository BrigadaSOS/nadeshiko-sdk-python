from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_user_api_key_body import CreateUserApiKeyBody
from ...models.create_user_api_key_response_201 import CreateUserApiKeyResponse201
from ...models.error_400 import Error400
from ...models.error_401 import Error401
from ...models.error_403 import Error403
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...types import Response


def _get_kwargs(
    *,
    body: CreateUserApiKeyBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/user/api-keys",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateUserApiKeyResponse201 | Error400 | Error401 | Error403 | Error429 | Error500 | None:
    if response.status_code == 201:
        response_201 = CreateUserApiKeyResponse201.from_dict(response.json())

        return response_201

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
) -> Response[CreateUserApiKeyResponse201 | Error400 | Error401 | Error403 | Error429 | Error500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateUserApiKeyBody,
) -> Response[CreateUserApiKeyResponse201 | Error400 | Error401 | Error403 | Error429 | Error500]:
    r"""Create an API key with chosen scopes

     Creates an API key for the signed-in reader, carrying exactly the scopes
    asked for.

    Use this rather than the better-auth `/v1/auth/api-key/create` endpoint
    whenever the key is going anywhere but your own code. That endpoint cannot
    take a scope list — the underlying plugin treats `permissions` as a
    server-only field and rejects any request that carries one — so keys made
    through it get the read-only default instead.

    **Scopes are the whole of a key's authority.** Nothing re-checks the owner's
    role when the key is used, so a key with `WRITE_PROFILE` can rewrite that
    account's profile from anywhere it ends up. Grant the narrowest set the
    consumer needs: a third-party search or dictionary tool wants
    `[\"READ_MEDIA\"]` and nothing else.

    Session-authenticated only. A key cannot be used to mint another key.

    Args:
        body (CreateUserApiKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateUserApiKeyResponse201 | Error400 | Error401 | Error403 | Error429 | Error500]
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
    body: CreateUserApiKeyBody,
) -> CreateUserApiKeyResponse201 | Error400 | Error401 | Error403 | Error429 | Error500 | None:
    r"""Create an API key with chosen scopes

     Creates an API key for the signed-in reader, carrying exactly the scopes
    asked for.

    Use this rather than the better-auth `/v1/auth/api-key/create` endpoint
    whenever the key is going anywhere but your own code. That endpoint cannot
    take a scope list — the underlying plugin treats `permissions` as a
    server-only field and rejects any request that carries one — so keys made
    through it get the read-only default instead.

    **Scopes are the whole of a key's authority.** Nothing re-checks the owner's
    role when the key is used, so a key with `WRITE_PROFILE` can rewrite that
    account's profile from anywhere it ends up. Grant the narrowest set the
    consumer needs: a third-party search or dictionary tool wants
    `[\"READ_MEDIA\"]` and nothing else.

    Session-authenticated only. A key cannot be used to mint another key.

    Args:
        body (CreateUserApiKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateUserApiKeyResponse201 | Error400 | Error401 | Error403 | Error429 | Error500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateUserApiKeyBody,
) -> Response[CreateUserApiKeyResponse201 | Error400 | Error401 | Error403 | Error429 | Error500]:
    r"""Create an API key with chosen scopes

     Creates an API key for the signed-in reader, carrying exactly the scopes
    asked for.

    Use this rather than the better-auth `/v1/auth/api-key/create` endpoint
    whenever the key is going anywhere but your own code. That endpoint cannot
    take a scope list — the underlying plugin treats `permissions` as a
    server-only field and rejects any request that carries one — so keys made
    through it get the read-only default instead.

    **Scopes are the whole of a key's authority.** Nothing re-checks the owner's
    role when the key is used, so a key with `WRITE_PROFILE` can rewrite that
    account's profile from anywhere it ends up. Grant the narrowest set the
    consumer needs: a third-party search or dictionary tool wants
    `[\"READ_MEDIA\"]` and nothing else.

    Session-authenticated only. A key cannot be used to mint another key.

    Args:
        body (CreateUserApiKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateUserApiKeyResponse201 | Error400 | Error401 | Error403 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateUserApiKeyBody,
) -> CreateUserApiKeyResponse201 | Error400 | Error401 | Error403 | Error429 | Error500 | None:
    r"""Create an API key with chosen scopes

     Creates an API key for the signed-in reader, carrying exactly the scopes
    asked for.

    Use this rather than the better-auth `/v1/auth/api-key/create` endpoint
    whenever the key is going anywhere but your own code. That endpoint cannot
    take a scope list — the underlying plugin treats `permissions` as a
    server-only field and rejects any request that carries one — so keys made
    through it get the read-only default instead.

    **Scopes are the whole of a key's authority.** Nothing re-checks the owner's
    role when the key is used, so a key with `WRITE_PROFILE` can rewrite that
    account's profile from anywhere it ends up. Grant the narrowest set the
    consumer needs: a third-party search or dictionary tool wants
    `[\"READ_MEDIA\"]` and nothing else.

    Session-authenticated only. A key cannot be used to mint another key.

    Args:
        body (CreateUserApiKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateUserApiKeyResponse201 | Error400 | Error401 | Error403 | Error429 | Error500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
