from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetAdminDashboardCollectionsResponse200TopCollectionsItem")


@_attrs_define
class GetAdminDashboardCollectionsResponse200TopCollectionsItem:
    """
    Attributes:
        id (int):
        name (str):
        type_ (str):
        visibility (str):
        segment_count (int):
    """

    id: int
    name: str
    type_: str
    visibility: str
    segment_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_ = self.type_

        visibility = self.visibility

        segment_count = self.segment_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type_,
                "visibility": visibility,
                "segmentCount": segment_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        type_ = d.pop("type")

        visibility = d.pop("visibility")

        segment_count = d.pop("segmentCount")

        get_admin_dashboard_collections_response_200_top_collections_item = cls(
            id=id,
            name=name,
            type_=type_,
            visibility=visibility,
            segment_count=segment_count,
        )

        get_admin_dashboard_collections_response_200_top_collections_item.additional_properties = d
        return get_admin_dashboard_collections_response_200_top_collections_item

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
