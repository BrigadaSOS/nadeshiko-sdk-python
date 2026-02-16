from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_activity import UserActivity
    from ..models.user_export_show_response_200_lists_item import UserExportShowResponse200ListsItem
    from ..models.user_export_show_response_200_profile import UserExportShowResponse200Profile
    from ..models.user_export_show_response_200_reports_item import (
        UserExportShowResponse200ReportsItem,
    )
    from ..models.user_preferences import UserPreferences


T = TypeVar("T", bound="UserExportShowResponse200")


@_attrs_define
class UserExportShowResponse200:
    """
    Attributes:
        profile (UserExportShowResponse200Profile):
        preferences (UserPreferences):
        activity (list[UserActivity]):
        lists (list[UserExportShowResponse200ListsItem]):
        reports (list[UserExportShowResponse200ReportsItem]):
    """

    profile: UserExportShowResponse200Profile
    preferences: UserPreferences
    activity: list[UserActivity]
    lists: list[UserExportShowResponse200ListsItem]
    reports: list[UserExportShowResponse200ReportsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile = self.profile.to_dict()

        preferences = self.preferences.to_dict()

        activity = []
        for activity_item_data in self.activity:
            activity_item = activity_item_data.to_dict()
            activity.append(activity_item)

        lists = []
        for lists_item_data in self.lists:
            lists_item = lists_item_data.to_dict()
            lists.append(lists_item)

        reports = []
        for reports_item_data in self.reports:
            reports_item = reports_item_data.to_dict()
            reports.append(reports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "profile": profile,
                "preferences": preferences,
                "activity": activity,
                "lists": lists,
                "reports": reports,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_activity import UserActivity
        from ..models.user_export_show_response_200_lists_item import (
            UserExportShowResponse200ListsItem,
        )
        from ..models.user_export_show_response_200_profile import UserExportShowResponse200Profile
        from ..models.user_export_show_response_200_reports_item import (
            UserExportShowResponse200ReportsItem,
        )
        from ..models.user_preferences import UserPreferences

        d = dict(src_dict)
        profile = UserExportShowResponse200Profile.from_dict(d.pop("profile"))

        preferences = UserPreferences.from_dict(d.pop("preferences"))

        activity = []
        _activity = d.pop("activity")
        for activity_item_data in _activity:
            activity_item = UserActivity.from_dict(activity_item_data)

            activity.append(activity_item)

        lists = []
        _lists = d.pop("lists")
        for lists_item_data in _lists:
            lists_item = UserExportShowResponse200ListsItem.from_dict(lists_item_data)

            lists.append(lists_item)

        reports = []
        _reports = d.pop("reports")
        for reports_item_data in _reports:
            reports_item = UserExportShowResponse200ReportsItem.from_dict(reports_item_data)

            reports.append(reports_item)

        user_export_show_response_200 = cls(
            profile=profile,
            preferences=preferences,
            activity=activity,
            lists=lists,
            reports=reports,
        )

        user_export_show_response_200.additional_properties = d
        return user_export_show_response_200

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
