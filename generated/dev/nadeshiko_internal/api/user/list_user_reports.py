from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_401 import Error401
from ...models.error_500 import Error500
from ...models.list_user_reports_status import ListUserReportsStatus
from ...models.report_list_response import ReportListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 20,
    status: ListUserReportsStatus | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["limit"] = limit

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/user/reports",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error401 | Error500 | ReportListResponse | None:
    if response.status_code == 200:
        response_200 = ReportListResponse.from_dict(response.json())

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
) -> Response[Error401 | Error500 | ReportListResponse]:
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
    limit: int | Unset = 20,
    status: ListUserReportsStatus | Unset = UNSET,
) -> Response[Error401 | Error500 | ReportListResponse]:
    """List user's own reports

     Returns the authenticated user's submitted reports with cursor pagination.

    **Permissions:** Session authentication (cookie-based).

    Args:
        cursor (int | Unset):
        limit (int | Unset):  Default: 20.
        status (ListUserReportsStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error401 | Error500 | ReportListResponse]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        limit=limit,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 20,
    status: ListUserReportsStatus | Unset = UNSET,
) -> Error401 | Error500 | ReportListResponse | None:
    """List user's own reports

     Returns the authenticated user's submitted reports with cursor pagination.

    **Permissions:** Session authentication (cookie-based).

    Args:
        cursor (int | Unset):
        limit (int | Unset):  Default: 20.
        status (ListUserReportsStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error401 | Error500 | ReportListResponse
    """

    return sync_detailed(
        client=client,
        cursor=cursor,
        limit=limit,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 20,
    status: ListUserReportsStatus | Unset = UNSET,
) -> Response[Error401 | Error500 | ReportListResponse]:
    """List user's own reports

     Returns the authenticated user's submitted reports with cursor pagination.

    **Permissions:** Session authentication (cookie-based).

    Args:
        cursor (int | Unset):
        limit (int | Unset):  Default: 20.
        status (ListUserReportsStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error401 | Error500 | ReportListResponse]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        limit=limit,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 20,
    status: ListUserReportsStatus | Unset = UNSET,
) -> Error401 | Error500 | ReportListResponse | None:
    """List user's own reports

     Returns the authenticated user's submitted reports with cursor pagination.

    **Permissions:** Session authentication (cookie-based).

    Args:
        cursor (int | Unset):
        limit (int | Unset):  Default: 20.
        status (ListUserReportsStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error401 | Error500 | ReportListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            cursor=cursor,
            limit=limit,
            status=status,
        )
    ).parsed
