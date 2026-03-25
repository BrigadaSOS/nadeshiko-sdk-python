from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.segment import Segment
    from ..models.segment_context_response_includes import SegmentContextResponseIncludes


T = TypeVar("T", bound="SegmentContextResponse")


@_attrs_define
class SegmentContextResponse:
    """
    Attributes:
        segments (list[Segment]):
        includes (SegmentContextResponseIncludes):
    """

    segments: list[Segment]
    includes: SegmentContextResponseIncludes
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        segments = []
        for segments_item_data in self.segments:
            segments_item = segments_item_data.to_dict()
            segments.append(segments_item)

        includes = self.includes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "segments": segments,
                "includes": includes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.segment import Segment
        from ..models.segment_context_response_includes import SegmentContextResponseIncludes

        _src = dict(src_dict)
        segments = []
        _segments = _src.pop("segments")
        for segments_item_data in _segments:
            segments_item = Segment.from_dict(segments_item_data)

            segments.append(segments_item)

        includes = SegmentContextResponseIncludes.from_dict(_src.pop("includes"))

        segment_context_response = cls(
            segments=segments,
            includes=includes,
        )

        segment_context_response.additional_properties = _src
        return segment_context_response

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
