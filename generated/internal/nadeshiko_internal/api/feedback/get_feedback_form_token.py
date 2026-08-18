from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...models.feedback_form_token import FeedbackFormToken
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/feedback/token",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error429 | Error500 | FeedbackFormToken | None:
    if response.status_code == 200:
        response_200 = FeedbackFormToken.from_dict(response.json())

        return response_200

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
) -> Response[Error429 | Error500 | FeedbackFormToken]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error429 | Error500 | FeedbackFormToken]:
    """Issue a feedback form token

     Called when the feedback panel opens. The token it returns carries the moment
    it was issued, sealed so the client cannot edit it, and `POST /v1/feedback`
    requires one: a submission that arrives faster than a person could have typed
    it, or with no token at all, is treated as automated.

    Deliberately a separate call rather than something embedded in the page: the
    site's HTML is cached at the edge, so anything baked into it would be shared
    by every visitor who got that copy and would be stale by an unbounded amount.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error429 | Error500 | FeedbackFormToken]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> Error429 | Error500 | FeedbackFormToken | None:
    """Issue a feedback form token

     Called when the feedback panel opens. The token it returns carries the moment
    it was issued, sealed so the client cannot edit it, and `POST /v1/feedback`
    requires one: a submission that arrives faster than a person could have typed
    it, or with no token at all, is treated as automated.

    Deliberately a separate call rather than something embedded in the page: the
    site's HTML is cached at the edge, so anything baked into it would be shared
    by every visitor who got that copy and would be stale by an unbounded amount.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error429 | Error500 | FeedbackFormToken
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error429 | Error500 | FeedbackFormToken]:
    """Issue a feedback form token

     Called when the feedback panel opens. The token it returns carries the moment
    it was issued, sealed so the client cannot edit it, and `POST /v1/feedback`
    requires one: a submission that arrives faster than a person could have typed
    it, or with no token at all, is treated as automated.

    Deliberately a separate call rather than something embedded in the page: the
    site's HTML is cached at the edge, so anything baked into it would be shared
    by every visitor who got that copy and would be stale by an unbounded amount.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error429 | Error500 | FeedbackFormToken]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> Error429 | Error500 | FeedbackFormToken | None:
    """Issue a feedback form token

     Called when the feedback panel opens. The token it returns carries the moment
    it was issued, sealed so the client cannot edit it, and `POST /v1/feedback`
    requires one: a submission that arrives faster than a person could have typed
    it, or with no token at all, is treated as automated.

    Deliberately a separate call rather than something embedded in the page: the
    site's HTML is cached at the edge, so anything baked into it would be shared
    by every visitor who got that copy and would be stale by an unbounded amount.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error429 | Error500 | FeedbackFormToken
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
