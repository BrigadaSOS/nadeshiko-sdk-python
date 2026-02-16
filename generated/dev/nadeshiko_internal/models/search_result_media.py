from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.category import Category
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchResultMedia")


@_attrs_define
class SearchResultMedia:
    """Media information included in search results

    Attributes:
        media_id (int): Unique identifier for the media Example: 110316.
        name_romaji (str): Romaji transliteration of the media name Example: Steins;Gate.
        category (Category): Media category type Example: ANIME.
        name_en (str | Unset): English name of the media Example: Steins;Gate.
        name_ja (str | Unset): Original Japanese name of the media Example: シュタインズ・ゲート.
        cover_url (str | Unset): URL to the cover image Example: https://example.com/media/anime/steins-gate/cover.jpg.
        banner_url (str | Unset): URL to the banner image Example: https://example.com/media/anime/steins-
            gate/banner.jpg.
    """

    media_id: int
    name_romaji: str
    category: Category
    name_en: str | Unset = UNSET
    name_ja: str | Unset = UNSET
    cover_url: str | Unset = UNSET
    banner_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media_id = self.media_id

        name_romaji = self.name_romaji

        category = self.category.value

        name_en = self.name_en

        name_ja = self.name_ja

        cover_url = self.cover_url

        banner_url = self.banner_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mediaId": media_id,
                "nameRomaji": name_romaji,
                "category": category,
            }
        )
        if name_en is not UNSET:
            field_dict["nameEn"] = name_en
        if name_ja is not UNSET:
            field_dict["nameJa"] = name_ja
        if cover_url is not UNSET:
            field_dict["coverUrl"] = cover_url
        if banner_url is not UNSET:
            field_dict["bannerUrl"] = banner_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        media_id = d.pop("mediaId")

        name_romaji = d.pop("nameRomaji")

        category = Category(d.pop("category"))

        name_en = d.pop("nameEn", UNSET)

        name_ja = d.pop("nameJa", UNSET)

        cover_url = d.pop("coverUrl", UNSET)

        banner_url = d.pop("bannerUrl", UNSET)

        search_result_media = cls(
            media_id=media_id,
            name_romaji=name_romaji,
            category=category,
            name_en=name_en,
            name_ja=name_ja,
            cover_url=cover_url,
            banner_url=banner_url,
        )

        search_result_media.additional_properties = d
        return search_result_media

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
