from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_preferences_translation_visibility_preferences_en import (
    UserPreferencesTranslationVisibilityPreferencesEN,
    check_user_preferences_translation_visibility_preferences_en,
)
from ..models.user_preferences_translation_visibility_preferences_es import (
    UserPreferencesTranslationVisibilityPreferencesES,
    check_user_preferences_translation_visibility_preferences_es,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserPreferencesTranslationVisibilityPreferences")


@_attrs_define
class UserPreferencesTranslationVisibilityPreferences:
    """Per-language visibility mode for translations in search results, keyed by ISO 639-1 code (uppercase)

    Attributes:
        en (UserPreferencesTranslationVisibilityPreferencesEN | Unset):
        es (UserPreferencesTranslationVisibilityPreferencesES | Unset):
    """

    en: UserPreferencesTranslationVisibilityPreferencesEN | Unset = UNSET
    es: UserPreferencesTranslationVisibilityPreferencesES | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        en: str | Unset = UNSET
        if not isinstance(self.en, Unset):
            en = self.en

        es: str | Unset = UNSET
        if not isinstance(self.es, Unset):
            es = self.es

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if en is not UNSET:
            field_dict["EN"] = en
        if es is not UNSET:
            field_dict["ES"] = es

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        _en = _src.pop("EN", UNSET)
        en: UserPreferencesTranslationVisibilityPreferencesEN | Unset
        if isinstance(_en, Unset):
            en = UNSET
        else:
            en = check_user_preferences_translation_visibility_preferences_en(_en)

        _es = _src.pop("ES", UNSET)
        es: UserPreferencesTranslationVisibilityPreferencesES | Unset
        if isinstance(_es, Unset):
            es = UNSET
        else:
            es = check_user_preferences_translation_visibility_preferences_es(_es)

        user_preferences_translation_visibility_preferences = cls(
            en=en,
            es=es,
        )

        user_preferences_translation_visibility_preferences.additional_properties = _src
        return user_preferences_translation_visibility_preferences

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
