from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.category import Category, check_category

T = TypeVar("T", bound="MediaSummary")


@_attrs_define
class MediaSummary:
    """Slim media item returned by autocomplete (names + cover only)

    Attributes:
        public_id (str): Public ID for the media Example: V1StGXR8_Z5d.
        slug (str): URL-friendly slug for the media Example: bakuman.
        name_ja (str): Original Japanese name of the media Example: バクマン。.
        name_romaji (str): Romaji transliteration of the media name Example: Bakuman..
        name_en (str): English name of the media Example: Bakuman..
        cover_url (str): Full URL to the cover image Example: https://cdn.example.com/media/anime/bakuman/cover.webp.
        category (Category): Media category type Example: ANIME.
    """

    public_id: str
    slug: str
    name_ja: str
    name_romaji: str
    name_en: str
    cover_url: str
    category: Category
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_id = self.public_id

        slug = self.slug

        name_ja = self.name_ja

        name_romaji = self.name_romaji

        name_en = self.name_en

        cover_url = self.cover_url

        category: str = self.category

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "publicId": public_id,
                "slug": slug,
                "nameJa": name_ja,
                "nameRomaji": name_romaji,
                "nameEn": name_en,
                "coverUrl": cover_url,
                "category": category,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        public_id = _src.pop("publicId")

        slug = _src.pop("slug")

        name_ja = _src.pop("nameJa")

        name_romaji = _src.pop("nameRomaji")

        name_en = _src.pop("nameEn")

        cover_url = _src.pop("coverUrl")

        category = check_category(_src.pop("category"))

        media_summary = cls(
            public_id=public_id,
            slug=slug,
            name_ja=name_ja,
            name_romaji=name_romaji,
            name_en=name_en,
            cover_url=cover_url,
            category=category,
        )

        media_summary.additional_properties = _src
        return media_summary

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
