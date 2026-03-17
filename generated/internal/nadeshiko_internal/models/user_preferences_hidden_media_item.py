from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserPreferencesHiddenMediaItem")


@_attrs_define
class UserPreferencesHiddenMediaItem:
    """
    Attributes:
        media_id (int):
        name_en (str | Unset):
        name_ja (str | Unset):
        name_romaji (str | Unset):
    """

    media_id: int
    name_en: str | Unset = UNSET
    name_ja: str | Unset = UNSET
    name_romaji: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media_id = self.media_id

        name_en = self.name_en

        name_ja = self.name_ja

        name_romaji = self.name_romaji

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mediaId": media_id,
            }
        )
        if name_en is not UNSET:
            field_dict["nameEn"] = name_en
        if name_ja is not UNSET:
            field_dict["nameJa"] = name_ja
        if name_romaji is not UNSET:
            field_dict["nameRomaji"] = name_romaji

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        media_id = d.pop("mediaId")

        name_en = d.pop("nameEn", UNSET)

        name_ja = d.pop("nameJa", UNSET)

        name_romaji = d.pop("nameRomaji", UNSET)

        user_preferences_hidden_media_item = cls(
            media_id=media_id,
            name_en=name_en,
            name_ja=name_ja,
            name_romaji=name_romaji,
        )

        user_preferences_hidden_media_item.additional_properties = d
        return user_preferences_hidden_media_item

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
