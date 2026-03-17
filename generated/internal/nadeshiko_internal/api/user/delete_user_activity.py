from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activity_type import ActivityType
from ...models.delete_user_activity_response_200 import DeleteUserActivityResponse200
from ...models.error_401 import Error401
from ...models.error_500 import Error500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    activity_type: ActivityType | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_activity_type: str | Unset = UNSET
    if not isinstance(activity_type, Unset):
        json_activity_type = activity_type.value

    params["activityType"] = json_activity_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/user/activity",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteUserActivityResponse200 | Error401 | Error500 | None:
    if response.status_code == 200:
        response_200 = DeleteUserActivityResponse200.from_dict(response.json())

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
) -> Response[DeleteUserActivityResponse200 | Error401 | Error500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    activity_type: ActivityType | Unset = UNSET,
) -> Response[DeleteUserActivityResponse200 | Error401 | Error500]:
    """Clear user activity history

     Deletes the authenticated user's activity history. Optionally filter by activity type.

    **Permissions:** Session authentication (cookie-based).

    Args:
        activity_type (ActivityType | Unset): Type of user activity

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteUserActivityResponse200 | Error401 | Error500]
    """

    kwargs = _get_kwargs(
        activity_type=activity_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    activity_type: ActivityType | Unset = UNSET,
) -> DeleteUserActivityResponse200 | Error401 | Error500 | None:
    """Clear user activity history

     Deletes the authenticated user's activity history. Optionally filter by activity type.

    **Permissions:** Session authentication (cookie-based).

    Args:
        activity_type (ActivityType | Unset): Type of user activity

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteUserActivityResponse200 | Error401 | Error500
    """

    return sync_detailed(
        client=client,
        activity_type=activity_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    activity_type: ActivityType | Unset = UNSET,
) -> Response[DeleteUserActivityResponse200 | Error401 | Error500]:
    """Clear user activity history

     Deletes the authenticated user's activity history. Optionally filter by activity type.

    **Permissions:** Session authentication (cookie-based).

    Args:
        activity_type (ActivityType | Unset): Type of user activity

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteUserActivityResponse200 | Error401 | Error500]
    """

    kwargs = _get_kwargs(
        activity_type=activity_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    activity_type: ActivityType | Unset = UNSET,
) -> DeleteUserActivityResponse200 | Error401 | Error500 | None:
    """Clear user activity history

     Deletes the authenticated user's activity history. Optionally filter by activity type.

    **Permissions:** Session authentication (cookie-based).

    Args:
        activity_type (ActivityType | Unset): Type of user activity

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteUserActivityResponse200 | Error401 | Error500
    """

    return (
        await asyncio_detailed(
            client=client,
            activity_type=activity_type,
        )
    ).parsed
