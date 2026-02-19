from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_activity_stats_response_200_top_media_item import (
        GetActivityStatsResponse200TopMediaItem,
    )


T = TypeVar("T", bound="GetActivityStatsResponse200")


@_attrs_define
class GetActivityStatsResponse200:
    """
    Attributes:
        total_searches (int):
        total_exports (int):
        total_plays (int):
        total_list_adds (int):
        streak_days (int): Consecutive days with at least one activity
        top_media (list[GetActivityStatsResponse200TopMediaItem]):
    """

    total_searches: int
    total_exports: int
    total_plays: int
    total_list_adds: int
    streak_days: int
    top_media: list[GetActivityStatsResponse200TopMediaItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_searches = self.total_searches

        total_exports = self.total_exports

        total_plays = self.total_plays

        total_list_adds = self.total_list_adds

        streak_days = self.streak_days

        top_media = []
        for top_media_item_data in self.top_media:
            top_media_item = top_media_item_data.to_dict()
            top_media.append(top_media_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalSearches": total_searches,
                "totalExports": total_exports,
                "totalPlays": total_plays,
                "totalListAdds": total_list_adds,
                "streakDays": streak_days,
                "topMedia": top_media,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_activity_stats_response_200_top_media_item import (
            GetActivityStatsResponse200TopMediaItem,
        )

        d = dict(src_dict)
        total_searches = d.pop("totalSearches")

        total_exports = d.pop("totalExports")

        total_plays = d.pop("totalPlays")

        total_list_adds = d.pop("totalListAdds")

        streak_days = d.pop("streakDays")

        top_media = []
        _top_media = d.pop("topMedia")
        for top_media_item_data in _top_media:
            top_media_item = GetActivityStatsResponse200TopMediaItem.from_dict(top_media_item_data)

            top_media.append(top_media_item)

        get_activity_stats_response_200 = cls(
            total_searches=total_searches,
            total_exports=total_exports,
            total_plays=total_plays,
            total_list_adds=total_list_adds,
            streak_days=streak_days,
            top_media=top_media,
        )

        get_activity_stats_response_200.additional_properties = d
        return get_activity_stats_response_200

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
