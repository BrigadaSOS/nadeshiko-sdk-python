from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_401 import Error401
from ...models.error_403 import Error403
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...models.report_shirabe_refusal_body import ReportShirabeRefusalBody
from ...types import Response


def _get_kwargs(
    *,
    body: ReportShirabeRefusalBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/user/connections/shirabe/refused",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Error401 | Error403 | Error429 | Error500 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Any | Error401 | Error403 | Error429 | Error500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ReportShirabeRefusalBody,
) -> Response[Any | Error401 | Error403 | Error429 | Error500]:
    """Report that Shirabe refused a reader's key on a lookup

     A word lookup is where a dead link is actually discovered: the reader's key
    is sent, Shirabe refuses it, and the lookup quietly answers from the default
    dictionaries instead. Without this, that refusal was a log line and nothing
    else -- the settings page went on naming the account, and every later lookup
    repeated the same doomed round trip.

    What the status means is Shirabe's own distinction, and the three outcomes
    are different repairs:

    * `401` - the key is invalid, expired or revoked. The link is over until the
      reader makes a new one, and it is marked so the settings page can say so.
    * `403` - the key works but is missing a permission. The stack is re-read so
      the stored scopes catch up, which surfaces as a re-consent rather than a
      repair.
    * anything else - not an answer about the key. Ignored.

    Refused unless the request came through our own Nitro proxy (the shared
    internal secret), like the credential and resync routes beside it. A client
    that could post here could disconnect its own reader's link at will.

    Args:
        body (ReportShirabeRefusalBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error401 | Error403 | Error429 | Error500]
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
    client: AuthenticatedClient,
    body: ReportShirabeRefusalBody,
) -> Any | Error401 | Error403 | Error429 | Error500 | None:
    """Report that Shirabe refused a reader's key on a lookup

     A word lookup is where a dead link is actually discovered: the reader's key
    is sent, Shirabe refuses it, and the lookup quietly answers from the default
    dictionaries instead. Without this, that refusal was a log line and nothing
    else -- the settings page went on naming the account, and every later lookup
    repeated the same doomed round trip.

    What the status means is Shirabe's own distinction, and the three outcomes
    are different repairs:

    * `401` - the key is invalid, expired or revoked. The link is over until the
      reader makes a new one, and it is marked so the settings page can say so.
    * `403` - the key works but is missing a permission. The stack is re-read so
      the stored scopes catch up, which surfaces as a re-consent rather than a
      repair.
    * anything else - not an answer about the key. Ignored.

    Refused unless the request came through our own Nitro proxy (the shared
    internal secret), like the credential and resync routes beside it. A client
    that could post here could disconnect its own reader's link at will.

    Args:
        body (ReportShirabeRefusalBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error401 | Error403 | Error429 | Error500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ReportShirabeRefusalBody,
) -> Response[Any | Error401 | Error403 | Error429 | Error500]:
    """Report that Shirabe refused a reader's key on a lookup

     A word lookup is where a dead link is actually discovered: the reader's key
    is sent, Shirabe refuses it, and the lookup quietly answers from the default
    dictionaries instead. Without this, that refusal was a log line and nothing
    else -- the settings page went on naming the account, and every later lookup
    repeated the same doomed round trip.

    What the status means is Shirabe's own distinction, and the three outcomes
    are different repairs:

    * `401` - the key is invalid, expired or revoked. The link is over until the
      reader makes a new one, and it is marked so the settings page can say so.
    * `403` - the key works but is missing a permission. The stack is re-read so
      the stored scopes catch up, which surfaces as a re-consent rather than a
      repair.
    * anything else - not an answer about the key. Ignored.

    Refused unless the request came through our own Nitro proxy (the shared
    internal secret), like the credential and resync routes beside it. A client
    that could post here could disconnect its own reader's link at will.

    Args:
        body (ReportShirabeRefusalBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error401 | Error403 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ReportShirabeRefusalBody,
) -> Any | Error401 | Error403 | Error429 | Error500 | None:
    """Report that Shirabe refused a reader's key on a lookup

     A word lookup is where a dead link is actually discovered: the reader's key
    is sent, Shirabe refuses it, and the lookup quietly answers from the default
    dictionaries instead. Without this, that refusal was a log line and nothing
    else -- the settings page went on naming the account, and every later lookup
    repeated the same doomed round trip.

    What the status means is Shirabe's own distinction, and the three outcomes
    are different repairs:

    * `401` - the key is invalid, expired or revoked. The link is over until the
      reader makes a new one, and it is marked so the settings page can say so.
    * `403` - the key works but is missing a permission. The stack is re-read so
      the stored scopes catch up, which surfaces as a re-consent rather than a
      repair.
    * anything else - not an answer about the key. Ignored.

    Refused unless the request came through our own Nitro proxy (the shared
    internal secret), like the credential and resync routes beside it. A client
    that could post here could disconnect its own reader's link at will.

    Args:
        body (ReportShirabeRefusalBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error401 | Error403 | Error429 | Error500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
