from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pagination_info import PaginationInfo
    from ..models.search_result import SearchResult


T = TypeVar("T", bound="SearchHealthCheckResponse")


@_attrs_define
class SearchHealthCheckResponse:
    """
    Attributes:
        results (list[SearchResult] | Unset):
        pagination (PaginationInfo | Unset): Pagination metadata for search results
        cursor (list[float] | Unset): Cursor for pagination
    """

    results: list[SearchResult] | Unset = UNSET
    pagination: PaginationInfo | Unset = UNSET
    cursor: list[float] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        pagination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        cursor: list[float] | Unset = UNSET
        if not isinstance(self.cursor, Unset):
            cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if results is not UNSET:
            field_dict["results"] = results
        if pagination is not UNSET:
            field_dict["pagination"] = pagination
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination_info import PaginationInfo
        from ..models.search_result import SearchResult

        d = dict(src_dict)
        _results = d.pop("results", UNSET)
        results: list[SearchResult] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = SearchResult.from_dict(results_item_data)

                results.append(results_item)

        _pagination = d.pop("pagination", UNSET)
        pagination: PaginationInfo | Unset
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = PaginationInfo.from_dict(_pagination)

        cursor = cast(list[float], d.pop("cursor", UNSET))

        search_health_check_response = cls(
            results=results,
            pagination=pagination,
            cursor=cursor,
        )

        search_health_check_response.additional_properties = d
        return search_health_check_response

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
