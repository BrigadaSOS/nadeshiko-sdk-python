from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_admin_dashboard_collections_response_200_by_type_and_visibility_item import (
        GetAdminDashboardCollectionsResponse200ByTypeAndVisibilityItem,
    )
    from ..models.get_admin_dashboard_collections_response_200_top_collections_item import (
        GetAdminDashboardCollectionsResponse200TopCollectionsItem,
    )


T = TypeVar("T", bound="GetAdminDashboardCollectionsResponse200")


@_attrs_define
class GetAdminDashboardCollectionsResponse200:
    """
    Attributes:
        total_collections (int):
        by_type_and_visibility (list[GetAdminDashboardCollectionsResponse200ByTypeAndVisibilityItem]):
        average_size (float):
        top_collections (list[GetAdminDashboardCollectionsResponse200TopCollectionsItem]):
    """

    total_collections: int
    by_type_and_visibility: list[GetAdminDashboardCollectionsResponse200ByTypeAndVisibilityItem]
    average_size: float
    top_collections: list[GetAdminDashboardCollectionsResponse200TopCollectionsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_collections = self.total_collections

        by_type_and_visibility = []
        for by_type_and_visibility_item_data in self.by_type_and_visibility:
            by_type_and_visibility_item = by_type_and_visibility_item_data.to_dict()
            by_type_and_visibility.append(by_type_and_visibility_item)

        average_size = self.average_size

        top_collections = []
        for top_collections_item_data in self.top_collections:
            top_collections_item = top_collections_item_data.to_dict()
            top_collections.append(top_collections_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalCollections": total_collections,
                "byTypeAndVisibility": by_type_and_visibility,
                "averageSize": average_size,
                "topCollections": top_collections,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_admin_dashboard_collections_response_200_by_type_and_visibility_item import (
            GetAdminDashboardCollectionsResponse200ByTypeAndVisibilityItem,
        )
        from ..models.get_admin_dashboard_collections_response_200_top_collections_item import (
            GetAdminDashboardCollectionsResponse200TopCollectionsItem,
        )

        d = dict(src_dict)
        total_collections = d.pop("totalCollections")

        by_type_and_visibility = []
        _by_type_and_visibility = d.pop("byTypeAndVisibility")
        for by_type_and_visibility_item_data in _by_type_and_visibility:
            by_type_and_visibility_item = (
                GetAdminDashboardCollectionsResponse200ByTypeAndVisibilityItem.from_dict(
                    by_type_and_visibility_item_data
                )
            )

            by_type_and_visibility.append(by_type_and_visibility_item)

        average_size = d.pop("averageSize")

        top_collections = []
        _top_collections = d.pop("topCollections")
        for top_collections_item_data in _top_collections:
            top_collections_item = (
                GetAdminDashboardCollectionsResponse200TopCollectionsItem.from_dict(
                    top_collections_item_data
                )
            )

            top_collections.append(top_collections_item)

        get_admin_dashboard_collections_response_200 = cls(
            total_collections=total_collections,
            by_type_and_visibility=by_type_and_visibility,
            average_size=average_size,
            top_collections=top_collections,
        )

        get_admin_dashboard_collections_response_200.additional_properties = d
        return get_admin_dashboard_collections_response_200

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
