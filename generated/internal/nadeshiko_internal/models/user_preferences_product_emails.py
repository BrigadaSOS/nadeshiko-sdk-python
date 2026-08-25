from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserPreferencesProductEmails")


@_attrs_define
class UserPreferencesProductEmails:
    """Whether we may send this account the lifecycle mail — the day-7 note, the
    feedback ask, the monthly recap. Absent means yes: these are service
    messages about the functionality the reader uses, so the default is on and
    the reader turns it off, here or from the link in any of them.

    Does NOT govern transactional mail. Sign-in links and address verification
    are the account working rather than news about it, and honouring this flag
    for them would let somebody lock themselves out by unsubscribing.

        Attributes:
            enabled (bool | Unset): The master switch, and the only thing a `List-Unsubscribe` header with
                no category sets. Off here stops every category below it.
            recap (bool | Unset): The monthly digest of the reader's own activity. Absent means follow
                `enabled` — never a fresh yes, or a reader who left before this
                category existed would be re-subscribed by its arrival.
            checkins (bool | Unset): The occasional one-off questions: the day-7 note and the win-back.
                Absent means follow `enabled`.
            updates (bool | Unset): Releases and new features, including any request for support that
                rides in one. Sent through Zoho Campaigns rather than from here, so
                this governs the audience export. Absent means follow `enabled`.
    """

    enabled: bool | Unset = UNSET
    recap: bool | Unset = UNSET
    checkins: bool | Unset = UNSET
    updates: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        recap = self.recap

        checkins = self.checkins

        updates = self.updates

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if recap is not UNSET:
            field_dict["recap"] = recap
        if checkins is not UNSET:
            field_dict["checkins"] = checkins
        if updates is not UNSET:
            field_dict["updates"] = updates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        enabled = _src.pop("enabled", UNSET)

        recap = _src.pop("recap", UNSET)

        checkins = _src.pop("checkins", UNSET)

        updates = _src.pop("updates", UNSET)

        user_preferences_product_emails = cls(
            enabled=enabled,
            recap=recap,
            checkins=checkins,
            updates=updates,
        )

        user_preferences_product_emails.additional_properties = _src
        return user_preferences_product_emails

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
