from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.admin_dashboard_show_response_200_activity import (
        AdminDashboardShowResponse200Activity,
    )
    from ..models.admin_dashboard_show_response_200_media import AdminDashboardShowResponse200Media
    from ..models.admin_dashboard_show_response_200_system import (
        AdminDashboardShowResponse200System,
    )
    from ..models.admin_dashboard_show_response_200_users import AdminDashboardShowResponse200Users


T = TypeVar("T", bound="AdminDashboardShowResponse200")


@_attrs_define
class AdminDashboardShowResponse200:
    """
    Attributes:
        media (AdminDashboardShowResponse200Media):
        users (AdminDashboardShowResponse200Users):
        activity (AdminDashboardShowResponse200Activity):
        system (AdminDashboardShowResponse200System):
    """

    media: AdminDashboardShowResponse200Media
    users: AdminDashboardShowResponse200Users
    activity: AdminDashboardShowResponse200Activity
    system: AdminDashboardShowResponse200System
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
        from ..models.admin_dashboard_show_response_200_activity import (
            AdminDashboardShowResponse200Activity,
        )
        from ..models.admin_dashboard_show_response_200_media import (
            AdminDashboardShowResponse200Media,
        )
        from ..models.admin_dashboard_show_response_200_system import (
            AdminDashboardShowResponse200System,
        )
        from ..models.admin_dashboard_show_response_200_users import (
            AdminDashboardShowResponse200Users,
        )

        d = dict(src_dict)
        media = AdminDashboardShowResponse200Media.from_dict(d.pop("media"))

        users = AdminDashboardShowResponse200Users.from_dict(d.pop("users"))

        activity = AdminDashboardShowResponse200Activity.from_dict(d.pop("activity"))

        system = AdminDashboardShowResponse200System.from_dict(d.pop("system"))

        admin_dashboard_show_response_200 = cls(
            media=media,
            users=users,
            activity=activity,
            system=system,
        )

        admin_dashboard_show_response_200.additional_properties = d
        return admin_dashboard_show_response_200

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
