from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.report_status import ReportStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchUpdateReportsRequest")


@_attrs_define
class BatchUpdateReportsRequest:
    """
    Attributes:
        ids (list[int]): Report IDs to update Example: [1, 2, 3].
        status (ReportStatus): Current status of a report Example: OPEN.
        admin_notes (str | Unset): Optional admin notes to set on all selected reports
    """

    ids: list[int]
    status: ReportStatus
    admin_notes: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ids = self.ids

        status = self.status.value

        admin_notes = self.admin_notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ids": ids,
                "status": status,
            }
        )
        if admin_notes is not UNSET:
            field_dict["adminNotes"] = admin_notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        ids = cast(list[int], _src.pop("ids"))

        status = ReportStatus(_src.pop("status"))

        admin_notes = _src.pop("adminNotes", UNSET)

        batch_update_reports_request = cls(
            ids=ids,
            status=status,
            admin_notes=admin_notes,
        )

        batch_update_reports_request.additional_properties = _src
        return batch_update_reports_request

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
