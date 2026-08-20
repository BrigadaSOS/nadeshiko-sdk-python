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
            enabled (bool | Unset): Whether lifecycle emails are enabled (default true)
    """

    enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        enabled = _src.pop("enabled", UNSET)

        user_preferences_product_emails = cls(
            enabled=enabled,
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
