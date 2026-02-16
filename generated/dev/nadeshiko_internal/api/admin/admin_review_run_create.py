from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.admin_review_run_create_category import AdminReviewRunCreateCategory
from ...models.error_401 import Error401
from ...models.error_403 import Error403
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...models.run_review_response import RunReviewResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    category: AdminReviewRunCreateCategory | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_category: str | Unset = UNSET
    if not isinstance(category, Unset):
        json_category = category.value

    params["category"] = json_category

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/admin/review/run",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error401 | Error403 | Error429 | Error500 | RunReviewResponse | None:
    if response.status_code == 200:
        response_200 = RunReviewResponse.from_dict(response.json())

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
) -> Response[Error401 | Error403 | Error429 | Error500 | RunReviewResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    category: AdminReviewRunCreateCategory | Unset = UNSET,
) -> Response[Error401 | Error403 | Error429 | Error500 | RunReviewResponse]:
    """Run auto-checks

     Triggers all enabled auto-checks. Creates ReviewCheckRun records and AUTO reports for any findings.

    **Permissions:** `ADD_MEDIA`

    Args:
        category (AdminReviewRunCreateCategory | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error401 | Error403 | Error429 | Error500 | RunReviewResponse]
    """

    kwargs = _get_kwargs(
        category=category,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    category: AdminReviewRunCreateCategory | Unset = UNSET,
) -> Error401 | Error403 | Error429 | Error500 | RunReviewResponse | None:
    """Run auto-checks

     Triggers all enabled auto-checks. Creates ReviewCheckRun records and AUTO reports for any findings.

    **Permissions:** `ADD_MEDIA`

    Args:
        category (AdminReviewRunCreateCategory | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error401 | Error403 | Error429 | Error500 | RunReviewResponse
    """

    return sync_detailed(
        client=client,
        category=category,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    category: AdminReviewRunCreateCategory | Unset = UNSET,
) -> Response[Error401 | Error403 | Error429 | Error500 | RunReviewResponse]:
    """Run auto-checks

     Triggers all enabled auto-checks. Creates ReviewCheckRun records and AUTO reports for any findings.

    **Permissions:** `ADD_MEDIA`

    Args:
        category (AdminReviewRunCreateCategory | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error401 | Error403 | Error429 | Error500 | RunReviewResponse]
    """

    kwargs = _get_kwargs(
        category=category,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    category: AdminReviewRunCreateCategory | Unset = UNSET,
) -> Error401 | Error403 | Error429 | Error500 | RunReviewResponse | None:
    """Run auto-checks

     Triggers all enabled auto-checks. Creates ReviewCheckRun records and AUTO reports for any findings.

    **Permissions:** `ADD_MEDIA`

    Args:
        category (AdminReviewRunCreateCategory | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error401 | Error403 | Error429 | Error500 | RunReviewResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            category=category,
        )
    ).parsed
