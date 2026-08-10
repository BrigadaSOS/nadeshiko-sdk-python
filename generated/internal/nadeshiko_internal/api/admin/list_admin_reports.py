from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.admin_report_list_response import AdminReportListResponse
from ...models.error_401 import Error401
from ...models.error_403 import Error403
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...models.report_source import ReportSource
from ...models.report_target_type import ReportTargetType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cursor: str | Unset = UNSET,
    take: int | Unset = 20,
    status: str | Unset = UNSET,
    source: ReportSource | Unset = UNSET,
    target_type: ReportTargetType | Unset = UNSET,
    target_media_id: int | Unset = UNSET,
    target_episode_number: int | Unset = UNSET,
    target_segment_id: int | Unset = UNSET,
    orphaned: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["take"] = take

    params["status"] = status

    json_source: str | Unset = UNSET
    if not isinstance(source, Unset):
        json_source = source

    params["source"] = json_source

    json_target_type: str | Unset = UNSET
    if not isinstance(target_type, Unset):
        json_target_type = target_type

    params["target.type"] = json_target_type

    params["target.mediaId"] = target_media_id

    params["target.episodeNumber"] = target_episode_number

    params["target.segmentId"] = target_segment_id

    params["orphaned"] = orphaned

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/admin/reports",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AdminReportListResponse | Error401 | Error403 | Error429 | Error500 | None:
    if response.status_code == 200:
        response_200 = AdminReportListResponse.from_dict(response.json())

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
) -> Response[AdminReportListResponse | Error401 | Error403 | Error429 | Error500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    take: int | Unset = 20,
    status: str | Unset = UNSET,
    source: ReportSource | Unset = UNSET,
    target_type: ReportTargetType | Unset = UNSET,
    target_media_id: int | Unset = UNSET,
    target_episode_number: int | Unset = UNSET,
    target_segment_id: int | Unset = UNSET,
    orphaned: bool | Unset = UNSET,
) -> Response[AdminReportListResponse | Error401 | Error403 | Error429 | Error500]:
    """List all reports

     Returns all reports with filtering and cursor pagination.
    Supports filtering by source (USER/AUTO) to separate user reports from auto-check findings.

    Args:
        cursor (str | Unset):
        take (int | Unset):  Default: 20.
        status (str | Unset):
        source (ReportSource | Unset): Origin of the report Example: USER.
        target_type (ReportTargetType | Unset): Kind of entity a report is about Example: SEGMENT.
        target_media_id (int | Unset):
        target_episode_number (int | Unset):
        target_segment_id (int | Unset):
        orphaned (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminReportListResponse | Error401 | Error403 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        take=take,
        status=status,
        source=source,
        target_type=target_type,
        target_media_id=target_media_id,
        target_episode_number=target_episode_number,
        target_segment_id=target_segment_id,
        orphaned=orphaned,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    take: int | Unset = 20,
    status: str | Unset = UNSET,
    source: ReportSource | Unset = UNSET,
    target_type: ReportTargetType | Unset = UNSET,
    target_media_id: int | Unset = UNSET,
    target_episode_number: int | Unset = UNSET,
    target_segment_id: int | Unset = UNSET,
    orphaned: bool | Unset = UNSET,
) -> AdminReportListResponse | Error401 | Error403 | Error429 | Error500 | None:
    """List all reports

     Returns all reports with filtering and cursor pagination.
    Supports filtering by source (USER/AUTO) to separate user reports from auto-check findings.

    Args:
        cursor (str | Unset):
        take (int | Unset):  Default: 20.
        status (str | Unset):
        source (ReportSource | Unset): Origin of the report Example: USER.
        target_type (ReportTargetType | Unset): Kind of entity a report is about Example: SEGMENT.
        target_media_id (int | Unset):
        target_episode_number (int | Unset):
        target_segment_id (int | Unset):
        orphaned (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminReportListResponse | Error401 | Error403 | Error429 | Error500
    """

    return sync_detailed(
        client=client,
        cursor=cursor,
        take=take,
        status=status,
        source=source,
        target_type=target_type,
        target_media_id=target_media_id,
        target_episode_number=target_episode_number,
        target_segment_id=target_segment_id,
        orphaned=orphaned,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    take: int | Unset = 20,
    status: str | Unset = UNSET,
    source: ReportSource | Unset = UNSET,
    target_type: ReportTargetType | Unset = UNSET,
    target_media_id: int | Unset = UNSET,
    target_episode_number: int | Unset = UNSET,
    target_segment_id: int | Unset = UNSET,
    orphaned: bool | Unset = UNSET,
) -> Response[AdminReportListResponse | Error401 | Error403 | Error429 | Error500]:
    """List all reports

     Returns all reports with filtering and cursor pagination.
    Supports filtering by source (USER/AUTO) to separate user reports from auto-check findings.

    Args:
        cursor (str | Unset):
        take (int | Unset):  Default: 20.
        status (str | Unset):
        source (ReportSource | Unset): Origin of the report Example: USER.
        target_type (ReportTargetType | Unset): Kind of entity a report is about Example: SEGMENT.
        target_media_id (int | Unset):
        target_episode_number (int | Unset):
        target_segment_id (int | Unset):
        orphaned (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminReportListResponse | Error401 | Error403 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        take=take,
        status=status,
        source=source,
        target_type=target_type,
        target_media_id=target_media_id,
        target_episode_number=target_episode_number,
        target_segment_id=target_segment_id,
        orphaned=orphaned,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    take: int | Unset = 20,
    status: str | Unset = UNSET,
    source: ReportSource | Unset = UNSET,
    target_type: ReportTargetType | Unset = UNSET,
    target_media_id: int | Unset = UNSET,
    target_episode_number: int | Unset = UNSET,
    target_segment_id: int | Unset = UNSET,
    orphaned: bool | Unset = UNSET,
) -> AdminReportListResponse | Error401 | Error403 | Error429 | Error500 | None:
    """List all reports

     Returns all reports with filtering and cursor pagination.
    Supports filtering by source (USER/AUTO) to separate user reports from auto-check findings.

    Args:
        cursor (str | Unset):
        take (int | Unset):  Default: 20.
        status (str | Unset):
        source (ReportSource | Unset): Origin of the report Example: USER.
        target_type (ReportTargetType | Unset): Kind of entity a report is about Example: SEGMENT.
        target_media_id (int | Unset):
        target_episode_number (int | Unset):
        target_segment_id (int | Unset):
        orphaned (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminReportListResponse | Error401 | Error403 | Error429 | Error500
    """

    return (
        await asyncio_detailed(
            client=client,
            cursor=cursor,
            take=take,
            status=status,
            source=source,
            target_type=target_type,
            target_media_id=target_media_id,
            target_episode_number=target_episode_number,
            target_segment_id=target_segment_id,
            orphaned=orphaned,
        )
    ).parsed
