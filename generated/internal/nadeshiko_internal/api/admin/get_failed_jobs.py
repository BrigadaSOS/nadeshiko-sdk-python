from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_failed_jobs_queue_name import GetFailedJobsQueueName
from ...models.get_failed_jobs_response_200_item import GetFailedJobsResponse200Item
from typing import cast



def _get_kwargs(
    queue_name: GetFailedJobsQueueName,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/admin/queues/{queue_name}/failed".format(queue_name=quote(str(queue_name), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | list[GetFailedJobsResponse200Item] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = GetFailedJobsResponse200Item.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | list[GetFailedJobsResponse200Item]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    queue_name: GetFailedJobsQueueName,
    *,
    client: AuthenticatedClient,

) -> Response[Error | list[GetFailedJobsResponse200Item]]:
    """ Get failed jobs from a queue

     Get jobs that have exceeded their retry limit and permanently failed.

    **Requirements:**
    - Required Scopes: `ADD_MEDIA` (admin-level permission)

    **Use cases:**
    - Identify segments that failed to sync to Elasticsearch
    - Debug persistent sync issues
    - Decide whether to retry or purge failed jobs

    Args:
        queue_name (GetFailedJobsQueueName):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[GetFailedJobsResponse200Item]]
     """


    kwargs = _get_kwargs(
        queue_name=queue_name,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    queue_name: GetFailedJobsQueueName,
    *,
    client: AuthenticatedClient,

) -> Error | list[GetFailedJobsResponse200Item] | None:
    """ Get failed jobs from a queue

     Get jobs that have exceeded their retry limit and permanently failed.

    **Requirements:**
    - Required Scopes: `ADD_MEDIA` (admin-level permission)

    **Use cases:**
    - Identify segments that failed to sync to Elasticsearch
    - Debug persistent sync issues
    - Decide whether to retry or purge failed jobs

    Args:
        queue_name (GetFailedJobsQueueName):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[GetFailedJobsResponse200Item]
     """


    return sync_detailed(
        queue_name=queue_name,
client=client,

    ).parsed

async def asyncio_detailed(
    queue_name: GetFailedJobsQueueName,
    *,
    client: AuthenticatedClient,

) -> Response[Error | list[GetFailedJobsResponse200Item]]:
    """ Get failed jobs from a queue

     Get jobs that have exceeded their retry limit and permanently failed.

    **Requirements:**
    - Required Scopes: `ADD_MEDIA` (admin-level permission)

    **Use cases:**
    - Identify segments that failed to sync to Elasticsearch
    - Debug persistent sync issues
    - Decide whether to retry or purge failed jobs

    Args:
        queue_name (GetFailedJobsQueueName):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[GetFailedJobsResponse200Item]]
     """


    kwargs = _get_kwargs(
        queue_name=queue_name,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    queue_name: GetFailedJobsQueueName,
    *,
    client: AuthenticatedClient,

) -> Error | list[GetFailedJobsResponse200Item] | None:
    """ Get failed jobs from a queue

     Get jobs that have exceeded their retry limit and permanently failed.

    **Requirements:**
    - Required Scopes: `ADD_MEDIA` (admin-level permission)

    **Use cases:**
    - Identify segments that failed to sync to Elasticsearch
    - Debug persistent sync issues
    - Decide whether to retry or purge failed jobs

    Args:
        queue_name (GetFailedJobsQueueName):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[GetFailedJobsResponse200Item]
     """


    return (await asyncio_detailed(
        queue_name=queue_name,
client=client,

    )).parsed
