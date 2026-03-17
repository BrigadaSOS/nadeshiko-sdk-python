from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.media_search_stats_episode_hits import MediaSearchStatsEpisodeHits


T = TypeVar("T", bound="MediaSearchStats")


@_attrs_define
class MediaSearchStats:
    """Search hit statistics for a single media

    Attributes:
        media_id (int): Media identifier (look up full details in includes.media) Example: 110316.
        public_id (str): Public identifier for use in URLs and filters Example: abc123xyz.
        match_count (int): Number of matching segments found in this media Example: 42.
        episode_hits (MediaSearchStatsEpisodeHits): Mapping of episode numbers to segment hit counts Example: {'1': 5,
            '2': 8, '3': 3}.
    """

    media_id: int
    public_id: str
    match_count: int
    episode_hits: MediaSearchStatsEpisodeHits
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media_id = self.media_id

        public_id = self.public_id

        match_count = self.match_count

        episode_hits = self.episode_hits.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mediaId": media_id,
                "publicId": public_id,
                "matchCount": match_count,
                "episodeHits": episode_hits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_search_stats_episode_hits import MediaSearchStatsEpisodeHits

        d = dict(src_dict)
        media_id = d.pop("mediaId")

        public_id = d.pop("publicId")

        match_count = d.pop("matchCount")

        episode_hits = MediaSearchStatsEpisodeHits.from_dict(d.pop("episodeHits"))

        media_search_stats = cls(
            media_id=media_id,
            public_id=public_id,
            match_count=match_count,
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
