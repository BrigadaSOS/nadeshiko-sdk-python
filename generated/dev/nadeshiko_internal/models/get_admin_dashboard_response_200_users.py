from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetAdminDashboardResponse200Users")


@_attrs_define
class GetAdminDashboardResponse200Users:
    """
    Attributes:
        total_users (int):
        recently_registered_count (int): Users registered in the last 30 days
        recently_active_count (int): Users active in the last 30 days
    """

    total_users: int
    recently_registered_count: int
    recently_active_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_users = self.total_users

        recently_registered_count = self.recently_registered_count

        recently_active_count = self.recently_active_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalUsers": total_users,
                "recentlyRegisteredCount": recently_registered_count,
                "recentlyActiveCount": recently_active_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_users = d.pop("totalUsers")

        recently_registered_count = d.pop("recentlyRegisteredCount")

        recently_active_count = d.pop("recentlyActiveCount")

        get_admin_dashboard_response_200_users = cls(
            total_users=total_users,
            recently_registered_count=recently_registered_count,
            recently_active_count=recently_active_count,
        )

        get_admin_dashboard_response_200_users.additional_properties = d
        return get_admin_dashboard_response_200_users

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
