from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_queue_stats_response_200_item import GetQueueStatsResponse200Item
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/admin/queues/stats",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | list[GetQueueStatsResponse200Item] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = GetQueueStatsResponse200Item.from_dict(response_200_item_data)



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | list[GetQueueStatsResponse200Item]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Error | list[GetQueueStatsResponse200Item]]:
    """ Get queue statistics

     Get statistics for all ES sync queues including pending and failed job counts.

    **Requirements:**
    - Required Scopes: `ADD_MEDIA` (admin-level permission)

    **Use cases:**
    - Monitor queue health
    - Detect stuck jobs
    - Check backlog size

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[GetQueueStatsResponse200Item]]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> Error | list[GetQueueStatsResponse200Item] | None:
    """ Get queue statistics

     Get statistics for all ES sync queues including pending and failed job counts.

    **Requirements:**
    - Required Scopes: `ADD_MEDIA` (admin-level permission)

    **Use cases:**
    - Monitor queue health
    - Detect stuck jobs
    - Check backlog size

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[GetQueueStatsResponse200Item]
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Error | list[GetQueueStatsResponse200Item]]:
    """ Get queue statistics

     Get statistics for all ES sync queues including pending and failed job counts.

    **Requirements:**
    - Required Scopes: `ADD_MEDIA` (admin-level permission)

    **Use cases:**
    - Monitor queue health
    - Detect stuck jobs
    - Check backlog size

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[GetQueueStatsResponse200Item]]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> Error | list[GetQueueStatsResponse200Item] | None:
    """ Get queue statistics

     Get statistics for all ES sync queues including pending and failed job counts.

    **Requirements:**
    - Required Scopes: `ADD_MEDIA` (admin-level permission)

    **Use cases:**
    - Monitor queue health
    - Detect stuck jobs
    - Check backlog size

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[GetQueueStatsResponse200Item]
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
