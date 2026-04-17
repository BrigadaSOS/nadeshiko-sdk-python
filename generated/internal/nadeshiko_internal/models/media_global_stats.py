from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MediaGlobalStats")


@_attrs_define
class MediaGlobalStats:
    """Global corpus totals across all media

    Attributes:
        total_media (int): Total number of media across all pages Example: 312.
        total_segments (int): Total number of non-deleted segments Example: 184520.
        total_episodes (int): Total number of episodes Example: 4287.
    """

    total_media: int
    total_segments: int
    total_episodes: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_media = self.total_media

        total_segments = self.total_segments

        total_episodes = self.total_episodes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalMedia": total_media,
                "totalSegments": total_segments,
                "totalEpisodes": total_episodes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        total_media = _src.pop("totalMedia")

        total_segments = _src.pop("totalSegments")

        total_episodes = _src.pop("totalEpisodes")

        media_global_stats = cls(
            total_media=total_media,
            total_segments=total_segments,
            total_episodes=total_episodes,
        )

        media_global_stats.additional_properties = _src
        return media_global_stats

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
