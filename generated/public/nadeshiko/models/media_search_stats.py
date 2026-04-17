from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.media_search_stats_episode_hits_item import MediaSearchStatsEpisodeHitsItem


T = TypeVar("T", bound="MediaSearchStats")


@_attrs_define
class MediaSearchStats:
    """Search hit statistics for a single media

    Attributes:
        media_public_id (str): Media public ID (look up full details in `includes.media` when `include[]=media` is
            requested) Example: V1StGXR8_Z5d.
        match_count (int): Number of matching segments found in this media Example: 42.
        episode_hits (list[MediaSearchStatsEpisodeHitsItem]): Episode-level hit counts Example: [{'episode': 1,
            'hitCount': 5}, {'episode': 2, 'hitCount': 8}, {'episode': 3, 'hitCount': 3}].
    """

    media_public_id: str
    match_count: int
    episode_hits: list[MediaSearchStatsEpisodeHitsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media_public_id = self.media_public_id

        match_count = self.match_count

        episode_hits = []
        for episode_hits_item_data in self.episode_hits:
            episode_hits_item = episode_hits_item_data.to_dict()
            episode_hits.append(episode_hits_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mediaPublicId": media_public_id,
                "matchCount": match_count,
                "episodeHits": episode_hits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_search_stats_episode_hits_item import MediaSearchStatsEpisodeHitsItem

        _src = dict(src_dict)
        media_public_id = _src.pop("mediaPublicId")

        match_count = _src.pop("matchCount")

        episode_hits = []
        _episode_hits = _src.pop("episodeHits")
        for episode_hits_item_data in _episode_hits:
            episode_hits_item = MediaSearchStatsEpisodeHitsItem.from_dict(episode_hits_item_data)

            episode_hits.append(episode_hits_item)

        media_search_stats = cls(
            media_public_id=media_public_id,
            match_count=match_count,
            episode_hits=episode_hits,
        )

        media_search_stats.additional_properties = _src
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
