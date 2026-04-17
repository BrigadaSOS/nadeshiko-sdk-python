from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.report_source import ReportSource
from ..models.report_target_type import ReportTargetType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkUpdateReportsRequestFilters")


@_attrs_define
class BulkUpdateReportsRequestFilters:
    """Filters to select which reports to update. If omitted, updates all reports.

    Attributes:
        status (str | Unset): Filter by current report status. Accepts a single value or comma-separated list (e.g.
            "OPEN,PROCESSING").
        source (ReportSource | Unset): Origin of the report Example: USER.
        target_type (ReportTargetType | Unset): Kind of entity a report is about Example: SEGMENT.
        target_media_id (int | Unset): Filter by target media ID
        target_episode_number (int | Unset): Filter by target episode number
        target_segment_id (int | Unset): Filter by target segment ID
        audit_run_id (int | Unset): Filter by audit run ID
        orphaned (bool | Unset): Only update reports whose target media no longer exists
    """

    status: str | Unset = UNSET
    source: ReportSource | Unset = UNSET
    target_type: ReportTargetType | Unset = UNSET
    target_media_id: int | Unset = UNSET
    target_episode_number: int | Unset = UNSET
    target_segment_id: int | Unset = UNSET
    audit_run_id: int | Unset = UNSET
    orphaned: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        target_type: str | Unset = UNSET
        if not isinstance(self.target_type, Unset):
            target_type = self.target_type.value

        target_media_id = self.target_media_id

        target_episode_number = self.target_episode_number

        target_segment_id = self.target_segment_id

        audit_run_id = self.audit_run_id

        orphaned = self.orphaned

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if source is not UNSET:
            field_dict["source"] = source
        if target_type is not UNSET:
            field_dict["targetType"] = target_type
        if target_media_id is not UNSET:
            field_dict["targetMediaId"] = target_media_id
        if target_episode_number is not UNSET:
            field_dict["targetEpisodeNumber"] = target_episode_number
        if target_segment_id is not UNSET:
            field_dict["targetSegmentId"] = target_segment_id
        if audit_run_id is not UNSET:
            field_dict["auditRunId"] = audit_run_id
        if orphaned is not UNSET:
            field_dict["orphaned"] = orphaned

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        status = _src.pop("status", UNSET)

        _source = _src.pop("source", UNSET)
        source: ReportSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = ReportSource(_source)

        _target_type = _src.pop("targetType", UNSET)
        target_type: ReportTargetType | Unset
        if isinstance(_target_type, Unset):
            target_type = UNSET
        else:
            target_type = ReportTargetType(_target_type)

        target_media_id = _src.pop("targetMediaId", UNSET)

        target_episode_number = _src.pop("targetEpisodeNumber", UNSET)

        target_segment_id = _src.pop("targetSegmentId", UNSET)

        audit_run_id = _src.pop("auditRunId", UNSET)

        orphaned = _src.pop("orphaned", UNSET)

        bulk_update_reports_request_filters = cls(
            status=status,
            source=source,
            target_type=target_type,
            target_media_id=target_media_id,
            target_episode_number=target_episode_number,
            target_segment_id=target_segment_id,
            audit_run_id=audit_run_id,
            orphaned=orphaned,
        )

        bulk_update_reports_request_filters.additional_properties = _src
        return bulk_update_reports_request_filters

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
