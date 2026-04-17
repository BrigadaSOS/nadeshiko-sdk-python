from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cursor_pagination import CursorPagination
    from ..models.media_audit_run import MediaAuditRun


T = TypeVar("T", bound="ListAdminMediaAuditRunsResponse200")


@_attrs_define
class ListAdminMediaAuditRunsResponse200:
    """
    Attributes:
        runs (list[MediaAuditRun]):
        pagination (CursorPagination): Opaque cursor pagination metadata
    """

    runs: list[MediaAuditRun]
    pagination: CursorPagination
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        runs = []
        for runs_item_data in self.runs:
            runs_item = runs_item_data.to_dict()
            runs.append(runs_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "runs": runs,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cursor_pagination import CursorPagination
        from ..models.media_audit_run import MediaAuditRun

        _src = dict(src_dict)
        runs = []
        _runs = _src.pop("runs")
        for runs_item_data in _runs:
            runs_item = MediaAuditRun.from_dict(runs_item_data)

            runs.append(runs_item)

        pagination = CursorPagination.from_dict(_src.pop("pagination"))

        list_admin_media_audit_runs_response_200 = cls(
            runs=runs,
            pagination=pagination,
        )

        list_admin_media_audit_runs_response_200.additional_properties = _src
        return list_admin_media_audit_runs_response_200

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
