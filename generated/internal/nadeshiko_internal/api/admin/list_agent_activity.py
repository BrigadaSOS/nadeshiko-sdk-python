import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_activity_response import AgentActivityResponse
from ...models.error_400 import Error400
from ...models.error_401 import Error401
from ...models.error_403 import Error403
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    since: datetime.datetime | Unset = UNSET,
    report_id: int | Unset = UNSET,
    take: int | Unset = 100,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_since: str | Unset = UNSET
    if not isinstance(since, Unset):
        json_since = since.isoformat()
    params["since"] = json_since

    params["reportId"] = report_id

    params["take"] = take

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/admin/agent-activity",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentActivityResponse | Error400 | Error401 | Error403 | Error429 | Error500 | None:
    if response.status_code == 200:
        response_200 = AgentActivityResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error400.from_dict(response.json())

        return response_400

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
) -> Response[AgentActivityResponse | Error400 | Error401 | Error403 | Error429 | Error500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    since: datetime.datetime | Unset = UNSET,
    report_id: int | Unset = UNSET,
    take: int | Unset = 100,
) -> Response[AgentActivityResponse | Error400 | Error401 | Error403 | Error429 | Error500]:
    """List edits made by the moderation agent

     Returns segment revisions written under a service credential, newest first,
    joined to the segment they changed and the report they answered.

    This is the independent record of what the agent actually did. The agent's own
    Discord digest reports what it believes it did; this reports what landed in the
    database. Reading both is how a run that half-failed, or an action the agent
    did not mention, becomes visible.

    Each entry carries the pre-edit `snapshot`, so a bad edit can be reverted
    straight from here through the revision restore endpoint without going hunting
    for the revision number.

    Args:
        since (datetime.datetime | Unset):
        report_id (int | Unset):
        take (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentActivityResponse | Error400 | Error401 | Error403 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        since=since,
        report_id=report_id,
        take=take,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    since: datetime.datetime | Unset = UNSET,
    report_id: int | Unset = UNSET,
    take: int | Unset = 100,
) -> AgentActivityResponse | Error400 | Error401 | Error403 | Error429 | Error500 | None:
    """List edits made by the moderation agent

     Returns segment revisions written under a service credential, newest first,
    joined to the segment they changed and the report they answered.

    This is the independent record of what the agent actually did. The agent's own
    Discord digest reports what it believes it did; this reports what landed in the
    database. Reading both is how a run that half-failed, or an action the agent
    did not mention, becomes visible.

    Each entry carries the pre-edit `snapshot`, so a bad edit can be reverted
    straight from here through the revision restore endpoint without going hunting
    for the revision number.

    Args:
        since (datetime.datetime | Unset):
        report_id (int | Unset):
        take (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentActivityResponse | Error400 | Error401 | Error403 | Error429 | Error500
    """

    return sync_detailed(
        client=client,
        since=since,
        report_id=report_id,
        take=take,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    since: datetime.datetime | Unset = UNSET,
    report_id: int | Unset = UNSET,
    take: int | Unset = 100,
) -> Response[AgentActivityResponse | Error400 | Error401 | Error403 | Error429 | Error500]:
    """List edits made by the moderation agent

     Returns segment revisions written under a service credential, newest first,
    joined to the segment they changed and the report they answered.

    This is the independent record of what the agent actually did. The agent's own
    Discord digest reports what it believes it did; this reports what landed in the
    database. Reading both is how a run that half-failed, or an action the agent
    did not mention, becomes visible.

    Each entry carries the pre-edit `snapshot`, so a bad edit can be reverted
    straight from here through the revision restore endpoint without going hunting
    for the revision number.

    Args:
        since (datetime.datetime | Unset):
        report_id (int | Unset):
        take (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentActivityResponse | Error400 | Error401 | Error403 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        since=since,
        report_id=report_id,
        take=take,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    since: datetime.datetime | Unset = UNSET,
    report_id: int | Unset = UNSET,
    take: int | Unset = 100,
) -> AgentActivityResponse | Error400 | Error401 | Error403 | Error429 | Error500 | None:
    """List edits made by the moderation agent

     Returns segment revisions written under a service credential, newest first,
    joined to the segment they changed and the report they answered.

    This is the independent record of what the agent actually did. The agent's own
    Discord digest reports what it believes it did; this reports what landed in the
    database. Reading both is how a run that half-failed, or an action the agent
    did not mention, becomes visible.

    Each entry carries the pre-edit `snapshot`, so a bad edit can be reverted
    straight from here through the revision restore endpoint without going hunting
    for the revision number.

    Args:
        since (datetime.datetime | Unset):
        report_id (int | Unset):
        take (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentActivityResponse | Error400 | Error401 | Error403 | Error429 | Error500
    """

    return (
        await asyncio_detailed(
            client=client,
            since=since,
            report_id=report_id,
            take=take,
        )
    ).parsed
