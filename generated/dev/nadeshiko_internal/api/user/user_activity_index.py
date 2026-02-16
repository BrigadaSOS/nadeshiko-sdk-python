from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activity_type import ActivityType
from ...models.error_401 import Error401
from ...models.error_500 import Error500
from ...models.user_activity_index_response_200 import UserActivityIndexResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cursor: int | Unset = UNSET,
    size: int | Unset = 20,
    activity_type: ActivityType | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["size"] = size

    json_activity_type: str | Unset = UNSET
    if not isinstance(activity_type, Unset):
        json_activity_type = activity_type.value

    params["activityType"] = json_activity_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/user/activity",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error401 | Error500 | UserActivityIndexResponse200 | None:
    if response.status_code == 200:
        response_200 = UserActivityIndexResponse200.from_dict(response.json())

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
) -> Response[Error401 | Error500 | UserActivityIndexResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    cursor: int | Unset = UNSET,
    size: int | Unset = 20,
    activity_type: ActivityType | Unset = UNSET,
) -> Response[Error401 | Error500 | UserActivityIndexResponse200]:
    """Get user activity history

     Returns the authenticated user's activity history with cursor-based pagination.

    **Permissions:** Session authentication (cookie-based).

    Args:
        cursor (int | Unset):
        size (int | Unset):  Default: 20.
        activity_type (ActivityType | Unset): Type of user activity

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error401 | Error500 | UserActivityIndexResponse200]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        size=size,
        activity_type=activity_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    cursor: int | Unset = UNSET,
    size: int | Unset = 20,
    activity_type: ActivityType | Unset = UNSET,
) -> Error401 | Error500 | UserActivityIndexResponse200 | None:
    """Get user activity history

     Returns the authenticated user's activity history with cursor-based pagination.

    **Permissions:** Session authentication (cookie-based).

    Args:
        cursor (int | Unset):
        size (int | Unset):  Default: 20.
        activity_type (ActivityType | Unset): Type of user activity

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error401 | Error500 | UserActivityIndexResponse200
    """

    return sync_detailed(
        client=client,
        cursor=cursor,
        size=size,
        activity_type=activity_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cursor: int | Unset = UNSET,
    size: int | Unset = 20,
    activity_type: ActivityType | Unset = UNSET,
) -> Response[Error401 | Error500 | UserActivityIndexResponse200]:
    """Get user activity history

     Returns the authenticated user's activity history with cursor-based pagination.

    **Permissions:** Session authentication (cookie-based).

    Args:
        cursor (int | Unset):
        size (int | Unset):  Default: 20.
        activity_type (ActivityType | Unset): Type of user activity

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error401 | Error500 | UserActivityIndexResponse200]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        size=size,
        activity_type=activity_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cursor: int | Unset = UNSET,
    size: int | Unset = 20,
    activity_type: ActivityType | Unset = UNSET,
) -> Error401 | Error500 | UserActivityIndexResponse200 | None:
    """Get user activity history

     Returns the authenticated user's activity history with cursor-based pagination.

    **Permissions:** Session authentication (cookie-based).

    Args:
        cursor (int | Unset):
        size (int | Unset):  Default: 20.
        activity_type (ActivityType | Unset): Type of user activity

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error401 | Error500 | UserActivityIndexResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            cursor=cursor,
            size=size,
            activity_type=activity_type,
        )
    ).parsed
