from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_admin_dashboard_overview_response_200_activity_daily_activity_item import (
        GetAdminDashboardOverviewResponse200ActivityDailyActivityItem,
    )


T = TypeVar("T", bound="GetAdminDashboardOverviewResponse200Activity")


@_attrs_define
class GetAdminDashboardOverviewResponse200Activity:
    """
    Attributes:
        total_searches (int):
        total_exports (int):
        total_plays (int):
        total_shares (int):
        active_searchers_7_d (int): Unique users who searched in the last 7 days
        daily_activity (list[GetAdminDashboardOverviewResponse200ActivityDailyActivityItem]):
    """

    total_searches: int
    total_exports: int
    total_plays: int
    total_shares: int
    active_searchers_7_d: int
    daily_activity: list[GetAdminDashboardOverviewResponse200ActivityDailyActivityItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_searches = self.total_searches

        total_exports = self.total_exports

        total_plays = self.total_plays

        total_shares = self.total_shares

        active_searchers_7_d = self.active_searchers_7_d

        daily_activity = []
        for daily_activity_item_data in self.daily_activity:
            daily_activity_item = daily_activity_item_data.to_dict()
            daily_activity.append(daily_activity_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalSearches": total_searches,
                "totalExports": total_exports,
                "totalPlays": total_plays,
                "totalShares": total_shares,
                "activeSearchers7d": active_searchers_7_d,
                "dailyActivity": daily_activity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_admin_dashboard_overview_response_200_activity_daily_activity_item import (
            GetAdminDashboardOverviewResponse200ActivityDailyActivityItem,
        )

        _src = dict(src_dict)
        total_searches = _src.pop("totalSearches")

        total_exports = _src.pop("totalExports")

        total_plays = _src.pop("totalPlays")

        total_shares = _src.pop("totalShares")

        active_searchers_7_d = _src.pop("activeSearchers7d")

        daily_activity = []
        _daily_activity = _src.pop("dailyActivity")
        for daily_activity_item_data in _daily_activity:
            daily_activity_item = (
                GetAdminDashboardOverviewResponse200ActivityDailyActivityItem.from_dict(
                    daily_activity_item_data
                )
            )

            daily_activity.append(daily_activity_item)

        get_admin_dashboard_overview_response_200_activity = cls(
            total_searches=total_searches,
            total_exports=total_exports,
            total_plays=total_plays,
            total_shares=total_shares,
            active_searchers_7_d=active_searchers_7_d,
            daily_activity=daily_activity,
        )

        get_admin_dashboard_overview_response_200_activity.additional_properties = _src
        return get_admin_dashboard_overview_response_200_activity

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
