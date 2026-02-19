from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cursor_pagination import CursorPagination
    from ..models.segment import Segment


T = TypeVar("T", bound="ListSegmentsResponse200")


@_attrs_define
class ListSegmentsResponse200:
    """
    Attributes:
        segments (list[Segment]): Array of segment objects
        pagination (CursorPagination): Cursor pagination metadata
    """

    segments: list[Segment]
    pagination: CursorPagination
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        segments = []
        for segments_item_data in self.segments:
            segments_item = segments_item_data.to_dict()
            segments.append(segments_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "segments": segments,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cursor_pagination import CursorPagination
        from ..models.segment import Segment

        d = dict(src_dict)
        segments = []
        _segments = d.pop("segments")
        for segments_item_data in _segments:
            segments_item = Segment.from_dict(segments_item_data)

            segments.append(segments_item)

        pagination = CursorPagination.from_dict(d.pop("pagination"))

        list_segments_response_200 = cls(
            segments=segments,
            pagination=pagination,
        )

        list_segments_response_200.additional_properties = d
        return list_segments_response_200

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
