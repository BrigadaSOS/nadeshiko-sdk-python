import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_user_activity_by_date_response_200 import DeleteUserActivityByDateResponse200
from ...models.error_401 import Error401
from ...models.error_500 import Error500
from ...types import Response


def _get_kwargs(
    date: datetime.date,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/user/activity/date/{date}".format(
            date=quote(str(date), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteUserActivityByDateResponse200 | Error401 | Error500 | None:
    if response.status_code == 200:
        response_200 = DeleteUserActivityByDateResponse200.from_dict(response.json())

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
) -> Response[DeleteUserActivityByDateResponse200 | Error401 | Error500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    date: datetime.date,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteUserActivityByDateResponse200 | Error401 | Error500]:
    """Delete all activity for a specific date

     Deletes all activity records for the authenticated user on the given date.

    **Permissions:** Session authentication (cookie-based).

    Args:
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteUserActivityByDateResponse200 | Error401 | Error500]
    """

    kwargs = _get_kwargs(
        date=date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    date: datetime.date,
    *,
    client: AuthenticatedClient,
) -> DeleteUserActivityByDateResponse200 | Error401 | Error500 | None:
    """Delete all activity for a specific date

     Deletes all activity records for the authenticated user on the given date.

    **Permissions:** Session authentication (cookie-based).

    Args:
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteUserActivityByDateResponse200 | Error401 | Error500
    """

    return sync_detailed(
        date=date,
        client=client,
    ).parsed


async def asyncio_detailed(
    date: datetime.date,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteUserActivityByDateResponse200 | Error401 | Error500]:
    """Delete all activity for a specific date

     Deletes all activity records for the authenticated user on the given date.

    **Permissions:** Session authentication (cookie-based).

    Args:
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteUserActivityByDateResponse200 | Error401 | Error500]
    """

    kwargs = _get_kwargs(
        date=date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    date: datetime.date,
    *,
    client: AuthenticatedClient,
) -> DeleteUserActivityByDateResponse200 | Error401 | Error500 | None:
    """Delete all activity for a specific date

     Deletes all activity records for the authenticated user on the given date.

    **Permissions:** Session authentication (cookie-based).

    Args:
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteUserActivityByDateResponse200 | Error401 | Error500
    """

    return (
        await asyncio_detailed(
            date=date,
            client=client,
        )
    ).parsed
