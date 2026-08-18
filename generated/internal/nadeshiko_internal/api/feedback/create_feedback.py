from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_feedback_request import CreateFeedbackRequest
from ...models.error_400 import Error400
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...models.feedback_receipt import FeedbackReceipt
from ...types import Response


def _get_kwargs(
    *,
    body: CreateFeedbackRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/feedback",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error400 | Error429 | Error500 | FeedbackReceipt | None:
    if response.status_code == 201:
        response_201 = FeedbackReceipt.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = Error400.from_dict(response.json())

        return response_400

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
) -> Response[Error400 | Error429 | Error500 | FeedbackReceipt]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateFeedbackRequest,
) -> Response[Error400 | Error429 | Error500 | FeedbackReceipt]:
    """Send feedback

     Records a free-text message about the product and notifies the team.

    Open to anonymous visitors on purpose — the person best placed to report a
    broken sign-up or a confusing empty state is the one who is not signed in.
    A session, when there is one, attaches the account and overrides `email`.

    Automated submissions are dropped silently rather than rejected: they get the
    same `201` as everyone else, and nothing is stored.

    Args:
        body (CreateFeedbackRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error429 | Error500 | FeedbackReceipt]
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
    body: CreateFeedbackRequest,
) -> Error400 | Error429 | Error500 | FeedbackReceipt | None:
    """Send feedback

     Records a free-text message about the product and notifies the team.

    Open to anonymous visitors on purpose — the person best placed to report a
    broken sign-up or a confusing empty state is the one who is not signed in.
    A session, when there is one, attaches the account and overrides `email`.

    Automated submissions are dropped silently rather than rejected: they get the
    same `201` as everyone else, and nothing is stored.

    Args:
        body (CreateFeedbackRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error429 | Error500 | FeedbackReceipt
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateFeedbackRequest,
) -> Response[Error400 | Error429 | Error500 | FeedbackReceipt]:
    """Send feedback

     Records a free-text message about the product and notifies the team.

    Open to anonymous visitors on purpose — the person best placed to report a
    broken sign-up or a confusing empty state is the one who is not signed in.
    A session, when there is one, attaches the account and overrides `email`.

    Automated submissions are dropped silently rather than rejected: they get the
    same `201` as everyone else, and nothing is stored.

    Args:
        body (CreateFeedbackRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error429 | Error500 | FeedbackReceipt]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateFeedbackRequest,
) -> Error400 | Error429 | Error500 | FeedbackReceipt | None:
    """Send feedback

     Records a free-text message about the product and notifies the team.

    Open to anonymous visitors on purpose — the person best placed to report a
    broken sign-up or a confusing empty state is the one who is not signed in.
    A session, when there is one, attaches the account and overrides `email`.

    Automated submissions are dropped silently rather than rejected: they get the
    same `201` as everyone else, and nothing is stored.

    Args:
        body (CreateFeedbackRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error429 | Error500 | FeedbackReceipt
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
