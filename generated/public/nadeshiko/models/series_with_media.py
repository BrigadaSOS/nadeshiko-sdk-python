from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.series_with_media_media_item import SeriesWithMediaMediaItem


T = TypeVar("T", bound="SeriesWithMedia")


@_attrs_define
class SeriesWithMedia:
    """Series with ordered media entries

    Attributes:
        id (int): Series ID Example: 1.
        name_ja (str): Japanese name of the series Example: バクマン。シリーズ.
        name_romaji (str): Romaji name of the series Example: Bakuman. Series.
        name_en (str): English name of the series Example: Bakuman Series.
        media (list[SeriesWithMediaMediaItem]): All media in the series, sorted by position
    """

    id: int
    name_ja: str
    name_romaji: str
    name_en: str
    media: list[SeriesWithMediaMediaItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name_ja = self.name_ja

        name_romaji = self.name_romaji

        name_en = self.name_en

        media = []
        for media_item_data in self.media:
            media_item = media_item_data.to_dict()
            media.append(media_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "nameJa": name_ja,
                "nameRomaji": name_romaji,
                "nameEn": name_en,
                "media": media,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.series_with_media_media_item import SeriesWithMediaMediaItem

        d = dict(src_dict)
        id = d.pop("id")

        name_ja = d.pop("nameJa")

        name_romaji = d.pop("nameRomaji")

        name_en = d.pop("nameEn")

        media = []
        _media = d.pop("media")
        for media_item_data in _media:
            media_item = SeriesWithMediaMediaItem.from_dict(media_item_data)

            media.append(media_item)

        series_with_media = cls(
            id=id,
            name_ja=name_ja,
            name_romaji=name_romaji,
            name_en=name_en,
            media=media,
        )

        series_with_media.additional_properties = d
        return series_with_media

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
