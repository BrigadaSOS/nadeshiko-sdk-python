from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_preferences_word_popup_definition_size import (
    UserPreferencesWordPopupDefinitionSize,
    check_user_preferences_word_popup_definition_size,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserPreferencesWordPopup")


@_attrs_define
class UserPreferencesWordPopup:
    """How the word card behaves when a reader taps a word in a sentence. A group rather than a loose key so the settings
    that follow it have somewhere to live.

        Attributes:
            definition_size (UserPreferencesWordPopupDefinitionSize | Unset): How large the definitions themselves are
                printed. The card holds a reader's own monolingual dictionaries now, which is Japanese prose rather than a
                three-word English gloss, and a size that suited "to die; to pass away" is small for a paragraph of 大辞林. MEDIUM
                is the default; SMALL is what the card printed before this existed.
    """

    definition_size: UserPreferencesWordPopupDefinitionSize | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        definition_size: str | Unset = UNSET
        if not isinstance(self.definition_size, Unset):
            definition_size = self.definition_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if definition_size is not UNSET:
            field_dict["definitionSize"] = definition_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        _definition_size = _src.pop("definitionSize", UNSET)
        definition_size: UserPreferencesWordPopupDefinitionSize | Unset
        if isinstance(_definition_size, Unset):
            definition_size = UNSET
        else:
            definition_size = check_user_preferences_word_popup_definition_size(_definition_size)

        user_preferences_word_popup = cls(
            definition_size=definition_size,
        )

        user_preferences_word_popup.additional_properties = _src
        return user_preferences_word_popup

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
