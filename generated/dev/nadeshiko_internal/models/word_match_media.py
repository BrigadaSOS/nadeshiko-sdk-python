from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WordMatchMedia")


@_attrs_define
class WordMatchMedia:
    """Media entry containing word matches

    Attributes:
        media_id (int | Unset): Unique identifier for the media Example: 110316.
        name_en (str | Unset): English name of the media Example: Steins;Gate.
        name_ja (str | Unset): Original Japanese name of the media Example: シュタインズ・ゲート.
        name_romaji (str | Unset): Romaji transliteration of the media name Example: Steins;Gate.
        match_count (int | Unset): Number of times the word appears in this media Example: 234.
    """

    media_id: int | Unset = UNSET
    name_en: str | Unset = UNSET
    name_ja: str | Unset = UNSET
    name_romaji: str | Unset = UNSET
    match_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media_id = self.media_id

        name_en = self.name_en

        name_ja = self.name_ja

        name_romaji = self.name_romaji

        match_count = self.match_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if media_id is not UNSET:
            field_dict["mediaId"] = media_id
        if name_en is not UNSET:
            field_dict["nameEn"] = name_en
        if name_ja is not UNSET:
            field_dict["nameJa"] = name_ja
        if name_romaji is not UNSET:
            field_dict["nameRomaji"] = name_romaji
        if match_count is not UNSET:
            field_dict["matchCount"] = match_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        media_id = d.pop("mediaId", UNSET)

        name_en = d.pop("nameEn", UNSET)

        name_ja = d.pop("nameJa", UNSET)

        name_romaji = d.pop("nameRomaji", UNSET)

        match_count = d.pop("matchCount", UNSET)

        word_match_media = cls(
            media_id=media_id,
            name_en=name_en,
            name_ja=name_ja,
            name_romaji=name_romaji,
            match_count=match_count,
        )

        word_match_media.additional_properties = d
        return word_match_media

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
