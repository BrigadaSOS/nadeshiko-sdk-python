from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetAdminDashboardOverviewResponse200ActivityDailyActivityItem")


@_attrs_define
class GetAdminDashboardOverviewResponse200ActivityDailyActivityItem:
    """
    Attributes:
        date (str):
        count (int):
    """

    date: str
    count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date")

        count = d.pop("count")

        get_admin_dashboard_overview_response_200_activity_daily_activity_item = cls(
            date=date,
            count=count,
        )

        get_admin_dashboard_overview_response_200_activity_daily_activity_item.additional_properties = d
        return get_admin_dashboard_overview_response_200_activity_daily_activity_item

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
