from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RunAuditResponseChecksRunItem")


@_attrs_define
class RunAuditResponseChecksRunItem:
    """
    Attributes:
        audit_name (str): Audit identifier
        label (str): Human-readable audit name
        result_count (int): Number of reports created
        run_id (int): ID of the created run record
    """

    audit_name: str
    label: str
    result_count: int
    run_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audit_name = self.audit_name

        label = self.label

        result_count = self.result_count

        run_id = self.run_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "auditName": audit_name,
                "label": label,
                "resultCount": result_count,
                "runId": run_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        audit_name = d.pop("auditName")

        label = d.pop("label")

        result_count = d.pop("resultCount")

        run_id = d.pop("runId")

        run_audit_response_checks_run_item = cls(
            audit_name=audit_name,
            label=label,
            result_count=result_count,
            run_id=run_id,
        )

        run_audit_response_checks_run_item.additional_properties = d
        return run_audit_response_checks_run_item

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
