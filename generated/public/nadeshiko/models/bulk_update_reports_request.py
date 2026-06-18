from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.report_status import ReportStatus, check_report_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_update_reports_request_filters import BulkUpdateReportsRequestFilters


T = TypeVar("T", bound="BulkUpdateReportsRequest")


@_attrs_define
class BulkUpdateReportsRequest:
    """
    Attributes:
        status (ReportStatus): Current status of a report Example: OPEN.
        admin_notes (str | Unset): Optional admin notes to set on all matching reports
        filters (BulkUpdateReportsRequestFilters | Unset): Filters to select which reports to update. If omitted,
            updates all reports.
    """

    status: ReportStatus
    admin_notes: str | Unset = UNSET
    filters: BulkUpdateReportsRequestFilters | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str = self.status

        admin_notes = self.admin_notes

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if admin_notes is not UNSET:
            field_dict["adminNotes"] = admin_notes
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_update_reports_request_filters import BulkUpdateReportsRequestFilters

        _src = dict(src_dict)
        status = check_report_status(_src.pop("status"))

        admin_notes = _src.pop("adminNotes", UNSET)

        _filters = _src.pop("filters", UNSET)
        filters: BulkUpdateReportsRequestFilters | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = BulkUpdateReportsRequestFilters.from_dict(_filters)

        bulk_update_reports_request = cls(
            status=status,
            admin_notes=admin_notes,
            filters=filters,
        )

        bulk_update_reports_request.additional_properties = _src
        return bulk_update_reports_request

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
