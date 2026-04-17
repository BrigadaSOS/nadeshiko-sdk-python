from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_delete_reports_request_filters import BulkDeleteReportsRequestFilters


T = TypeVar("T", bound="BulkDeleteReportsRequest")


@_attrs_define
class BulkDeleteReportsRequest:
    """
    Attributes:
        filters (BulkDeleteReportsRequestFilters | Unset): Filters to select which reports to delete. If omitted,
            deletes all reports.
    """

    filters: BulkDeleteReportsRequestFilters | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_delete_reports_request_filters import BulkDeleteReportsRequestFilters

        _src = dict(src_dict)
        _filters = _src.pop("filters", UNSET)
        filters: BulkDeleteReportsRequestFilters | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = BulkDeleteReportsRequestFilters.from_dict(_filters)

        bulk_delete_reports_request = cls(
            filters=filters,
        )

        bulk_delete_reports_request.additional_properties = _src
        return bulk_delete_reports_request

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
