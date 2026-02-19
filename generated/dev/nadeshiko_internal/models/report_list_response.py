from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cursor_pagination import CursorPagination
    from ..models.report import Report


T = TypeVar("T", bound="ReportListResponse")


@_attrs_define
class ReportListResponse:
    """
    Attributes:
        reports (list[Report]):
        pagination (CursorPagination): Cursor pagination metadata
    """

    reports: list[Report]
    pagination: CursorPagination
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reports = []
        for reports_item_data in self.reports:
            reports_item = reports_item_data.to_dict()
            reports.append(reports_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reports": reports,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cursor_pagination import CursorPagination
        from ..models.report import Report

        d = dict(src_dict)
        reports = []
        _reports = d.pop("reports")
        for reports_item_data in _reports:
            reports_item = Report.from_dict(reports_item_data)

            reports.append(reports_item)

        pagination = CursorPagination.from_dict(d.pop("pagination"))

        report_list_response = cls(
            reports=reports,
            pagination=pagination,
        )

        report_list_response.additional_properties = d
        return report_list_response

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
