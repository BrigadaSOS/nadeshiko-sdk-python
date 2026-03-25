from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetUserActivityStatsResponse200TopMediaItem")


@_attrs_define
class GetUserActivityStatsResponse200TopMediaItem:
    """
    Attributes:
        media_id (int):
        count (int):
    """

    media_id: int
    count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media_id = self.media_id

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mediaId": media_id,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        media_id = _src.pop("mediaId")

        count = _src.pop("count")

        get_user_activity_stats_response_200_top_media_item = cls(
            media_id=media_id,
            count=count,
        )

        get_user_activity_stats_response_200_top_media_item.additional_properties = _src
        return get_user_activity_stats_response_200_top_media_item

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
