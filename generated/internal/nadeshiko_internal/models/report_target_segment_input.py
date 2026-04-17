from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.report_target_segment_input_type import ReportTargetSegmentInputType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportTargetSegmentInput")


@_attrs_define
class ReportTargetSegmentInput:
    """
    Attributes:
        type_ (ReportTargetSegmentInputType): Report target type Example: SEGMENT.
        media_public_id (str): publicId of the media this report targets Example: V1StGXR8_Z5d.
        segment_public_id (str): Segment publicId Example: abc123def456.
        episode_number (int | Unset): Episode number containing the segment Example: 5.
    """

    type_: ReportTargetSegmentInputType
    media_public_id: str
    segment_public_id: str
    episode_number: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        media_public_id = self.media_public_id

        segment_public_id = self.segment_public_id

        episode_number = self.episode_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "mediaPublicId": media_public_id,
                "segmentPublicId": segment_public_id,
            }
        )
        if episode_number is not UNSET:
            field_dict["episodeNumber"] = episode_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        type_ = ReportTargetSegmentInputType(_src.pop("type"))

        media_public_id = _src.pop("mediaPublicId")

        segment_public_id = _src.pop("segmentPublicId")

        episode_number = _src.pop("episodeNumber", UNSET)

        report_target_segment_input = cls(
            type_=type_,
            media_public_id=media_public_id,
            segment_public_id=segment_public_id,
            episode_number=episode_number,
        )

        report_target_segment_input.additional_properties = _src
        return report_target_segment_input

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
