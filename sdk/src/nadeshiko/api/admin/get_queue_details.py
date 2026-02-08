from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_queue_details_queue_name import GetQueueDetailsQueueName
from ...models.get_queue_details_response_200 import GetQueueDetailsResponse200
from typing import cast



def _get_kwargs(
    queue_name: GetQueueDetailsQueueName,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/admin/queues/{queue_name}".format(queue_name=quote(str(queue_name), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetQueueDetailsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetQueueDetailsResponse200.from_dict(response.json())



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

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetQueueDetailsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    queue_name: GetQueueDetailsQueueName,
    *,
    client: AuthenticatedClient,

) -> Response[Error | GetQueueDetailsResponse200]:
    """ Get detailed queue information

     Get detailed information about a specific queue including completed, expired, and cancelled jobs.

    **Requirements:**
    - Required Scopes: `ADD_MEDIA` (admin-level permission)

    **Queue names:**
    - `es-sync-create` - Jobs to create new segments
    - `es-sync-update` - Jobs to update existing segments
    - `es-sync-delete` - Jobs to delete segments

    Args:
        queue_name (GetQueueDetailsQueueName):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetQueueDetailsResponse200]
     """


    kwargs = _get_kwargs(
        queue_name=queue_name,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    queue_name: GetQueueDetailsQueueName,
    *,
    client: AuthenticatedClient,

) -> Error | GetQueueDetailsResponse200 | None:
    """ Get detailed queue information

     Get detailed information about a specific queue including completed, expired, and cancelled jobs.

    **Requirements:**
    - Required Scopes: `ADD_MEDIA` (admin-level permission)

    **Queue names:**
    - `es-sync-create` - Jobs to create new segments
    - `es-sync-update` - Jobs to update existing segments
    - `es-sync-delete` - Jobs to delete segments

    Args:
        queue_name (GetQueueDetailsQueueName):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetQueueDetailsResponse200
     """


    return sync_detailed(
        queue_name=queue_name,
client=client,

    ).parsed

async def asyncio_detailed(
    queue_name: GetQueueDetailsQueueName,
    *,
    client: AuthenticatedClient,

) -> Response[Error | GetQueueDetailsResponse200]:
    """ Get detailed queue information

     Get detailed information about a specific queue including completed, expired, and cancelled jobs.

    **Requirements:**
    - Required Scopes: `ADD_MEDIA` (admin-level permission)

    **Queue names:**
    - `es-sync-create` - Jobs to create new segments
    - `es-sync-update` - Jobs to update existing segments
    - `es-sync-delete` - Jobs to delete segments

    Args:
        queue_name (GetQueueDetailsQueueName):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetQueueDetailsResponse200]
     """


    kwargs = _get_kwargs(
        queue_name=queue_name,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    queue_name: GetQueueDetailsQueueName,
    *,
    client: AuthenticatedClient,

) -> Error | GetQueueDetailsResponse200 | None:
    """ Get detailed queue information

     Get detailed information about a specific queue including completed, expired, and cancelled jobs.

    **Requirements:**
    - Required Scopes: `ADD_MEDIA` (admin-level permission)

    **Queue names:**
    - `es-sync-create` - Jobs to create new segments
    - `es-sync-update` - Jobs to update existing segments
    - `es-sync-delete` - Jobs to delete segments

    Args:
        queue_name (GetQueueDetailsQueueName):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetQueueDetailsResponse200
     """


    return (await asyncio_detailed(
        queue_name=queue_name,
client=client,

    )).parsed
