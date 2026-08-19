from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateFeedbackRequest")


@_attrs_define
class CreateFeedbackRequest:
    """
    Attributes:
        body (str): The message. Free text — no category, no target. Example: The audio on the search page stops after
            the first segment on Firefox..
        form_token (str): Opaque token from `GET /v1/feedback/token`, issued when the panel opened.
            It carries the issue time, so a submission that arrives implausibly fast
            after the form appeared can be told from a person typing.
        email (str | Unset): Optional reply address for anonymous senders. Ignored when the request
            carries a session: the account's own address is used instead, so a signed-in
            sender cannot attribute a message to somebody else's inbox.
             Example: you@example.com.
        nickname (str | Unset): Honeypot. Not rendered to people; anything in it marks the submission as
            automated. Present in the contract because it has to be accepted to be
            ignored.
        page_path (str | Unset): Same-origin path (and query) the sender was on, e.g. `/search?q=彼女`.
            Anything that is not a rooted path is dropped rather than rejected.
             Example: /search?q=彼女.
        locale (str | Unset): The locale the page rendered in, which is not the same question as
            `Accept-Language`: the site's locale comes from the URL prefix and a stored
            preference, so a reader on `/es/search` with an English browser is reading
            Spanish. Falls back to the request header when absent.
             Example: es.
        app_version (str | Unset): The frontend build the sender was running. Client-supplied because it is the
            only side that knows: the browser can be holding a bundle several deploys
            old, and the API's own version says nothing about it.
             Example: 2.4.0.
        posthog_session_id (str | Unset): PostHog session id, so a report links to its session replay. Blank where
            posthog is not loaded.
        posthog_distinct_id (str | Unset): PostHog person id.
    """

    body: str
    form_token: str
    email: str | Unset = UNSET
    nickname: str | Unset = UNSET
    page_path: str | Unset = UNSET
    locale: str | Unset = UNSET
    app_version: str | Unset = UNSET
    posthog_session_id: str | Unset = UNSET
    posthog_distinct_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        form_token = self.form_token

        email = self.email

        nickname = self.nickname

        page_path = self.page_path

        locale = self.locale

        app_version = self.app_version

        posthog_session_id = self.posthog_session_id

        posthog_distinct_id = self.posthog_distinct_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
                "formToken": form_token,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if page_path is not UNSET:
            field_dict["pagePath"] = page_path
        if locale is not UNSET:
            field_dict["locale"] = locale
        if app_version is not UNSET:
            field_dict["appVersion"] = app_version
        if posthog_session_id is not UNSET:
            field_dict["posthogSessionId"] = posthog_session_id
        if posthog_distinct_id is not UNSET:
            field_dict["posthogDistinctId"] = posthog_distinct_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        body = _src.pop("body")

        form_token = _src.pop("formToken")

        email = _src.pop("email", UNSET)

        nickname = _src.pop("nickname", UNSET)

        page_path = _src.pop("pagePath", UNSET)

        locale = _src.pop("locale", UNSET)

        app_version = _src.pop("appVersion", UNSET)

        posthog_session_id = _src.pop("posthogSessionId", UNSET)

        posthog_distinct_id = _src.pop("posthogDistinctId", UNSET)

        create_feedback_request = cls(
            body=body,
            form_token=form_token,
            email=email,
            nickname=nickname,
            page_path=page_path,
            locale=locale,
            app_version=app_version,
            posthog_session_id=posthog_session_id,
            posthog_distinct_id=posthog_distinct_id,
        )

        create_feedback_request.additional_properties = _src
        return create_feedback_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
