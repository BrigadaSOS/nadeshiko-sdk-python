from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.report_reason import ReportReason
from ..models.report_source import ReportSource
from ..models.report_status import ReportStatus
from ..models.report_target_type import ReportTargetType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.report_data_type_0 import ReportDataType0


T = TypeVar("T", bound="Report")


@_attrs_define
class Report:
    """
    Attributes:
        id (int): Report ID Example: 1.
        source (ReportSource): Who created this report Example: USER.
        target_type (ReportTargetType): What level the report targets Example: SEGMENT.
        target_media_id (int): Media ID this report targets Example: 42.
        reason (ReportReason): Reason for the report Example: WRONG_TRANSLATION.
        status (ReportStatus): Current status of the report Example: PENDING.
        created_at (datetime.datetime): When the report was created
        target_episode_number (int | None | Unset): Episode number (for EPISODE/SEGMENT targets) Example: 5.
        target_segment_uuid (None | str | Unset): Segment UUID (for SEGMENT targets) Example: 3fd94cef-a3e1-31ae-
            bc8d-e743f03e9c7e.
        review_check_run_id (int | None | Unset): ID of the auto-check run that created this report (AUTO only)
        description (None | str | Unset): Optional description with additional details
        data (None | ReportDataType0 | Unset): Check-specific metrics (AUTO reports) or null (USER reports)
        admin_notes (None | str | Unset): Notes from the admin who reviewed the report
        user_id (int | None | Unset): ID of the user who submitted the report (USER reports only) Example: 42.
        updated_at (datetime.datetime | None | Unset): When the report was last updated
    """

    id: int
    source: ReportSource
    target_type: ReportTargetType
    target_media_id: int
    reason: ReportReason
    status: ReportStatus
    created_at: datetime.datetime
    target_episode_number: int | None | Unset = UNSET
    target_segment_uuid: None | str | Unset = UNSET
    review_check_run_id: int | None | Unset = UNSET
    description: None | str | Unset = UNSET
    data: None | ReportDataType0 | Unset = UNSET
    admin_notes: None | str | Unset = UNSET
    user_id: int | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.report_data_type_0 import ReportDataType0

        id = self.id

        source = self.source.value

        target_type = self.target_type.value

        target_media_id = self.target_media_id

        reason = self.reason.value

        status = self.status.value

        created_at = self.created_at.isoformat()

        target_episode_number: int | None | Unset
        if isinstance(self.target_episode_number, Unset):
            target_episode_number = UNSET
        else:
            target_episode_number = self.target_episode_number

        target_segment_uuid: None | str | Unset
        if isinstance(self.target_segment_uuid, Unset):
            target_segment_uuid = UNSET
        else:
            target_segment_uuid = self.target_segment_uuid

        review_check_run_id: int | None | Unset
        if isinstance(self.review_check_run_id, Unset):
            review_check_run_id = UNSET
        else:
            review_check_run_id = self.review_check_run_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, ReportDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        admin_notes: None | str | Unset
        if isinstance(self.admin_notes, Unset):
            admin_notes = UNSET
        else:
            admin_notes = self.admin_notes

        user_id: int | None | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "source": source,
                "targetType": target_type,
                "targetMediaId": target_media_id,
                "reason": reason,
                "status": status,
                "createdAt": created_at,
            }
        )
        if target_episode_number is not UNSET:
            field_dict["targetEpisodeNumber"] = target_episode_number
        if target_segment_uuid is not UNSET:
            field_dict["targetSegmentUuid"] = target_segment_uuid
        if review_check_run_id is not UNSET:
            field_dict["reviewCheckRunId"] = review_check_run_id
        if description is not UNSET:
            field_dict["description"] = description
        if data is not UNSET:
            field_dict["data"] = data
        if admin_notes is not UNSET:
            field_dict["adminNotes"] = admin_notes
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.report_data_type_0 import ReportDataType0

        d = dict(src_dict)
        id = d.pop("id")

        source = ReportSource(d.pop("source"))

        target_type = ReportTargetType(d.pop("targetType"))

        target_media_id = d.pop("targetMediaId")

        reason = ReportReason(d.pop("reason"))

        status = ReportStatus(d.pop("status"))

        created_at = isoparse(d.pop("createdAt"))

        def _parse_target_episode_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        target_episode_number = _parse_target_episode_number(d.pop("targetEpisodeNumber", UNSET))

        def _parse_target_segment_uuid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_segment_uuid = _parse_target_segment_uuid(d.pop("targetSegmentUuid", UNSET))

        def _parse_review_check_run_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        review_check_run_id = _parse_review_check_run_id(d.pop("reviewCheckRunId", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_data(data: object) -> None | ReportDataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = ReportDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReportDataType0 | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_admin_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        admin_notes = _parse_admin_notes(d.pop("adminNotes", UNSET))

        def _parse_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_id = _parse_user_id(d.pop("userId", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))

        report = cls(
            id=id,
            source=source,
            target_type=target_type,
            target_media_id=target_media_id,
            reason=reason,
            status=status,
            created_at=created_at,
            target_episode_number=target_episode_number,
            target_segment_uuid=target_segment_uuid,
            review_check_run_id=review_check_run_id,
            description=description,
            data=data,
            admin_notes=admin_notes,
            user_id=user_id,
            updated_at=updated_at,
        )

        report.additional_properties = d
        return report

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
