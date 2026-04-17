from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.report_reason import ReportReason
from ..models.report_source import ReportSource

T = TypeVar("T", bound="AdminReportGroupItem")


@_attrs_define
class AdminReportGroupItem:
    """
    Attributes:
        id (int): Report ID
        reason (ReportReason): Reason for the report Example: WRONG_TRANSLATION.
        description (None | str): Optional description with additional details
        source (ReportSource): Origin of the report Example: USER.
        reporter_name (str): Name of the reporter
        created_at (datetime.datetime): When the report was created
        admin_notes (None | str): Notes from the admin who reviewed the report
    """

    id: int
    reason: ReportReason
    description: None | str
    source: ReportSource
    reporter_name: str
    created_at: datetime.datetime
    admin_notes: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        reason = self.reason.value

        description: None | str
        description = self.description

        source = self.source.value

        reporter_name = self.reporter_name

        created_at = self.created_at.isoformat()

        admin_notes: None | str
        admin_notes = self.admin_notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "reason": reason,
                "description": description,
                "source": source,
                "reporterName": reporter_name,
                "createdAt": created_at,
                "adminNotes": admin_notes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        id = _src.pop("id")

        reason = ReportReason(_src.pop("reason"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(_src.pop("description"))

        source = ReportSource(_src.pop("source"))

        reporter_name = _src.pop("reporterName")

        created_at = isoparse(_src.pop("createdAt"))

        def _parse_admin_notes(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        admin_notes = _parse_admin_notes(_src.pop("adminNotes"))

        admin_report_group_item = cls(
            id=id,
            reason=reason,
            description=description,
            source=source,
            reporter_name=reporter_name,
            created_at=created_at,
            admin_notes=admin_notes,
        )

        admin_report_group_item.additional_properties = _src
        return admin_report_group_item

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
