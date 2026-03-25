from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_preferences_content_rating_preferences_explicit import (
    UserPreferencesContentRatingPreferencesExplicit,
)
from ..models.user_preferences_content_rating_preferences_suggestive import (
    UserPreferencesContentRatingPreferencesSuggestive,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserPreferencesContentRatingPreferences")


@_attrs_define
class UserPreferencesContentRatingPreferences:
    """Per-category content rating display preferences

    Attributes:
        suggestive (UserPreferencesContentRatingPreferencesSuggestive | Unset):
        explicit (UserPreferencesContentRatingPreferencesExplicit | Unset):
    """

    suggestive: UserPreferencesContentRatingPreferencesSuggestive | Unset = UNSET
    explicit: UserPreferencesContentRatingPreferencesExplicit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        suggestive: str | Unset = UNSET
        if not isinstance(self.suggestive, Unset):
            suggestive = self.suggestive.value

        explicit: str | Unset = UNSET
        if not isinstance(self.explicit, Unset):
            explicit = self.explicit.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if suggestive is not UNSET:
            field_dict["suggestive"] = suggestive
        if explicit is not UNSET:
            field_dict["explicit"] = explicit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        _suggestive = _src.pop("suggestive", UNSET)
        suggestive: UserPreferencesContentRatingPreferencesSuggestive | Unset
        if isinstance(_suggestive, Unset):
            suggestive = UNSET
        else:
            suggestive = UserPreferencesContentRatingPreferencesSuggestive(_suggestive)

        _explicit = _src.pop("explicit", UNSET)
        explicit: UserPreferencesContentRatingPreferencesExplicit | Unset
        if isinstance(_explicit, Unset):
            explicit = UNSET
        else:
            explicit = UserPreferencesContentRatingPreferencesExplicit(_explicit)

        user_preferences_content_rating_preferences = cls(
            suggestive=suggestive,
            explicit=explicit,
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
