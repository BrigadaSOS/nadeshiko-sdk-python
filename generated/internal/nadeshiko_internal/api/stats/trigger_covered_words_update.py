from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_500 import Error500
from ...models.trigger_covered_words_update_body import TriggerCoveredWordsUpdateBody
from ...models.trigger_covered_words_update_response_200 import TriggerCoveredWordsUpdateResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: TriggerCoveredWordsUpdateBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/stats/covered-words/update",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error500 | TriggerCoveredWordsUpdateResponse200 | None:
    if response.status_code == 200:
        response_200 = TriggerCoveredWordsUpdateResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 500:
        response_500 = Error500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error500 | TriggerCoveredWordsUpdateResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: TriggerCoveredWordsUpdateBody | Unset = UNSET,
) -> Response[Error500 | TriggerCoveredWordsUpdateResponse200]:
    """Trigger word coverage update

     Re-checks word coverage by querying Elasticsearch for all words in the frequency table.
    Can optionally only check currently uncovered words (faster for incremental updates after adding new
    media).

    Args:
        body (TriggerCoveredWordsUpdateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error500 | TriggerCoveredWordsUpdateResponse200]
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
    body: TriggerCoveredWordsUpdateBody | Unset = UNSET,
) -> Error500 | TriggerCoveredWordsUpdateResponse200 | None:
    """Trigger word coverage update

     Re-checks word coverage by querying Elasticsearch for all words in the frequency table.
    Can optionally only check currently uncovered words (faster for incremental updates after adding new
    media).

    Args:
        body (TriggerCoveredWordsUpdateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error500 | TriggerCoveredWordsUpdateResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: TriggerCoveredWordsUpdateBody | Unset = UNSET,
) -> Response[Error500 | TriggerCoveredWordsUpdateResponse200]:
    """Trigger word coverage update

     Re-checks word coverage by querying Elasticsearch for all words in the frequency table.
    Can optionally only check currently uncovered words (faster for incremental updates after adding new
    media).

    Args:
        body (TriggerCoveredWordsUpdateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error500 | TriggerCoveredWordsUpdateResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: TriggerCoveredWordsUpdateBody | Unset = UNSET,
) -> Error500 | TriggerCoveredWordsUpdateResponse200 | None:
    """Trigger word coverage update

     Re-checks word coverage by querying Elasticsearch for all words in the frequency table.
    Can optionally only check currently uncovered words (faster for incremental updates after adding new
    media).

    Args:
        body (TriggerCoveredWordsUpdateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error500 | TriggerCoveredWordsUpdateResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
