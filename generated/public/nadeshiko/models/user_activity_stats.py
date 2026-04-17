from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_activity_stats_top_media_item import UserActivityStatsTopMediaItem


T = TypeVar("T", bound="UserActivityStats")


@_attrs_define
class UserActivityStats:
    """Aggregate statistics about a user's activity

    Attributes:
        total_searches (int):  Example: 1240.
        total_exports (int):  Example: 82.
        total_plays (int):  Example: 3400.
        total_list_adds (int):  Example: 58.
        total_shares (int):  Example: 17.
        top_media (list[UserActivityStatsTopMediaItem]):
    """

    total_searches: int
    total_exports: int
    total_plays: int
    total_list_adds: int
    total_shares: int
    top_media: list[UserActivityStatsTopMediaItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_searches = self.total_searches

        total_exports = self.total_exports

        total_plays = self.total_plays

        total_list_adds = self.total_list_adds

        total_shares = self.total_shares

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
                "totalShares": total_shares,
                "topMedia": top_media,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_activity_stats_top_media_item import UserActivityStatsTopMediaItem

        _src = dict(src_dict)
        total_searches = _src.pop("totalSearches")

        total_exports = _src.pop("totalExports")

        total_plays = _src.pop("totalPlays")

        total_list_adds = _src.pop("totalListAdds")

        total_shares = _src.pop("totalShares")

        top_media = []
        _top_media = _src.pop("topMedia")
        for top_media_item_data in _top_media:
            top_media_item = UserActivityStatsTopMediaItem.from_dict(top_media_item_data)

            top_media.append(top_media_item)

        user_activity_stats = cls(
            total_searches=total_searches,
            total_exports=total_exports,
            total_plays=total_plays,
            total_list_adds=total_list_adds,
            total_shares=total_shares,
            top_media=top_media,
        )

        user_activity_stats.additional_properties = _src
        return user_activity_stats

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
