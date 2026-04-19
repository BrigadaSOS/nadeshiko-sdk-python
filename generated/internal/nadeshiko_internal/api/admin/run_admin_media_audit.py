from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_401 import Error401
from ...models.error_403 import Error403
from ...models.error_404 import Error404
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...models.run_admin_media_audit_category import (
    RunAdminMediaAuditCategory,
)
from ...models.run_audit_response import RunAuditResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    name: str,
    *,
    category: RunAdminMediaAuditCategory | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_category: str | Unset = UNSET
    if not isinstance(category, Unset):
        json_category = category

    params["category"] = json_category

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/admin/media/audits/{name}/run".format(
            name=quote(str(name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error401 | Error403 | Error404 | Error429 | Error500 | RunAuditResponse | None:
    if response.status_code == 200:
        response_200 = RunAuditResponse.from_dict(response.json())

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
) -> Response[Error401 | Error403 | Error404 | Error429 | Error500 | RunAuditResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    category: RunAdminMediaAuditCategory | Unset = UNSET,
) -> Response[Error401 | Error403 | Error404 | Error429 | Error500 | RunAuditResponse]:
    """Run media audit

     Triggers all enabled audits (or a specific one). Creates MediaAuditRun records and AUTO reports for
    any findings.

    Args:
        name (str):
        category (RunAdminMediaAuditCategory | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error401 | Error403 | Error404 | Error429 | Error500 | RunAuditResponse]
    """

    kwargs = _get_kwargs(
        name=name,
        category=category,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient,
    category: RunAdminMediaAuditCategory | Unset = UNSET,
) -> Error401 | Error403 | Error404 | Error429 | Error500 | RunAuditResponse | None:
    """Run media audit

     Triggers all enabled audits (or a specific one). Creates MediaAuditRun records and AUTO reports for
    any findings.

    Args:
        name (str):
        category (RunAdminMediaAuditCategory | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error401 | Error403 | Error404 | Error429 | Error500 | RunAuditResponse
    """

    return sync_detailed(
        name=name,
        client=client,
        category=category,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    category: RunAdminMediaAuditCategory | Unset = UNSET,
) -> Response[Error401 | Error403 | Error404 | Error429 | Error500 | RunAuditResponse]:
    """Run media audit

     Triggers all enabled audits (or a specific one). Creates MediaAuditRun records and AUTO reports for
    any findings.

    Args:
        name (str):
        category (RunAdminMediaAuditCategory | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error401 | Error403 | Error404 | Error429 | Error500 | RunAuditResponse]
    """

    kwargs = _get_kwargs(
        name=name,
        category=category,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient,
    category: RunAdminMediaAuditCategory | Unset = UNSET,
) -> Error401 | Error403 | Error404 | Error429 | Error500 | RunAuditResponse | None:
    """Run media audit

     Triggers all enabled audits (or a specific one). Creates MediaAuditRun records and AUTO reports for
    any findings.

    Args:
        name (str):
        category (RunAdminMediaAuditCategory | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error401 | Error403 | Error404 | Error429 | Error500 | RunAuditResponse
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            category=category,
        )
    ).parsed
