from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_admin_dashboard_response_200_activity import (
        GetAdminDashboardResponse200Activity,
    )
    from ..models.get_admin_dashboard_response_200_media import GetAdminDashboardResponse200Media
    from ..models.get_admin_dashboard_response_200_system import GetAdminDashboardResponse200System
    from ..models.get_admin_dashboard_response_200_users import GetAdminDashboardResponse200Users


T = TypeVar("T", bound="GetAdminDashboardResponse200")


@_attrs_define
class GetAdminDashboardResponse200:
    """
    Attributes:
        media (GetAdminDashboardResponse200Media):
        users (GetAdminDashboardResponse200Users):
        activity (GetAdminDashboardResponse200Activity):
        system (GetAdminDashboardResponse200System):
    """

    media: GetAdminDashboardResponse200Media
    users: GetAdminDashboardResponse200Users
    activity: GetAdminDashboardResponse200Activity
    system: GetAdminDashboardResponse200System
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media = self.media.to_dict()

        users = self.users.to_dict()

        activity = self.activity.to_dict()

        system = self.system.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "media": media,
                "users": users,
                "activity": activity,
                "system": system,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_admin_dashboard_response_200_activity import (
            GetAdminDashboardResponse200Activity,
        )
        from ..models.get_admin_dashboard_response_200_media import (
            GetAdminDashboardResponse200Media,
        )
        from ..models.get_admin_dashboard_response_200_system import (
            GetAdminDashboardResponse200System,
        )
        from ..models.get_admin_dashboard_response_200_users import (
            GetAdminDashboardResponse200Users,
        )

        _src = dict(src_dict)
        media = GetAdminDashboardResponse200Media.from_dict(_src.pop("media"))

        users = GetAdminDashboardResponse200Users.from_dict(_src.pop("users"))

        activity = GetAdminDashboardResponse200Activity.from_dict(_src.pop("activity"))

        system = GetAdminDashboardResponse200System.from_dict(_src.pop("system"))

        get_admin_dashboard_response_200 = cls(
            media=media,
            users=users,
            activity=activity,
            system=system,
        )

        get_admin_dashboard_response_200.additional_properties = _src
        return get_admin_dashboard_response_200

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
