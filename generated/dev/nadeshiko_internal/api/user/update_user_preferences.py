from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_401 import Error401
from ...models.error_500 import Error500
from ...models.user_preferences import UserPreferences
from ...types import Response


def _get_kwargs(
    *,
    body: UserPreferences,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/user/preferences",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error401 | Error500 | UserPreferences | None:
    if response.status_code == 200:
        response_200 = UserPreferences.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error401.from_dict(response.json())

        return response_401

    if response.status_code == 500:
        response_500 = Error500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error401 | Error500 | UserPreferences]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UserPreferences,
) -> Response[Error401 | Error500 | UserPreferences]:
    """Update user preferences

     Deep-merges a partial preferences update into the user's existing preferences.
    Only the provided keys are updated; all other keys are preserved.

    **Permissions:** Session authentication (cookie-based).

    Args:
        body (UserPreferences):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error401 | Error500 | UserPreferences]
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
    body: UserPreferences,
) -> Error401 | Error500 | UserPreferences | None:
    """Update user preferences

     Deep-merges a partial preferences update into the user's existing preferences.
    Only the provided keys are updated; all other keys are preserved.

    **Permissions:** Session authentication (cookie-based).

    Args:
        body (UserPreferences):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error401 | Error500 | UserPreferences
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UserPreferences,
) -> Response[Error401 | Error500 | UserPreferences]:
    """Update user preferences

     Deep-merges a partial preferences update into the user's existing preferences.
    Only the provided keys are updated; all other keys are preserved.

    **Permissions:** Session authentication (cookie-based).

    Args:
        body (UserPreferences):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error401 | Error500 | UserPreferences]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UserPreferences,
) -> Error401 | Error500 | UserPreferences | None:
    """Update user preferences

     Deep-merges a partial preferences update into the user's existing preferences.
    Only the provided keys are updated; all other keys are preserved.

    **Permissions:** Session authentication (cookie-based).

    Args:
        body (UserPreferences):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error401 | Error500 | UserPreferences
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
