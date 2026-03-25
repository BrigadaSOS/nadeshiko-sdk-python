from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetAdminDashboardMediaResponse200TopMediaBySearchesItem")


@_attrs_define
class GetAdminDashboardMediaResponse200TopMediaBySearchesItem:
    """
    Attributes:
        media_id (int):
        media_name (str):
        count (int):
    """

    media_id: int
    media_name: str
    count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media_id = self.media_id

        media_name = self.media_name

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mediaId": media_id,
                "mediaName": media_name,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        media_id = _src.pop("mediaId")

        media_name = _src.pop("mediaName")

        count = _src.pop("count")

        get_admin_dashboard_media_response_200_top_media_by_searches_item = cls(
            media_id=media_id,
            media_name=media_name,
            count=count,
        )

        get_admin_dashboard_media_response_200_top_media_by_searches_item.additional_properties = (
            _src
        )
        return get_admin_dashboard_media_response_200_top_media_by_searches_item

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
