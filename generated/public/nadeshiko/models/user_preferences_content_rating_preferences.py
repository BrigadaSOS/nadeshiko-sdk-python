from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_preferences_content_rating_preferences_nsfw import (
    UserPreferencesContentRatingPreferencesNsfw,
    check_user_preferences_content_rating_preferences_nsfw,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserPreferencesContentRatingPreferences")


@_attrs_define
class UserPreferencesContentRatingPreferences:
    """Per-category content rating display preferences

    Attributes:
        nsfw (UserPreferencesContentRatingPreferencesNsfw | Unset):
    """

    nsfw: UserPreferencesContentRatingPreferencesNsfw | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nsfw: str | Unset = UNSET
        if not isinstance(self.nsfw, Unset):
            nsfw = self.nsfw

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nsfw is not UNSET:
            field_dict["nsfw"] = nsfw

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        _nsfw = _src.pop("nsfw", UNSET)
        nsfw: UserPreferencesContentRatingPreferencesNsfw | Unset
        if isinstance(_nsfw, Unset):
            nsfw = UNSET
        else:
            nsfw = check_user_preferences_content_rating_preferences_nsfw(_nsfw)

        user_preferences_content_rating_preferences = cls(
            nsfw=nsfw,
        )

        user_preferences_content_rating_preferences.additional_properties = _src
        return user_preferences_content_rating_preferences

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
