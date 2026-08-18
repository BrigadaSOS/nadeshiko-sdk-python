from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_401 import Error401
from ...models.error_403 import Error403
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...models.resync_shirabe_stack_body import ResyncShirabeStackBody
from ...types import Response


def _get_kwargs(
    *,
    body: ResyncShirabeStackBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/user/connections/shirabe/resync",
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
    body: ResyncShirabeStackBody,
) -> Response[Any | Error401 | Error403 | Error429 | Error500]:
    """Reconcile the stored Shirabe stack against a fingerprint a lookup saw

     Shirabe echoes the calling key's current stack fingerprint on every word
    lookup. Our frontend server hands it back here, so a reader who switches a
    dictionary off over there stops being served their cached definitions for it.

    Cheap by design. When the fingerprint matches what we hold, this only records
    that the copy was confirmed; only a mismatch costs a round trip to Shirabe.

    Refused unless the request came through our own Nitro proxy (the shared
    internal secret), like the credential route beside it. Nothing here is a
    reader-facing action: the browser never sees a fingerprint, and one supplied
    by a client would be a client choosing when our copy looks stale.

    Args:
        body (ResyncShirabeStackBody):

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
    body: ResyncShirabeStackBody,
) -> Any | Error401 | Error403 | Error429 | Error500 | None:
    """Reconcile the stored Shirabe stack against a fingerprint a lookup saw

     Shirabe echoes the calling key's current stack fingerprint on every word
    lookup. Our frontend server hands it back here, so a reader who switches a
    dictionary off over there stops being served their cached definitions for it.

    Cheap by design. When the fingerprint matches what we hold, this only records
    that the copy was confirmed; only a mismatch costs a round trip to Shirabe.

    Refused unless the request came through our own Nitro proxy (the shared
    internal secret), like the credential route beside it. Nothing here is a
    reader-facing action: the browser never sees a fingerprint, and one supplied
    by a client would be a client choosing when our copy looks stale.

    Args:
        body (ResyncShirabeStackBody):

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
    body: ResyncShirabeStackBody,
) -> Response[Any | Error401 | Error403 | Error429 | Error500]:
    """Reconcile the stored Shirabe stack against a fingerprint a lookup saw

     Shirabe echoes the calling key's current stack fingerprint on every word
    lookup. Our frontend server hands it back here, so a reader who switches a
    dictionary off over there stops being served their cached definitions for it.

    Cheap by design. When the fingerprint matches what we hold, this only records
    that the copy was confirmed; only a mismatch costs a round trip to Shirabe.

    Refused unless the request came through our own Nitro proxy (the shared
    internal secret), like the credential route beside it. Nothing here is a
    reader-facing action: the browser never sees a fingerprint, and one supplied
    by a client would be a client choosing when our copy looks stale.

    Args:
        body (ResyncShirabeStackBody):

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
    body: ResyncShirabeStackBody,
) -> Any | Error401 | Error403 | Error429 | Error500 | None:
    """Reconcile the stored Shirabe stack against a fingerprint a lookup saw

     Shirabe echoes the calling key's current stack fingerprint on every word
    lookup. Our frontend server hands it back here, so a reader who switches a
    dictionary off over there stops being served their cached definitions for it.

    Cheap by design. When the fingerprint matches what we hold, this only records
    that the copy was confirmed; only a mismatch costs a round trip to Shirabe.

    Refused unless the request came through our own Nitro proxy (the shared
    internal secret), like the credential route beside it. Nothing here is a
    reader-facing action: the browser never sees a fingerprint, and one supplied
    by a client would be a client choosing when our copy looks stale.

    Args:
        body (ResyncShirabeStackBody):

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
