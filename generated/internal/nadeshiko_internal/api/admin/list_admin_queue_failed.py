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
from ...models.list_admin_queue_failed_queue_name import ListAdminQueueFailedQueueName
from ...models.list_admin_queue_failed_response_200_item import ListAdminQueueFailedResponse200Item
from ...types import Response


def _get_kwargs(
    queue_name: ListAdminQueueFailedQueueName,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/admin/queues/{queue_name}/failed".format(
            queue_name=quote(str(queue_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Error400
    | Error401
    | Error403
    | Error429
    | Error500
    | list[ListAdminQueueFailedResponse200Item]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ListAdminQueueFailedResponse200Item.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

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
    Error400 | Error401 | Error403 | Error429 | Error500 | list[ListAdminQueueFailedResponse200Item]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    queue_name: ListAdminQueueFailedQueueName,
    *,
    client: AuthenticatedClient,
) -> Response[
    Error400 | Error401 | Error403 | Error429 | Error500 | list[ListAdminQueueFailedResponse200Item]
]:
    """Get failed jobs from a queue

     Returns jobs that have exceeded their retry limit and permanently failed.

    Args:
        queue_name (ListAdminQueueFailedQueueName):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error429 | Error500 | list[ListAdminQueueFailedResponse200Item]]
    """

    kwargs = _get_kwargs(
        queue_name=queue_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    queue_name: ListAdminQueueFailedQueueName,
    *,
    client: AuthenticatedClient,
) -> (
    Error400
    | Error401
    | Error403
    | Error429
    | Error500
    | list[ListAdminQueueFailedResponse200Item]
    | None
):
    """Get failed jobs from a queue

     Returns jobs that have exceeded their retry limit and permanently failed.

    Args:
        queue_name (ListAdminQueueFailedQueueName):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error403 | Error429 | Error500 | list[ListAdminQueueFailedResponse200Item]
    """

    return sync_detailed(
        queue_name=queue_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    queue_name: ListAdminQueueFailedQueueName,
    *,
    client: AuthenticatedClient,
) -> Response[
    Error400 | Error401 | Error403 | Error429 | Error500 | list[ListAdminQueueFailedResponse200Item]
]:
    """Get failed jobs from a queue

     Returns jobs that have exceeded their retry limit and permanently failed.

    Args:
        queue_name (ListAdminQueueFailedQueueName):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error429 | Error500 | list[ListAdminQueueFailedResponse200Item]]
    """

    kwargs = _get_kwargs(
        queue_name=queue_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    queue_name: ListAdminQueueFailedQueueName,
    *,
    client: AuthenticatedClient,
) -> (
    Error400
    | Error401
    | Error403
    | Error429
    | Error500
    | list[ListAdminQueueFailedResponse200Item]
    | None
):
    """Get failed jobs from a queue

     Returns jobs that have exceeded their retry limit and permanently failed.

    Args:
        queue_name (ListAdminQueueFailedQueueName):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error403 | Error429 | Error500 | list[ListAdminQueueFailedResponse200Item]
    """

    return (
        await asyncio_detailed(
            queue_name=queue_name,
            client=client,
        )
    ).parsed
