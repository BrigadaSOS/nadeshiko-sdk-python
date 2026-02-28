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
from ...models.get_segment_by_uuid_include_item import GetSegmentByUuidIncludeItem
from ...models.segment_internal import SegmentInternal
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: str,
    *,
    include: list[GetSegmentByUuidIncludeItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_include: list[str] | Unset = UNSET
    if not isinstance(include, Unset):
        json_include = []
        for include_item_data in include:
            include_item = include_item_data.value
            json_include.append(include_item)

    params["include"] = json_include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/media/segments/{uuid}".format(
            uuid=quote(str(uuid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentInternal | None:
    if response.status_code == 200:
        response_200 = SegmentInternal.from_dict(response.json())

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
) -> Response[Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentInternal]:
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
    include: list[GetSegmentByUuidIncludeItem] | Unset = UNSET,
) -> Response[Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentInternal]:
    """Get segment by UUID or publicId

     Returns a specific segment by its UUID or publicId. A shortcut alternative to the nested
    `/media/{mediaId}/episodes/{episodeNumber}/segments/{id}` path.

    Pass `include[]=ratingAnalysis` and/or `include[]=posAnalysis` to receive raw analysis fields
    alongside the standard segment data.

    **Permissions:** `UPDATE_MEDIA` (API key) or admin session

    Args:
        uuid (str):
        include (list[GetSegmentByUuidIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentInternal]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: str,
    *,
    client: AuthenticatedClient,
    include: list[GetSegmentByUuidIncludeItem] | Unset = UNSET,
) -> Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentInternal | None:
    """Get segment by UUID or publicId

     Returns a specific segment by its UUID or publicId. A shortcut alternative to the nested
    `/media/{mediaId}/episodes/{episodeNumber}/segments/{id}` path.

    Pass `include[]=ratingAnalysis` and/or `include[]=posAnalysis` to receive raw analysis fields
    alongside the standard segment data.

    **Permissions:** `UPDATE_MEDIA` (API key) or admin session

    Args:
        uuid (str):
        include (list[GetSegmentByUuidIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentInternal
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        include=include,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
    include: list[GetSegmentByUuidIncludeItem] | Unset = UNSET,
) -> Response[Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentInternal]:
    """Get segment by UUID or publicId

     Returns a specific segment by its UUID or publicId. A shortcut alternative to the nested
    `/media/{mediaId}/episodes/{episodeNumber}/segments/{id}` path.

    Pass `include[]=ratingAnalysis` and/or `include[]=posAnalysis` to receive raw analysis fields
    alongside the standard segment data.

    **Permissions:** `UPDATE_MEDIA` (API key) or admin session

    Args:
        uuid (str):
        include (list[GetSegmentByUuidIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentInternal]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: str,
    *,
    client: AuthenticatedClient,
    include: list[GetSegmentByUuidIncludeItem] | Unset = UNSET,
) -> Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentInternal | None:
    """Get segment by UUID or publicId

     Returns a specific segment by its UUID or publicId. A shortcut alternative to the nested
    `/media/{mediaId}/episodes/{episodeNumber}/segments/{id}` path.

    Pass `include[]=ratingAnalysis` and/or `include[]=posAnalysis` to receive raw analysis fields
    alongside the standard segment data.

    **Permissions:** `UPDATE_MEDIA` (API key) or admin session

    Args:
        uuid (str):
        include (list[GetSegmentByUuidIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentInternal
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            include=include,
        )
    ).parsed
