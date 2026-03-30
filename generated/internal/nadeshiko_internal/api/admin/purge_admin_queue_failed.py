from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400 import Error400
from ...models.error_401 import Error401
from ...models.error_403 import Error403
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...models.purge_admin_queue_failed_queue_name import PurgeAdminQueueFailedQueueName
from ...models.purge_admin_queue_failed_response_200 import PurgeAdminQueueFailedResponse200
from ...types import Response


def _get_kwargs(
    queue_name: PurgeAdminQueueFailedQueueName,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/admin/queues/{queue_name}/purge".format(
            queue_name=quote(str(queue_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error400 | Error401 | Error403 | Error429 | Error500 | PurgeAdminQueueFailedResponse200 | None:
    if response.status_code == 200:
        response_200 = PurgeAdminQueueFailedResponse200.from_dict(response.json())

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
) -> Response[
    Error400 | Error401 | Error403 | Error429 | Error500 | PurgeAdminQueueFailedResponse200
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    queue_name: PurgeAdminQueueFailedQueueName,
    *,
    client: AuthenticatedClient,
) -> Response[
    Error400 | Error401 | Error403 | Error429 | Error500 | PurgeAdminQueueFailedResponse200
]:
    """Purge failed jobs from a queue

     Permanently deletes all failed jobs from a queue.
    This does **not** re-sync the affected segments -- use the reindex endpoint for that.

    Args:
        queue_name (PurgeAdminQueueFailedQueueName):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error429 | Error500 | PurgeAdminQueueFailedResponse200]
    """

    kwargs = _get_kwargs(
        queue_name=queue_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    queue_name: PurgeAdminQueueFailedQueueName,
    *,
    client: AuthenticatedClient,
) -> Error400 | Error401 | Error403 | Error429 | Error500 | PurgeAdminQueueFailedResponse200 | None:
    """Purge failed jobs from a queue

     Permanently deletes all failed jobs from a queue.
    This does **not** re-sync the affected segments -- use the reindex endpoint for that.

    Args:
        queue_name (PurgeAdminQueueFailedQueueName):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error403 | Error429 | Error500 | PurgeAdminQueueFailedResponse200
    """

    return sync_detailed(
        queue_name=queue_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    queue_name: PurgeAdminQueueFailedQueueName,
    *,
    client: AuthenticatedClient,
) -> Response[
    Error400 | Error401 | Error403 | Error429 | Error500 | PurgeAdminQueueFailedResponse200
]:
    """Purge failed jobs from a queue

     Permanently deletes all failed jobs from a queue.
    This does **not** re-sync the affected segments -- use the reindex endpoint for that.

    Args:
        queue_name (PurgeAdminQueueFailedQueueName):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error429 | Error500 | PurgeAdminQueueFailedResponse200]
    """

    kwargs = _get_kwargs(
        queue_name=queue_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    queue_name: PurgeAdminQueueFailedQueueName,
    *,
    client: AuthenticatedClient,
) -> Error400 | Error401 | Error403 | Error429 | Error500 | PurgeAdminQueueFailedResponse200 | None:
    """Purge failed jobs from a queue

     Permanently deletes all failed jobs from a queue.
    This does **not** re-sync the affected segments -- use the reindex endpoint for that.

    Args:
        queue_name (PurgeAdminQueueFailedQueueName):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error403 | Error429 | Error500 | PurgeAdminQueueFailedResponse200
    """

    return (
        await asyncio_detailed(
            queue_name=queue_name,
            client=client,
        )
    ).parsed
