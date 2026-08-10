from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.moderate_episode_segments_request_action import (
    ModerateEpisodeSegmentsRequestAction,
    check_moderate_episode_segments_request_action,
)
from ..models.segment_status import SegmentStatus, check_segment_status
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModerateEpisodeSegmentsRequest")


@_attrs_define
class ModerateEpisodeSegmentsRequest:
    """
    Attributes:
        action (ModerateEpisodeSegmentsRequestAction): Which bulk action to apply
        max_affected (int): Refuse the request if the episode has more segments than this.

            There is no safe default, so it is required: the right ceiling depends on
            whether a person is about to review the result. The request is rejected
            whole — a cap smaller than the episode changes nothing rather than applying
            to the first N segments.
             Example: 500.
        offset_ms (int | Unset): Milliseconds to shift every segment by; negative moves clips earlier.
            Required for `shiftTimings`, ignored otherwise.
             Example: -1200.
        status (SegmentStatus | Unset): Segment status Example: ACTIVE.
        report_id (int | Unset): The report this action answers, recorded on every revision it writes Example: 4821.
    """

    action: ModerateEpisodeSegmentsRequestAction
    max_affected: int
    offset_ms: int | Unset = UNSET
    status: SegmentStatus | Unset = UNSET
    report_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action: str = self.action

        max_affected = self.max_affected

        offset_ms = self.offset_ms

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        report_id = self.report_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "maxAffected": max_affected,
            }
        )
        if offset_ms is not UNSET:
            field_dict["offsetMs"] = offset_ms
        if status is not UNSET:
            field_dict["status"] = status
        if report_id is not UNSET:
            field_dict["reportId"] = report_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        action = check_moderate_episode_segments_request_action(_src.pop("action"))

        max_affected = _src.pop("maxAffected")

        offset_ms = _src.pop("offsetMs", UNSET)

        _status = _src.pop("status", UNSET)
        status: SegmentStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_segment_status(_status)

        report_id = _src.pop("reportId", UNSET)

        moderate_episode_segments_request = cls(
            action=action,
            max_affected=max_affected,
            offset_ms=offset_ms,
            status=status,
            report_id=report_id,
        )

        moderate_episode_segments_request.additional_properties = _src
        return moderate_episode_segments_request

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
