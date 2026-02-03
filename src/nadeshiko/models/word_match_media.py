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
        english_name (str | Unset): English translation of the media name Example: Steins;Gate.
        japanese_name (str | Unset): Original Japanese name of the media Example: シュタインズ・ゲート.
        romaji_name (str | Unset): Romaji transliteration of the media name Example: Steins;Gate.
        matches (int | Unset): Number of times the word appears in this media Example: 234.
    """

    media_id: int | Unset = UNSET
    english_name: str | Unset = UNSET
    japanese_name: str | Unset = UNSET
    romaji_name: str | Unset = UNSET
    matches: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media_id = self.media_id

        english_name = self.english_name

        japanese_name = self.japanese_name

        romaji_name = self.romaji_name

        matches = self.matches

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if media_id is not UNSET:
            field_dict["media_id"] = media_id
        if english_name is not UNSET:
            field_dict["english_name"] = english_name
        if japanese_name is not UNSET:
            field_dict["japanese_name"] = japanese_name
        if romaji_name is not UNSET:
            field_dict["romaji_name"] = romaji_name
        if matches is not UNSET:
            field_dict["matches"] = matches

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        media_id = d.pop("media_id", UNSET)

        english_name = d.pop("english_name", UNSET)

        japanese_name = d.pop("japanese_name", UNSET)

        romaji_name = d.pop("romaji_name", UNSET)

        matches = d.pop("matches", UNSET)

        word_match_media = cls(
            media_id=media_id,
            english_name=english_name,
            japanese_name=japanese_name,
            romaji_name=romaji_name,
            matches=matches,
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
