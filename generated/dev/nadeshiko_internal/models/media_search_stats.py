from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.category import Category
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_search_stats_episode_hits import MediaSearchStatsEpisodeHits


T = TypeVar("T", bound="MediaSearchStats")


@_attrs_define
class MediaSearchStats:
    """Search result statistics grouped by media

    Attributes:
        media_id (int | Unset): Unique identifier for the media Example: 110316.
        category (Category | Unset): Media category type Example: ANIME.
        name_romaji (str | Unset): Romaji transliteration of the media name Example: Steins;Gate.
        name_en (str | Unset): English name of the media Example: Steins;Gate.
        name_ja (str | Unset): Original Japanese name of the media Example: シュタインズ・ゲート.
        segment_count (int | Unset): Total number of segments found for this media Example: 42.
        episode_hits (MediaSearchStatsEpisodeHits | Unset): Mapping of episode numbers to segment hit counts Example:
            {'1': 5, '2': 8, '3': 3}.
    """

    media_id: int | Unset = UNSET
    category: Category | Unset = UNSET
    name_romaji: str | Unset = UNSET
    name_en: str | Unset = UNSET
    name_ja: str | Unset = UNSET
    segment_count: int | Unset = UNSET
    episode_hits: MediaSearchStatsEpisodeHits | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media_id = self.media_id

        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        name_romaji = self.name_romaji

        name_en = self.name_en

        name_ja = self.name_ja

        segment_count = self.segment_count

        episode_hits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.episode_hits, Unset):
            episode_hits = self.episode_hits.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if media_id is not UNSET:
            field_dict["mediaId"] = media_id
        if category is not UNSET:
            field_dict["category"] = category
        if name_romaji is not UNSET:
            field_dict["nameRomaji"] = name_romaji
        if name_en is not UNSET:
            field_dict["nameEn"] = name_en
        if name_ja is not UNSET:
            field_dict["nameJa"] = name_ja
        if segment_count is not UNSET:
            field_dict["segmentCount"] = segment_count
        if episode_hits is not UNSET:
            field_dict["episodeHits"] = episode_hits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_search_stats_episode_hits import MediaSearchStatsEpisodeHits

        d = dict(src_dict)
        media_id = d.pop("mediaId", UNSET)

        _category = d.pop("category", UNSET)
        category: Category | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = Category(_category)

        name_romaji = d.pop("nameRomaji", UNSET)

        name_en = d.pop("nameEn", UNSET)

        name_ja = d.pop("nameJa", UNSET)

        segment_count = d.pop("segmentCount", UNSET)

        _episode_hits = d.pop("episodeHits", UNSET)
        episode_hits: MediaSearchStatsEpisodeHits | Unset
        if isinstance(_episode_hits, Unset):
            episode_hits = UNSET
        else:
            episode_hits = MediaSearchStatsEpisodeHits.from_dict(_episode_hits)

        media_search_stats = cls(
            media_id=media_id,
            category=category,
            name_romaji=name_romaji,
            name_en=name_en,
            name_ja=name_ja,
            segment_count=segment_count,
            episode_hits=episode_hits,
        )

        media_search_stats.additional_properties = d
        return media_search_stats

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
