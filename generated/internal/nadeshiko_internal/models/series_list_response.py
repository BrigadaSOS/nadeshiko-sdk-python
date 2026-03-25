from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.opaque_cursor_pagination import OpaqueCursorPagination
    from ..models.series import Series


T = TypeVar("T", bound="SeriesListResponse")


@_attrs_define
class SeriesListResponse:
    """
    Attributes:
        series (list[Series]):
        pagination (OpaqueCursorPagination): Opaque cursor pagination metadata
    """

    series: list[Series]
    pagination: OpaqueCursorPagination
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        series = []
        for series_item_data in self.series:
            series_item = series_item_data.to_dict()
            series.append(series_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "series": series,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.opaque_cursor_pagination import OpaqueCursorPagination
        from ..models.series import Series

        _src = dict(src_dict)
        series = []
        _series = _src.pop("series")
        for series_item_data in _series:
            series_item = Series.from_dict(series_item_data)

            series.append(series_item)

        pagination = OpaqueCursorPagination.from_dict(_src.pop("pagination"))

        series_list_response = cls(
            series=series,
            pagination=pagination,
        )

        series_list_response.additional_properties = _src
        return series_list_response

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
