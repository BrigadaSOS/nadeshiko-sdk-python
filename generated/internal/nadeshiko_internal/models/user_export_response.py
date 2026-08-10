from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.report import Report
    from ..models.user_activity import UserActivity
    from ..models.user_export_collection import UserExportCollection
    from ..models.user_export_response_profile import UserExportResponseProfile
    from ..models.user_export_response_truncated import UserExportResponseTruncated
    from ..models.user_preferences import UserPreferences


T = TypeVar("T", bound="UserExportResponse")


@_attrs_define
class UserExportResponse:
    """User data export payload (identifier-oriented references)

    Attributes:
        truncated (UserExportResponseTruncated): Which sections were cut short. The export is assembled and returned as
            a single JSON
            body, so each section has a ceiling: 50000 activity entries, 5000 reports, 1000
            collections, and 50000 collection segment references in total. A `true` here means more
            data exists than the response carries.
        profile (UserExportResponseProfile):
        preferences (UserPreferences):
        activity (list[UserActivity]):
        collections (list[UserExportCollection]):
        reports (list[Report]):
    """

    truncated: UserExportResponseTruncated
    profile: UserExportResponseProfile
    preferences: UserPreferences
    activity: list[UserActivity]
    collections: list[UserExportCollection]
    reports: list[Report]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        truncated = self.truncated.to_dict()

        profile = self.profile.to_dict()

        preferences = self.preferences.to_dict()

        activity = []
        for activity_item_data in self.activity:
            activity_item = activity_item_data.to_dict()
            activity.append(activity_item)

        collections = []
        for collections_item_data in self.collections:
            collections_item = collections_item_data.to_dict()
            collections.append(collections_item)

        reports = []
        for reports_item_data in self.reports:
            reports_item = reports_item_data.to_dict()
            reports.append(reports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "truncated": truncated,
                "profile": profile,
                "preferences": preferences,
                "activity": activity,
                "collections": collections,
                "reports": reports,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.report import Report
        from ..models.user_activity import UserActivity
        from ..models.user_export_collection import UserExportCollection
        from ..models.user_export_response_profile import UserExportResponseProfile
        from ..models.user_export_response_truncated import UserExportResponseTruncated
        from ..models.user_preferences import UserPreferences

        _src = dict(src_dict)
        truncated = UserExportResponseTruncated.from_dict(_src.pop("truncated"))

        profile = UserExportResponseProfile.from_dict(_src.pop("profile"))

        preferences = UserPreferences.from_dict(_src.pop("preferences"))

        activity = []
        _activity = _src.pop("activity")
        for activity_item_data in _activity:
            activity_item = UserActivity.from_dict(activity_item_data)

            activity.append(activity_item)

        collections = []
        _collections = _src.pop("collections")
        for collections_item_data in _collections:
            collections_item = UserExportCollection.from_dict(collections_item_data)

            collections.append(collections_item)

        reports = []
        _reports = _src.pop("reports")
        for reports_item_data in _reports:
            reports_item = Report.from_dict(reports_item_data)

            reports.append(reports_item)

        user_export_response = cls(
            truncated=truncated,
            profile=profile,
            preferences=preferences,
            activity=activity,
            collections=collections,
            reports=reports,
        )

        user_export_response.additional_properties = _src
        return user_export_response

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
