from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.affected_count_response import AffectedCountResponse
from ...models.error_401 import Error401
from ...models.error_403 import Error403
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...types import Response


def _get_kwargs(
    media_public_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/user/familiar-media/{media_public_id}".format(
            media_public_id=quote(str(media_public_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AffectedCountResponse | Error401 | Error403 | Error429 | Error500 | None:
    if response.status_code == 200:
        response_200 = AffectedCountResponse.from_dict(response.json())

        return response_200

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
) -> Response[AffectedCountResponse | Error401 | Error403 | Error429 | Error500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    media_public_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AffectedCountResponse | Error401 | Error403 | Error429 | Error500]:
    """Forget one title from the reader's tally

     Deletes the authenticated reader's tally for a single title, across every
    month it was counted in.

    The whole-tally clear is the blunt instrument; this is the one a reader
    reaches for when a single show is wrong -- a title they watched once for
    somebody else, or one the tally over-read. Forgetting a title does not stop
    it being counted again: the next export or share against it starts a fresh
    tally, which is the honest behaviour for a running count rather than a
    blocklist.

    Separate from the activity history, like the whole-tally clear: the two are
    stored apart and consented to apart, so neither touches the other's rows.

    Args:
        media_public_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AffectedCountResponse | Error401 | Error403 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        media_public_id=media_public_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    media_public_id: str,
    *,
    client: AuthenticatedClient,
) -> AffectedCountResponse | Error401 | Error403 | Error429 | Error500 | None:
    """Forget one title from the reader's tally

     Deletes the authenticated reader's tally for a single title, across every
    month it was counted in.

    The whole-tally clear is the blunt instrument; this is the one a reader
    reaches for when a single show is wrong -- a title they watched once for
    somebody else, or one the tally over-read. Forgetting a title does not stop
    it being counted again: the next export or share against it starts a fresh
    tally, which is the honest behaviour for a running count rather than a
    blocklist.

    Separate from the activity history, like the whole-tally clear: the two are
    stored apart and consented to apart, so neither touches the other's rows.

    Args:
        media_public_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AffectedCountResponse | Error401 | Error403 | Error429 | Error500
    """

    return sync_detailed(
        media_public_id=media_public_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    media_public_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AffectedCountResponse | Error401 | Error403 | Error429 | Error500]:
    """Forget one title from the reader's tally

     Deletes the authenticated reader's tally for a single title, across every
    month it was counted in.

    The whole-tally clear is the blunt instrument; this is the one a reader
    reaches for when a single show is wrong -- a title they watched once for
    somebody else, or one the tally over-read. Forgetting a title does not stop
    it being counted again: the next export or share against it starts a fresh
    tally, which is the honest behaviour for a running count rather than a
    blocklist.

    Separate from the activity history, like the whole-tally clear: the two are
    stored apart and consented to apart, so neither touches the other's rows.

    Args:
        media_public_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AffectedCountResponse | Error401 | Error403 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        media_public_id=media_public_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    media_public_id: str,
    *,
    client: AuthenticatedClient,
) -> AffectedCountResponse | Error401 | Error403 | Error429 | Error500 | None:
    """Forget one title from the reader's tally

     Deletes the authenticated reader's tally for a single title, across every
    month it was counted in.

    The whole-tally clear is the blunt instrument; this is the one a reader
    reaches for when a single show is wrong -- a title they watched once for
    somebody else, or one the tally over-read. Forgetting a title does not stop
    it being counted again: the next export or share against it starts a fresh
    tally, which is the honest behaviour for a running count rather than a
    blocklist.

    Separate from the activity history, like the whole-tally clear: the two are
    stored apart and consented to apart, so neither touches the other's rows.

    Args:
        media_public_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AffectedCountResponse | Error401 | Error403 | Error429 | Error500
    """

    return (
        await asyncio_detailed(
            media_public_id=media_public_id,
            client=client,
        )
    ).parsed
