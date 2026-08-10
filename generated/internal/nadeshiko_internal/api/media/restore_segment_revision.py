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
from ...types import Response


def _get_kwargs(
    segment_public_id: str,
    revision_number: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/media/segments/{segment_public_id}/revisions/{revision_number}/restore".format(
            segment_public_id=quote(str(segment_public_id), safe=""),
            revision_number=quote(str(revision_number), safe=""),
        ),
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
    segment_public_id: str,
    revision_number: int,
    *,
    client: AuthenticatedClient,
) -> Response[Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentInternal]:
    """Restore a segment revision

     Writes the values captured in the given revision's snapshot back onto the
    segment, undoing every edit made since.

    The restore is itself an edit: it writes a new revision snapshotting the state
    it replaced, so restoring is reversible by restoring again. Revision numbers
    are never rewound — a segment at revision 7 restored to revision 3 lands at
    revision 8, whose snapshot holds what revision 7 left behind.

    This is the undo path for a bad moderation edit, whether a person or the agent
    made it.

    Args:
        segment_public_id (str):
        revision_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentInternal]
    """

    kwargs = _get_kwargs(
        segment_public_id=segment_public_id,
        revision_number=revision_number,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    segment_public_id: str,
    revision_number: int,
    *,
    client: AuthenticatedClient,
) -> Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentInternal | None:
    """Restore a segment revision

     Writes the values captured in the given revision's snapshot back onto the
    segment, undoing every edit made since.

    The restore is itself an edit: it writes a new revision snapshotting the state
    it replaced, so restoring is reversible by restoring again. Revision numbers
    are never rewound — a segment at revision 7 restored to revision 3 lands at
    revision 8, whose snapshot holds what revision 7 left behind.

    This is the undo path for a bad moderation edit, whether a person or the agent
    made it.

    Args:
        segment_public_id (str):
        revision_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentInternal
    """

    return sync_detailed(
        segment_public_id=segment_public_id,
        revision_number=revision_number,
        client=client,
    ).parsed


async def asyncio_detailed(
    segment_public_id: str,
    revision_number: int,
    *,
    client: AuthenticatedClient,
) -> Response[Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentInternal]:
    """Restore a segment revision

     Writes the values captured in the given revision's snapshot back onto the
    segment, undoing every edit made since.

    The restore is itself an edit: it writes a new revision snapshotting the state
    it replaced, so restoring is reversible by restoring again. Revision numbers
    are never rewound — a segment at revision 7 restored to revision 3 lands at
    revision 8, whose snapshot holds what revision 7 left behind.

    This is the undo path for a bad moderation edit, whether a person or the agent
    made it.

    Args:
        segment_public_id (str):
        revision_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentInternal]
    """

    kwargs = _get_kwargs(
        segment_public_id=segment_public_id,
        revision_number=revision_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    segment_public_id: str,
    revision_number: int,
    *,
    client: AuthenticatedClient,
) -> Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentInternal | None:
    """Restore a segment revision

     Writes the values captured in the given revision's snapshot back onto the
    segment, undoing every edit made since.

    The restore is itself an edit: it writes a new revision snapshotting the state
    it replaced, so restoring is reversible by restoring again. Revision numbers
    are never rewound — a segment at revision 7 restored to revision 3 lands at
    revision 8, whose snapshot holds what revision 7 left behind.

    This is the undo path for a bad moderation edit, whether a person or the agent
    made it.

    Args:
        segment_public_id (str):
        revision_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | SegmentInternal
    """

    return (
        await asyncio_detailed(
            segment_public_id=segment_public_id,
            revision_number=revision_number,
            client=client,
        )
    ).parsed
