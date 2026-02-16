from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400 import Error400
from ...models.error_401 import Error401
from ...models.error_403 import Error403
from ...models.error_404 import Error404
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...models.segment_context_response import SegmentContextResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: str,
    *,
    limit: int | Unset = 3,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/media/segments/{uuid}/context".format(
            uuid=quote(str(uuid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentContextResponse | None
):
    if response.status_code == 200:
        response_200 = SegmentContextResponse.from_dict(response.json())

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
    Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentContextResponse
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 3,
) -> Response[
    Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentContextResponse
]:
    """Get surrounding context for a segment

     Retrieves segments surrounding a specific segment within an episode.
    Returns segments both before and after the target, providing dialogue context for how a sentence is
    used.

    **Permissions:** `READ_MEDIA`

    Args:
        uuid (str):
        limit (int | Unset):  Default: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentContextResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 3,
) -> (
    Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentContextResponse | None
):
    """Get surrounding context for a segment

     Retrieves segments surrounding a specific segment within an episode.
    Returns segments both before and after the target, providing dialogue context for how a sentence is
    used.

    **Permissions:** `READ_MEDIA`

    Args:
        uuid (str):
        limit (int | Unset):  Default: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentContextResponse
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 3,
) -> Response[
    Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentContextResponse
]:
    """Get surrounding context for a segment

     Retrieves segments surrounding a specific segment within an episode.
    Returns segments both before and after the target, providing dialogue context for how a sentence is
    used.

    **Permissions:** `READ_MEDIA`

    Args:
        uuid (str):
        limit (int | Unset):  Default: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentContextResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 3,
) -> (
    Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentContextResponse | None
):
    """Get surrounding context for a segment

     Retrieves segments surrounding a specific segment within an episode.
    Returns segments both before and after the target, providing dialogue context for how a sentence is
    used.

    **Permissions:** `READ_MEDIA`

    Args:
        uuid (str):
        limit (int | Unset):  Default: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentContextResponse
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            limit=limit,
        )
    ).parsed
