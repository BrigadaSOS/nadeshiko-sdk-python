from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_admin_dashboard_activity_response_200_daily_activity_by_type_item import (
        GetAdminDashboardActivityResponse200DailyActivityByTypeItem,
    )
    from ..models.get_admin_dashboard_activity_response_200_daily_exports_item import (
        GetAdminDashboardActivityResponse200DailyExportsItem,
    )
    from ..models.get_admin_dashboard_activity_response_200_top_exported_media_item import (
        GetAdminDashboardActivityResponse200TopExportedMediaItem,
    )
    from ..models.get_admin_dashboard_activity_response_200_top_searches_item import (
        GetAdminDashboardActivityResponse200TopSearchesItem,
    )


T = TypeVar("T", bound="GetAdminDashboardActivityResponse200")


@_attrs_define
class GetAdminDashboardActivityResponse200:
    """
    Attributes:
        daily_activity_by_type (list[GetAdminDashboardActivityResponse200DailyActivityByTypeItem]):
        top_searches (list[GetAdminDashboardActivityResponse200TopSearchesItem]):
        daily_exports (list[GetAdminDashboardActivityResponse200DailyExportsItem]):
        top_exported_media (list[GetAdminDashboardActivityResponse200TopExportedMediaItem]):
    """

    daily_activity_by_type: list[GetAdminDashboardActivityResponse200DailyActivityByTypeItem]
    top_searches: list[GetAdminDashboardActivityResponse200TopSearchesItem]
    daily_exports: list[GetAdminDashboardActivityResponse200DailyExportsItem]
    top_exported_media: list[GetAdminDashboardActivityResponse200TopExportedMediaItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        daily_activity_by_type = []
        for daily_activity_by_type_item_data in self.daily_activity_by_type:
            daily_activity_by_type_item = daily_activity_by_type_item_data.to_dict()
            daily_activity_by_type.append(daily_activity_by_type_item)

        top_searches = []
        for top_searches_item_data in self.top_searches:
            top_searches_item = top_searches_item_data.to_dict()
            top_searches.append(top_searches_item)

        daily_exports = []
        for daily_exports_item_data in self.daily_exports:
            daily_exports_item = daily_exports_item_data.to_dict()
            daily_exports.append(daily_exports_item)

        top_exported_media = []
        for top_exported_media_item_data in self.top_exported_media:
            top_exported_media_item = top_exported_media_item_data.to_dict()
            top_exported_media.append(top_exported_media_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dailyActivityByType": daily_activity_by_type,
                "topSearches": top_searches,
                "dailyExports": daily_exports,
                "topExportedMedia": top_exported_media,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_admin_dashboard_activity_response_200_daily_activity_by_type_item import (
            GetAdminDashboardActivityResponse200DailyActivityByTypeItem,
        )
        from ..models.get_admin_dashboard_activity_response_200_daily_exports_item import (
            GetAdminDashboardActivityResponse200DailyExportsItem,
        )
        from ..models.get_admin_dashboard_activity_response_200_top_exported_media_item import (
            GetAdminDashboardActivityResponse200TopExportedMediaItem,
        )
        from ..models.get_admin_dashboard_activity_response_200_top_searches_item import (
            GetAdminDashboardActivityResponse200TopSearchesItem,
        )

        _src = dict(src_dict)
        daily_activity_by_type = []
        _daily_activity_by_type = _src.pop("dailyActivityByType")
        for daily_activity_by_type_item_data in _daily_activity_by_type:
            daily_activity_by_type_item = (
                GetAdminDashboardActivityResponse200DailyActivityByTypeItem.from_dict(
                    daily_activity_by_type_item_data
                )
            )

            daily_activity_by_type.append(daily_activity_by_type_item)

        top_searches = []
        _top_searches = _src.pop("topSearches")
        for top_searches_item_data in _top_searches:
            top_searches_item = GetAdminDashboardActivityResponse200TopSearchesItem.from_dict(
                top_searches_item_data
            )

            top_searches.append(top_searches_item)

        daily_exports = []
        _daily_exports = _src.pop("dailyExports")
        for daily_exports_item_data in _daily_exports:
            daily_exports_item = GetAdminDashboardActivityResponse200DailyExportsItem.from_dict(
                daily_exports_item_data
            )

            daily_exports.append(daily_exports_item)

        top_exported_media = []
        _top_exported_media = _src.pop("topExportedMedia")
        for top_exported_media_item_data in _top_exported_media:
            top_exported_media_item = (
                GetAdminDashboardActivityResponse200TopExportedMediaItem.from_dict(
                    top_exported_media_item_data
                )
            )

            top_exported_media.append(top_exported_media_item)

        get_admin_dashboard_activity_response_200 = cls(
            daily_activity_by_type=daily_activity_by_type,
            top_searches=top_searches,
            daily_exports=daily_exports,
            top_exported_media=top_exported_media,
        )

        get_admin_dashboard_activity_response_200.additional_properties = _src
        return get_admin_dashboard_activity_response_200

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
