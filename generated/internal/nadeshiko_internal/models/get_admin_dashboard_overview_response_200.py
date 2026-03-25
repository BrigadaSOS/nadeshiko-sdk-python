from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_admin_dashboard_overview_response_200_activity import (
        GetAdminDashboardOverviewResponse200Activity,
    )
    from ..models.get_admin_dashboard_overview_response_200_media import (
        GetAdminDashboardOverviewResponse200Media,
    )
    from ..models.get_admin_dashboard_overview_response_200_users import (
        GetAdminDashboardOverviewResponse200Users,
    )


T = TypeVar("T", bound="GetAdminDashboardOverviewResponse200")


@_attrs_define
class GetAdminDashboardOverviewResponse200:
    """
    Attributes:
        media (GetAdminDashboardOverviewResponse200Media):
        users (GetAdminDashboardOverviewResponse200Users):
        activity (GetAdminDashboardOverviewResponse200Activity):
    """

    media: GetAdminDashboardOverviewResponse200Media
    users: GetAdminDashboardOverviewResponse200Users
    activity: GetAdminDashboardOverviewResponse200Activity
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media = self.media.to_dict()

        users = self.users.to_dict()

        activity = self.activity.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "media": media,
                "users": users,
                "activity": activity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_admin_dashboard_overview_response_200_activity import (
            GetAdminDashboardOverviewResponse200Activity,
        )
        from ..models.get_admin_dashboard_overview_response_200_media import (
            GetAdminDashboardOverviewResponse200Media,
        )
        from ..models.get_admin_dashboard_overview_response_200_users import (
            GetAdminDashboardOverviewResponse200Users,
        )

        _src = dict(src_dict)
        media = GetAdminDashboardOverviewResponse200Media.from_dict(_src.pop("media"))

        users = GetAdminDashboardOverviewResponse200Users.from_dict(_src.pop("users"))

        activity = GetAdminDashboardOverviewResponse200Activity.from_dict(_src.pop("activity"))

        get_admin_dashboard_overview_response_200 = cls(
            media=media,
            users=users,
            activity=activity,
        )

        get_admin_dashboard_overview_response_200.additional_properties = _src
        return get_admin_dashboard_overview_response_200

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
