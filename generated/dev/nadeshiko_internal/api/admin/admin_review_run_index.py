from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.admin_review_run_index_response_200 import AdminReviewRunIndexResponse200
from ...models.error_401 import Error401
from ...models.error_403 import Error403
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    check_name: str | Unset = UNSET,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["checkName"] = check_name

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/admin/review/runs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AdminReviewRunIndexResponse200 | Error401 | Error403 | Error429 | Error500 | None:
    if response.status_code == 200:
        response_200 = AdminReviewRunIndexResponse200.from_dict(response.json())

        return response_200

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
) -> Response[AdminReviewRunIndexResponse200 | Error401 | Error403 | Error429 | Error500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    check_name: str | Unset = UNSET,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 20,
) -> Response[AdminReviewRunIndexResponse200 | Error401 | Error403 | Error429 | Error500]:
    """List past check runs

     Returns past review check runs with summary stats. Supports filtering by check name and cursor
    pagination.

    **Permissions:** `ADD_MEDIA`

    Args:
        check_name (str | Unset):
        cursor (int | Unset):
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminReviewRunIndexResponse200 | Error401 | Error403 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        check_name=check_name,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    check_name: str | Unset = UNSET,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 20,
) -> AdminReviewRunIndexResponse200 | Error401 | Error403 | Error429 | Error500 | None:
    """List past check runs

     Returns past review check runs with summary stats. Supports filtering by check name and cursor
    pagination.

    **Permissions:** `ADD_MEDIA`

    Args:
        check_name (str | Unset):
        cursor (int | Unset):
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminReviewRunIndexResponse200 | Error401 | Error403 | Error429 | Error500
    """

    return sync_detailed(
        client=client,
        check_name=check_name,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    check_name: str | Unset = UNSET,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 20,
) -> Response[AdminReviewRunIndexResponse200 | Error401 | Error403 | Error429 | Error500]:
    """List past check runs

     Returns past review check runs with summary stats. Supports filtering by check name and cursor
    pagination.

    **Permissions:** `ADD_MEDIA`

    Args:
        check_name (str | Unset):
        cursor (int | Unset):
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminReviewRunIndexResponse200 | Error401 | Error403 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        check_name=check_name,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    check_name: str | Unset = UNSET,
    cursor: int | Unset = UNSET,
    limit: int | Unset = 20,
) -> AdminReviewRunIndexResponse200 | Error401 | Error403 | Error429 | Error500 | None:
    """List past check runs

     Returns past review check runs with summary stats. Supports filtering by check name and cursor
    pagination.

    **Permissions:** `ADD_MEDIA`

    Args:
        check_name (str | Unset):
        cursor (int | Unset):
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminReviewRunIndexResponse200 | Error401 | Error403 | Error429 | Error500
    """

    return (
        await asyncio_detailed(
            client=client,
            check_name=check_name,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
