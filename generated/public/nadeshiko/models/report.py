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

if TYPE_CHECKING:
    from ..models.report_data_type_0 import ReportDataType0
    from ..models.report_target_episode import ReportTargetEpisode
    from ..models.report_target_media import ReportTargetMedia
    from ..models.report_target_segment import ReportTargetSegment


T = TypeVar("T", bound="Report")


@_attrs_define
class Report:
    """
    Attributes:
        id (int): Report ID Example: 1.
        source (ReportSource): Who created this report Example: USER.
        target (ReportTargetEpisode | ReportTargetMedia | ReportTargetSegment):
        audit_run_id (int | None): ID of the audit run that created this report (AUTO only)
        reason (ReportReason): Reason for the report Example: WRONG_TRANSLATION.
        description (None | str): Optional description with additional details
        data (None | ReportDataType0): Check-specific metrics (AUTO reports) or null (USER reports)
        status (ReportStatus): Current status of the report Example: PENDING.
        admin_notes (None | str): Notes from the admin who reviewed the report
        user_id (int | None): ID of the user who submitted the report (USER reports only) Example: 42.
        created_at (datetime.datetime): When the report was created
        updated_at (datetime.datetime | None): When the report was last updated
    """

    id: int
    source: ReportSource
    target: ReportTargetEpisode | ReportTargetMedia | ReportTargetSegment
    audit_run_id: int | None
    reason: ReportReason
    description: None | str
    data: None | ReportDataType0
    status: ReportStatus
    admin_notes: None | str
    user_id: int | None
    created_at: datetime.datetime
    updated_at: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.report_data_type_0 import ReportDataType0
        from ..models.report_target_episode import ReportTargetEpisode
        from ..models.report_target_media import ReportTargetMedia

        id = self.id

        source = self.source.value

        target: dict[str, Any]
        if isinstance(self.target, ReportTargetMedia) or isinstance(
            self.target, ReportTargetEpisode
        ):
            target = self.target.to_dict()
        else:
            target = self.target.to_dict()

        audit_run_id: int | None
        audit_run_id = self.audit_run_id

        reason = self.reason.value

        description: None | str
        description = self.description

        data: dict[str, Any] | None
        if isinstance(self.data, ReportDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        status = self.status.value

        admin_notes: None | str
        admin_notes = self.admin_notes

        user_id: int | None
        user_id = self.user_id

        created_at = self.created_at.isoformat()

        updated_at: None | str
        if isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "source": source,
                "target": target,
                "auditRunId": audit_run_id,
                "reason": reason,
                "description": description,
                "data": data,
                "status": status,
                "adminNotes": admin_notes,
                "userId": user_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.report_data_type_0 import ReportDataType0
        from ..models.report_target_episode import ReportTargetEpisode
        from ..models.report_target_media import ReportTargetMedia
        from ..models.report_target_segment import ReportTargetSegment

        d = dict(src_dict)
        id = d.pop("id")

        source = ReportSource(d.pop("source"))

        def _parse_target(
            data: object,
        ) -> ReportTargetEpisode | ReportTargetMedia | ReportTargetSegment:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_report_target_type_0 = ReportTargetMedia.from_dict(data)

                return componentsschemas_report_target_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_report_target_type_1 = ReportTargetEpisode.from_dict(data)

                return componentsschemas_report_target_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_report_target_type_2 = ReportTargetSegment.from_dict(data)

            return componentsschemas_report_target_type_2

        target = _parse_target(d.pop("target"))

        def _parse_audit_run_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        audit_run_id = _parse_audit_run_id(d.pop("auditRunId"))

        reason = ReportReason(d.pop("reason"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_data(data: object) -> None | ReportDataType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = ReportDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReportDataType0, data)

        data = _parse_data(d.pop("data"))

        status = ReportStatus(d.pop("status"))

        def _parse_admin_notes(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        admin_notes = _parse_admin_notes(d.pop("adminNotes"))

        def _parse_user_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        user_id = _parse_user_id(d.pop("userId"))

        created_at = isoparse(d.pop("createdAt"))

        def _parse_updated_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        updated_at = _parse_updated_at(d.pop("updatedAt"))

        report = cls(
            id=id,
            source=source,
            target=target,
            audit_run_id=audit_run_id,
            reason=reason,
            description=description,
            data=data,
            status=status,
            admin_notes=admin_notes,
            user_id=user_id,
            created_at=created_at,
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
