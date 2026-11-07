from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MediaSearchStatsEpisodeHitsItem")


@_attrs_define
class MediaSearchStatsEpisodeHitsItem:
    """
    Attributes:
        episode (int): Episode number Example: 1.
        hit_count (int): Number of matching segments in this episode Example: 5.
        title (None | str | Unset): Episode title when it has one (an audiobook chapter's title), else null Example:
            (1)とにかく比企谷八幡はくさっている。.
    """

    episode: int
    hit_count: int
    title: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        episode = self.episode

        hit_count = self.hit_count

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "episode": episode,
                "hitCount": hit_count,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        episode = _src.pop("episode")

        hit_count = _src.pop("hitCount")

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(_src.pop("title", UNSET))

        media_search_stats_episode_hits_item = cls(
            episode=episode,
            hit_count=hit_count,
            title=title,
        )

        media_search_stats_episode_hits_item.additional_properties = _src
        return media_search_stats_episode_hits_item

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
