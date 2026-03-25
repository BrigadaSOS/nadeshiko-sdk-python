from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.category import Category

T = TypeVar("T", bound="MediaAutocompleteItem")


@_attrs_define
class MediaAutocompleteItem:
    """Slim media item returned by autocomplete (names + cover only)

    Attributes:
        id (int): Unique identifier for the media Example: 7674.
        public_id (str): Public identifier for the media Example: abc123xyz.
        name_ja (str): Original Japanese name of the media Example: バクマン。.
        name_romaji (str): Romaji transliteration of the media name Example: Bakuman..
        name_en (str): English name of the media Example: Bakuman..
        cover_url (str): Full URL to the cover image Example: https://cdn.example.com/media/anime/bakuman/cover.webp.
        category (Category): Media category type Example: ANIME.
    """

    id: int
    public_id: str
    name_ja: str
    name_romaji: str
    name_en: str
    cover_url: str
    category: Category
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        public_id = self.public_id

        name_ja = self.name_ja

        name_romaji = self.name_romaji

        name_en = self.name_en

        cover_url = self.cover_url

        category = self.category.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "publicId": public_id,
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
        id = _src.pop("id")

        public_id = _src.pop("publicId")

        name_ja = _src.pop("nameJa")

        name_romaji = _src.pop("nameRomaji")

        name_en = _src.pop("nameEn")

        cover_url = _src.pop("coverUrl")

        category = Category(_src.pop("category"))

        media_autocomplete_item = cls(
            id=id,
            public_id=public_id,
            name_ja=name_ja,
            name_romaji=name_romaji,
            name_en=name_en,
            cover_url=cover_url,
            category=category,
        )

        media_autocomplete_item.additional_properties = _src
        return media_autocomplete_item

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
