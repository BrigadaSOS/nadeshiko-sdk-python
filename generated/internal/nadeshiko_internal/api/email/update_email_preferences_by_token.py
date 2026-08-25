from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400 import Error400
from ...models.update_email_preferences_by_token_body import UpdateEmailPreferencesByTokenBody
from ...models.update_email_preferences_by_token_response_200 import (
    UpdateEmailPreferencesByTokenResponse200,
)
from ...types import Response


def _get_kwargs(
    *,
    body: UpdateEmailPreferencesByTokenBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/email/preferences",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error400 | UpdateEmailPreferencesByTokenResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdateEmailPreferencesByTokenResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error400.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error400 | UpdateEmailPreferencesByTokenResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateEmailPreferencesByTokenBody,
) -> Response[Error400 | UpdateEmailPreferencesByTokenResponse200]:
    r"""Change email preferences from an unsubscribe token

     Writes the categories the reader chose on the unsubscribe page.

    Every field is optional and only what is sent is changed, so the page can
    submit one checkbox without having to know or restate the rest.

    Turning the master off stops everything, which is what the \"stop all of it\"
    control does; turning it on again restores whatever the categories say.

    Args:
        body (UpdateEmailPreferencesByTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | UpdateEmailPreferencesByTokenResponse200]
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
    body: UpdateEmailPreferencesByTokenBody,
) -> Error400 | UpdateEmailPreferencesByTokenResponse200 | None:
    r"""Change email preferences from an unsubscribe token

     Writes the categories the reader chose on the unsubscribe page.

    Every field is optional and only what is sent is changed, so the page can
    submit one checkbox without having to know or restate the rest.

    Turning the master off stops everything, which is what the \"stop all of it\"
    control does; turning it on again restores whatever the categories say.

    Args:
        body (UpdateEmailPreferencesByTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | UpdateEmailPreferencesByTokenResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateEmailPreferencesByTokenBody,
) -> Response[Error400 | UpdateEmailPreferencesByTokenResponse200]:
    r"""Change email preferences from an unsubscribe token

     Writes the categories the reader chose on the unsubscribe page.

    Every field is optional and only what is sent is changed, so the page can
    submit one checkbox without having to know or restate the rest.

    Turning the master off stops everything, which is what the \"stop all of it\"
    control does; turning it on again restores whatever the categories say.

    Args:
        body (UpdateEmailPreferencesByTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | UpdateEmailPreferencesByTokenResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateEmailPreferencesByTokenBody,
) -> Error400 | UpdateEmailPreferencesByTokenResponse200 | None:
    r"""Change email preferences from an unsubscribe token

     Writes the categories the reader chose on the unsubscribe page.

    Every field is optional and only what is sent is changed, so the page can
    submit one checkbox without having to know or restate the rest.

    Turning the master off stops everything, which is what the \"stop all of it\"
    control does; turning it on again restores whatever the categories say.

    Args:
        body (UpdateEmailPreferencesByTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | UpdateEmailPreferencesByTokenResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
