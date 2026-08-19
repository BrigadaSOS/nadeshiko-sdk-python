from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserPreferencesFavoriteMediaItem")


@_attrs_define
class UserPreferencesFavoriteMediaItem:
    """
    Attributes:
        media_public_id (str): Public ID of the starred media
        favorited_at (datetime.datetime): When the reader starred it, set by the server.
        name_en (str | Unset):
        name_ja (str | Unset):
        name_romaji (str | Unset):
    """

    media_public_id: str
    favorited_at: datetime.datetime
    name_en: str | Unset = UNSET
    name_ja: str | Unset = UNSET
    name_romaji: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media_public_id = self.media_public_id

        favorited_at = self.favorited_at.isoformat()

        name_en = self.name_en

        name_ja = self.name_ja

        name_romaji = self.name_romaji

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mediaPublicId": media_public_id,
                "favoritedAt": favorited_at,
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
        _src = dict(src_dict)
        media_public_id = _src.pop("mediaPublicId")

        favorited_at = datetime.datetime.fromisoformat(_src.pop("favoritedAt"))

        name_en = _src.pop("nameEn", UNSET)

        name_ja = _src.pop("nameJa", UNSET)

        name_romaji = _src.pop("nameRomaji", UNSET)

        user_preferences_favorite_media_item = cls(
            media_public_id=media_public_id,
            favorited_at=favorited_at,
            name_en=name_en,
            name_ja=name_ja,
            name_romaji=name_romaji,
        )

        user_preferences_favorite_media_item.additional_properties = _src
        return user_preferences_favorite_media_item

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
