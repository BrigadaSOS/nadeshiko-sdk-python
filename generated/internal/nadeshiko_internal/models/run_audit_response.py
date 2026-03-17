from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.run_audit_response_checks_run_item import RunAuditResponseChecksRunItem


T = TypeVar("T", bound="RunAuditResponse")


@_attrs_define
class RunAuditResponse:
    """
    Attributes:
        category (None | str): Category filter used
        checks_run (list[RunAuditResponseChecksRunItem]):
        total_reports (int): Total reports created across all audits
    """

    category: None | str
    checks_run: list[RunAuditResponseChecksRunItem]
    total_reports: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category: None | str
        category = self.category

        checks_run = []
        for checks_run_item_data in self.checks_run:
            checks_run_item = checks_run_item_data.to_dict()
            checks_run.append(checks_run_item)

        total_reports = self.total_reports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "checksRun": checks_run,
                "totalReports": total_reports,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_audit_response_checks_run_item import RunAuditResponseChecksRunItem

        d = dict(src_dict)

        def _parse_category(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        category = _parse_category(d.pop("category"))

        checks_run = []
        _checks_run = d.pop("checksRun")
        for checks_run_item_data in _checks_run:
            checks_run_item = RunAuditResponseChecksRunItem.from_dict(checks_run_item_data)

            checks_run.append(checks_run_item)

        total_reports = d.pop("totalReports")

        run_audit_response = cls(
            category=category,
            checks_run=checks_run,
            total_reports=total_reports,
        )

        run_audit_response.additional_properties = d
        return run_audit_response

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
