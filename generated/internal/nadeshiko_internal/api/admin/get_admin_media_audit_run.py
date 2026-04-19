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
from ...models.get_admin_media_audit_run_response_200 import GetAdminMediaAuditRunResponse200
from ...types import Response


def _get_kwargs(
    audit_run_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/admin/media/audits/runs/{audit_run_id}".format(
            audit_run_id=quote(str(audit_run_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error401 | Error403 | Error404 | Error429 | Error500 | GetAdminMediaAuditRunResponse200 | None:
    if response.status_code == 200:
        response_200 = GetAdminMediaAuditRunResponse200.from_dict(response.json())

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
    Error401 | Error403 | Error404 | Error429 | Error500 | GetAdminMediaAuditRunResponse200
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    audit_run_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    Error401 | Error403 | Error404 | Error429 | Error500 | GetAdminMediaAuditRunResponse200
]:
    """Get audit run details

     Returns a specific media audit run record with its linked reports.

    Args:
        audit_run_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error401 | Error403 | Error404 | Error429 | Error500 | GetAdminMediaAuditRunResponse200]
    """

    kwargs = _get_kwargs(
        audit_run_id=audit_run_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    audit_run_id: int,
    *,
    client: AuthenticatedClient,
) -> Error401 | Error403 | Error404 | Error429 | Error500 | GetAdminMediaAuditRunResponse200 | None:
    """Get audit run details

     Returns a specific media audit run record with its linked reports.

    Args:
        audit_run_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error401 | Error403 | Error404 | Error429 | Error500 | GetAdminMediaAuditRunResponse200
    """

    return sync_detailed(
        audit_run_id=audit_run_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    audit_run_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    Error401 | Error403 | Error404 | Error429 | Error500 | GetAdminMediaAuditRunResponse200
]:
    """Get audit run details

     Returns a specific media audit run record with its linked reports.

    Args:
        audit_run_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error401 | Error403 | Error404 | Error429 | Error500 | GetAdminMediaAuditRunResponse200]
    """

    kwargs = _get_kwargs(
        audit_run_id=audit_run_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    audit_run_id: int,
    *,
    client: AuthenticatedClient,
) -> Error401 | Error403 | Error404 | Error429 | Error500 | GetAdminMediaAuditRunResponse200 | None:
    """Get audit run details

     Returns a specific media audit run record with its linked reports.

    Args:
        audit_run_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error401 | Error403 | Error404 | Error429 | Error500 | GetAdminMediaAuditRunResponse200
    """

    return (
        await asyncio_detailed(
            audit_run_id=audit_run_id,
            client=client,
        )
    ).parsed
