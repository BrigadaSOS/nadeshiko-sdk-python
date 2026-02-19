from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

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
        media_id (int): Media ID this report targets Example: 42.
        segment_uuid (str): Segment UUID this report targets Example: 3fd94cef-a3e1-31ae-bc8d-e743f03e9c7e.
        episode_number (int | Unset): Episode number containing the segment Example: 5.
    """

    type_: ReportTargetSegmentType
    media_id: int
    segment_uuid: str
    episode_number: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        media_id = self.media_id

        segment_uuid = self.segment_uuid

        episode_number = self.episode_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "mediaId": media_id,
                "segmentUuid": segment_uuid,
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

        segment_uuid = d.pop("segmentUuid")

        episode_number = d.pop("episodeNumber", UNSET)

        report_target_segment = cls(
            type_=type_,
            media_id=media_id,
            segment_uuid=segment_uuid,
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
