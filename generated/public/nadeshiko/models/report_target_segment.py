from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.report_target_segment_type import ReportTargetSegmentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportTargetSegment")


@_attrs_define
class ReportTargetSegment:
    """
    Attributes:
        type_ (ReportTargetSegmentType): Report target type Example: SEGMENT.
        media_id (str): Public ID of the media this report targets Example: V1StGXR8_Z5d.
        segment_id (None | str): Segment public ID or UUID Example: abc123xyz.
        episode_number (int | Unset): Episode number containing the segment Example: 5.
    """

    type_: ReportTargetSegmentType
    media_id: str
    segment_id: None | str
    episode_number: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        media_id = self.media_id

        segment_id: None | str
        segment_id = self.segment_id

        episode_number = self.episode_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "mediaId": media_id,
                "segmentId": segment_id,
            }
        )
        if episode_number is not UNSET:
            field_dict["episodeNumber"] = episode_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = ReportTargetSegmentType(d.pop("type"))

        media_id = d.pop("mediaId")

        def _parse_segment_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        segment_id = _parse_segment_id(d.pop("segmentId"))

        episode_number = d.pop("episodeNumber", UNSET)

        report_target_segment = cls(
            type_=type_,
            media_id=media_id,
            segment_id=segment_id,
            episode_number=episode_number,
        )

        report_target_segment.additional_properties = d
        return report_target_segment

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
