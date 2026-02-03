from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.fetch_sentence_context_request import FetchSentenceContextRequest
from ...models.fetch_sentence_context_response import FetchSentenceContextResponse
from ...types import Response


def _get_kwargs(
    *,
    body: FetchSentenceContextRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/search/media/context",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | FetchSentenceContextResponse | None:
    if response.status_code == 200:
        response_200 = FetchSentenceContextResponse.from_dict(response.json())

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


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | FetchSentenceContextResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FetchSentenceContextRequest,
) -> Response[Error | FetchSentenceContextResponse]:
    """Fetch context for a sentence

     Retrieves sentences surrounding a specific segment position within an episode.
    Returns segments both before and after the target position, providing context for understanding how
    a sentence is used in dialogue.

    **Requirements:**
    - Required scopes: `READ_MEDIA`

    Args:
        body (FetchSentenceContextRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | FetchSentenceContextResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: FetchSentenceContextRequest,
) -> Error | FetchSentenceContextResponse | None:
    """Fetch context for a sentence

     Retrieves sentences surrounding a specific segment position within an episode.
    Returns segments both before and after the target position, providing context for understanding how
    a sentence is used in dialogue.

    **Requirements:**
    - Required scopes: `READ_MEDIA`

    Args:
        body (FetchSentenceContextRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | FetchSentenceContextResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FetchSentenceContextRequest,
) -> Response[Error | FetchSentenceContextResponse]:
    """Fetch context for a sentence

     Retrieves sentences surrounding a specific segment position within an episode.
    Returns segments both before and after the target position, providing context for understanding how
    a sentence is used in dialogue.

    **Requirements:**
    - Required scopes: `READ_MEDIA`

    Args:
        body (FetchSentenceContextRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | FetchSentenceContextResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: FetchSentenceContextRequest,
) -> Error | FetchSentenceContextResponse | None:
    """Fetch context for a sentence

     Retrieves sentences surrounding a specific segment position within an episode.
    Returns segments both before and after the target position, providing context for understanding how
    a sentence is used in dialogue.

    **Requirements:**
    - Required scopes: `READ_MEDIA`

    Args:
        body (FetchSentenceContextRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | FetchSentenceContextResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
