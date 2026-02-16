from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.admin_morpheme_backfill_create_response_200 import (
    AdminMorphemeBackfillCreateResponse200,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/admin/morpheme-backfill",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AdminMorphemeBackfillCreateResponse200 | None:
    if response.status_code == 200:
        response_200 = AdminMorphemeBackfillCreateResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AdminMorphemeBackfillCreateResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[AdminMorphemeBackfillCreateResponse200]:
    """Backfill morpheme analysis for segments

     Analyzes segments that are missing morpheme data using the Sudachi sidecar service.
    Returns stats on how many segments were successfully analyzed vs failed.

    **Permissions:** `ADD_MEDIA`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminMorphemeBackfillCreateResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> AdminMorphemeBackfillCreateResponse200 | None:
    """Backfill morpheme analysis for segments

     Analyzes segments that are missing morpheme data using the Sudachi sidecar service.
    Returns stats on how many segments were successfully analyzed vs failed.

    **Permissions:** `ADD_MEDIA`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminMorphemeBackfillCreateResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[AdminMorphemeBackfillCreateResponse200]:
    """Backfill morpheme analysis for segments

     Analyzes segments that are missing morpheme data using the Sudachi sidecar service.
    Returns stats on how many segments were successfully analyzed vs failed.

    **Permissions:** `ADD_MEDIA`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminMorphemeBackfillCreateResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> AdminMorphemeBackfillCreateResponse200 | None:
    """Backfill morpheme analysis for segments

     Analyzes segments that are missing morpheme data using the Sudachi sidecar service.
    Returns stats on how many segments were successfully analyzed vs failed.

    **Permissions:** `ADD_MEDIA`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminMorphemeBackfillCreateResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
