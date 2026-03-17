from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_admin_dashboard_response_200_activity_daily_activity_30d_item import (
        GetAdminDashboardResponse200ActivityDailyActivity30DItem,
    )
    from ..models.get_admin_dashboard_response_200_activity_top_queries_7d_item import (
        GetAdminDashboardResponse200ActivityTopQueries7DItem,
    )


T = TypeVar("T", bound="GetAdminDashboardResponse200Activity")


@_attrs_define
class GetAdminDashboardResponse200Activity:
    """
    Attributes:
        total_searches (int):
        total_exports (int):
        total_plays (int):
        total_collection_adds (int):
        active_searchers_7_d (int): Unique users who searched in the last 7 days
        top_queries_7_d (list[GetAdminDashboardResponse200ActivityTopQueries7DItem]):
        daily_activity_30_d (list[GetAdminDashboardResponse200ActivityDailyActivity30DItem]):
    """

    total_searches: int
    total_exports: int
    total_plays: int
    total_collection_adds: int
    active_searchers_7_d: int
    top_queries_7_d: list[GetAdminDashboardResponse200ActivityTopQueries7DItem]
    daily_activity_30_d: list[GetAdminDashboardResponse200ActivityDailyActivity30DItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_searches = self.total_searches

        total_exports = self.total_exports

        total_plays = self.total_plays

        total_collection_adds = self.total_collection_adds

        active_searchers_7_d = self.active_searchers_7_d

        top_queries_7_d = []
        for top_queries_7_d_item_data in self.top_queries_7_d:
            top_queries_7_d_item = top_queries_7_d_item_data.to_dict()
            top_queries_7_d.append(top_queries_7_d_item)

        daily_activity_30_d = []
        for daily_activity_30_d_item_data in self.daily_activity_30_d:
            daily_activity_30_d_item = daily_activity_30_d_item_data.to_dict()
            daily_activity_30_d.append(daily_activity_30_d_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalSearches": total_searches,
                "totalExports": total_exports,
                "totalPlays": total_plays,
                "totalCollectionAdds": total_collection_adds,
                "activeSearchers7d": active_searchers_7_d,
                "topQueries7d": top_queries_7_d,
                "dailyActivity30d": daily_activity_30_d,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_admin_dashboard_response_200_activity_daily_activity_30d_item import (
            GetAdminDashboardResponse200ActivityDailyActivity30DItem,
        )
        from ..models.get_admin_dashboard_response_200_activity_top_queries_7d_item import (
            GetAdminDashboardResponse200ActivityTopQueries7DItem,
        )

        d = dict(src_dict)
        total_searches = d.pop("totalSearches")

        total_exports = d.pop("totalExports")

        total_plays = d.pop("totalPlays")

        total_collection_adds = d.pop("totalCollectionAdds")

        active_searchers_7_d = d.pop("activeSearchers7d")

        top_queries_7_d = []
        _top_queries_7_d = d.pop("topQueries7d")
        for top_queries_7_d_item_data in _top_queries_7_d:
            top_queries_7_d_item = GetAdminDashboardResponse200ActivityTopQueries7DItem.from_dict(
                top_queries_7_d_item_data
            )

            top_queries_7_d.append(top_queries_7_d_item)

        daily_activity_30_d = []
        _daily_activity_30_d = d.pop("dailyActivity30d")
        for daily_activity_30_d_item_data in _daily_activity_30_d:
            daily_activity_30_d_item = (
                GetAdminDashboardResponse200ActivityDailyActivity30DItem.from_dict(
                    daily_activity_30_d_item_data
                )
            )

            daily_activity_30_d.append(daily_activity_30_d_item)

        get_admin_dashboard_response_200_activity = cls(
            total_searches=total_searches,
            total_exports=total_exports,
            total_plays=total_plays,
            total_collection_adds=total_collection_adds,
            active_searchers_7_d=active_searchers_7_d,
            top_queries_7_d=top_queries_7_d,
            daily_activity_30_d=daily_activity_30_d,
        )

        get_admin_dashboard_response_200_activity.additional_properties = d
        return get_admin_dashboard_response_200_activity

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
