from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from typing import cast



def _get_kwargs(
    media_id: int,
    episode_number: int,
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/media/{media_id}/episodes/{episode_number}/segments/{id}".format(media_id=quote(str(media_id), safe=""),episode_number=quote(str(episode_number), safe=""),id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    media_id: int,
    episode_number: int,
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[Any | Error]:
    """ Delete segment (set status to deleted)

     Delete a segment by setting its status to 0 (DELETED)

    Args:
        media_id (int):
        episode_number (int):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        media_id=media_id,
episode_number=episode_number,
id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    media_id: int,
    episode_number: int,
    id: int,
    *,
    client: AuthenticatedClient,

) -> Any | Error | None:
    """ Delete segment (set status to deleted)

     Delete a segment by setting its status to 0 (DELETED)

    Args:
        media_id (int):
        episode_number (int):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return sync_detailed(
        media_id=media_id,
episode_number=episode_number,
id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    media_id: int,
    episode_number: int,
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[Any | Error]:
    """ Delete segment (set status to deleted)

     Delete a segment by setting its status to 0 (DELETED)

    Args:
        media_id (int):
        episode_number (int):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        media_id=media_id,
episode_number=episode_number,
id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    media_id: int,
    episode_number: int,
    id: int,
    *,
    client: AuthenticatedClient,

) -> Any | Error | None:
    """ Delete segment (set status to deleted)

     Delete a segment by setting its status to 0 (DELETED)

    Args:
        media_id (int):
        episode_number (int):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return (await asyncio_detailed(
        media_id=media_id,
episode_number=episode_number,
id=id,
client=client,

    )).parsed
