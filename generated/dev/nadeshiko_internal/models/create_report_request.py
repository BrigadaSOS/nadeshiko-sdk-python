from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_report_request_reason import CreateReportRequestReason
from ..models.create_report_request_target_type import CreateReportRequestTargetType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateReportRequest")


@_attrs_define
class CreateReportRequest:
    """
    Attributes:
        target_type (CreateReportRequestTargetType): Type of the entity being reported Example: SEGMENT.
        target_media_id (int): Media ID of the reported entity Example: 42.
        reason (CreateReportRequestReason): Reason for the report Example: WRONG_TRANSLATION.
        target_segment_uuid (str | Unset): Segment UUID (required when targetType is SEGMENT) Example:
            3fd94cef-a3e1-31ae-bc8d-e743f03e9c7e.
        description (str | Unset): Optional description with additional details Example: The translation doesn't match
            the spoken Japanese.
    """

    target_type: CreateReportRequestTargetType
    target_media_id: int
    reason: CreateReportRequestReason
    target_segment_uuid: str | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_type = self.target_type.value

        target_media_id = self.target_media_id

        reason = self.reason.value

        target_segment_uuid = self.target_segment_uuid

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "targetType": target_type,
                "targetMediaId": target_media_id,
                "reason": reason,
            }
        )
        if target_segment_uuid is not UNSET:
            field_dict["targetSegmentUuid"] = target_segment_uuid
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_type = CreateReportRequestTargetType(d.pop("targetType"))

        target_media_id = d.pop("targetMediaId")

        reason = CreateReportRequestReason(d.pop("reason"))

        target_segment_uuid = d.pop("targetSegmentUuid", UNSET)

        description = d.pop("description", UNSET)

        create_report_request = cls(
            target_type=target_type,
            target_media_id=target_media_id,
            reason=reason,
            target_segment_uuid=target_segment_uuid,
            description=description,
        )

        create_report_request.additional_properties = d
        return create_report_request

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
