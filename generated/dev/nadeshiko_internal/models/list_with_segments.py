from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_with_segments_type import ListWithSegmentsType
from ..models.list_with_segments_visibility import ListWithSegmentsVisibility

if TYPE_CHECKING:
    from ..models.list_with_segments_segments_item import ListWithSegmentsSegmentsItem


T = TypeVar("T", bound="ListWithSegments")


@_attrs_define
class ListWithSegments:
    """List with saved segments (search result format)

    Attributes:
        id (int): List ID Example: 123.
        name (str): Name of the list Example: Study Favorites.
        type_ (ListWithSegmentsType): Type of list Example: SEGMENT.
        user_id (int): User ID who owns the list Example: 1.
        visibility (ListWithSegmentsVisibility): Visibility of the list Example: PRIVATE.
        segments (list[ListWithSegmentsSegmentsItem]): Saved segments with their search result data
        total_count (int): Total number of segments in the list Example: 42.
    """

    id: int
    name: str
    type_: ListWithSegmentsType
    user_id: int
    visibility: ListWithSegmentsVisibility
    segments: list[ListWithSegmentsSegmentsItem]
    total_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_ = self.type_.value

        user_id = self.user_id

        visibility = self.visibility.value

        segments = []
        for segments_item_data in self.segments:
            segments_item = segments_item_data.to_dict()
            segments.append(segments_item)

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type_,
                "userId": user_id,
                "visibility": visibility,
                "segments": segments,
                "totalCount": total_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_with_segments_segments_item import ListWithSegmentsSegmentsItem

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        type_ = ListWithSegmentsType(d.pop("type"))

        user_id = d.pop("userId")

        visibility = ListWithSegmentsVisibility(d.pop("visibility"))

        segments = []
        _segments = d.pop("segments")
        for segments_item_data in _segments:
            segments_item = ListWithSegmentsSegmentsItem.from_dict(segments_item_data)

            segments.append(segments_item)

        total_count = d.pop("totalCount")

        list_with_segments = cls(
            id=id,
            name=name,
            type_=type_,
            user_id=user_id,
            visibility=visibility,
            segments=segments,
            total_count=total_count,
        )

        list_with_segments.additional_properties = d
        return list_with_segments

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
