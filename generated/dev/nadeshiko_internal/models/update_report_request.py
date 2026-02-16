from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_report_request_status import UpdateReportRequestStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateReportRequest")


@_attrs_define
class UpdateReportRequest:
    """
    Attributes:
        status (UpdateReportRequestStatus | Unset): New status for the report Example: ACCEPTED.
        admin_notes (str | Unset): Admin notes about the report Example: Confirmed wrong translation, will fix.
    """

    status: UpdateReportRequestStatus | Unset = UNSET
    admin_notes: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        admin_notes = self.admin_notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if admin_notes is not UNSET:
            field_dict["adminNotes"] = admin_notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: UpdateReportRequestStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = UpdateReportRequestStatus(_status)

        admin_notes = d.pop("adminNotes", UNSET)

        update_report_request = cls(
            status=status,
            admin_notes=admin_notes,
        )

        update_report_request.additional_properties = d
        return update_report_request

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
