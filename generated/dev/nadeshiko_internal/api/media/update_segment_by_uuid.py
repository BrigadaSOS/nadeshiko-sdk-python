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
from ...models.segment_internal import SegmentInternal
from ...models.segment_update_request import SegmentUpdateRequest
from ...types import Response


def _get_kwargs(
    uuid: str,
    *,
    body: SegmentUpdateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/media/segments/{uuid}".format(
            uuid=quote(str(uuid), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: SegmentUpdateRequest,
) -> Response[Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentInternal]:
    """Update segment by UUID

     Updates an existing segment identified by its UUID. Performs the UUID→segment lookup internally,
    then applies the update. Only provided fields will be updated.

    **Permissions:** `UPDATE_MEDIA`

    Args:
        uuid (str):
        body (SegmentUpdateRequest): All fields are optional for partial updates

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentInternal]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: str,
    *,
    client: AuthenticatedClient,
    body: SegmentUpdateRequest,
) -> Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentInternal | None:
    """Update segment by UUID

     Updates an existing segment identified by its UUID. Performs the UUID→segment lookup internally,
    then applies the update. Only provided fields will be updated.

    **Permissions:** `UPDATE_MEDIA`

    Args:
        uuid (str):
        body (SegmentUpdateRequest): All fields are optional for partial updates

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentInternal
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
    body: SegmentUpdateRequest,
) -> Response[Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentInternal]:
    """Update segment by UUID

     Updates an existing segment identified by its UUID. Performs the UUID→segment lookup internally,
    then applies the update. Only provided fields will be updated.

    **Permissions:** `UPDATE_MEDIA`

    Args:
        uuid (str):
        body (SegmentUpdateRequest): All fields are optional for partial updates

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentInternal]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: str,
    *,
    client: AuthenticatedClient,
    body: SegmentUpdateRequest,
) -> Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentInternal | None:
    """Update segment by UUID

     Updates an existing segment identified by its UUID. Performs the UUID→segment lookup internally,
    then applies the update. Only provided fields will be updated.

    **Permissions:** `UPDATE_MEDIA`

    Args:
        uuid (str):
        body (SegmentUpdateRequest): All fields are optional for partial updates

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
            body=body,
        )
    ).parsed
