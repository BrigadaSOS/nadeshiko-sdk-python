from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.admin_report_group import AdminReportGroup
    from ..models.cursor_pagination import CursorPagination


T = TypeVar("T", bound="AdminReportListResponse")


@_attrs_define
class AdminReportListResponse:
    """
    Attributes:
        groups (list[AdminReportGroup]):
        pagination (CursorPagination): Opaque cursor pagination metadata
    """

    groups: list[AdminReportGroup]
    pagination: CursorPagination
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        groups = []
        for groups_item_data in self.groups:
            groups_item = groups_item_data.to_dict()
            groups.append(groups_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "groups": groups,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admin_report_group import AdminReportGroup
        from ..models.cursor_pagination import CursorPagination

        _src = dict(src_dict)
        groups = []
        _groups = _src.pop("groups")
        for groups_item_data in _groups:
            groups_item = AdminReportGroup.from_dict(groups_item_data)

            groups.append(groups_item)

        pagination = CursorPagination.from_dict(_src.pop("pagination"))

        admin_report_list_response = cls(
            groups=groups,
            pagination=pagination,
        )

        admin_report_list_response.additional_properties = _src
        return admin_report_list_response

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
