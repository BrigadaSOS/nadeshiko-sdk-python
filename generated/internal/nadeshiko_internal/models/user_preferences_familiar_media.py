from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserPreferencesFamiliarMedia")


@_attrs_define
class UserPreferencesFamiliarMedia:
    """Whether to keep a monthly tally of which titles the reader studies, used to
    sort those titles up the search media filter.

    Deliberately NOT `searchHistory`: that preference governs the activity log
    (queries, timestamps, per-row deletion), this one governs an aggregate
    count per title per month. A reader can reasonably want the tally without
    the diary, so the two are stored apart, cleared apart, and expire apart.
    Existing readers who had `searchHistory` off were seeded to `false` here.

        Attributes:
            enabled (bool | Unset): Whether familiar-media tallying is enabled (default true)
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

        user_preferences_familiar_media = cls(
            enabled=enabled,
        )

        user_preferences_familiar_media.additional_properties = _src
        return user_preferences_familiar_media

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
