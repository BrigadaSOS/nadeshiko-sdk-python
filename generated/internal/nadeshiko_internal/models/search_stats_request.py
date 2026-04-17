from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.include_expansion import IncludeExpansion
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_filters import SearchFilters
    from ..models.search_query import SearchQuery


T = TypeVar("T", bound="SearchStatsRequest")


@_attrs_define
class SearchStatsRequest:
    """Stats request. All fields are optional — omit `query` to get filter counts for the full corpus.

    Attributes:
        query (SearchQuery | Unset): What to search for (omit for queryless browse/stats)
        filters (SearchFilters | Unset): Search filters for narrowing segment results
        include (list[IncludeExpansion] | Unset): Optional resources to expand in the response `includes` block
    """

    query: SearchQuery | Unset = UNSET
    filters: SearchFilters | Unset = UNSET
    include: list[IncludeExpansion] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        include: list[str] | Unset = UNSET
        if not isinstance(self.include, Unset):
            include = []
            for include_item_data in self.include:
                include_item = include_item_data.value
                include.append(include_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query is not UNSET:
            field_dict["query"] = query
        if filters is not UNSET:
            field_dict["filters"] = filters
        if include is not UNSET:
            field_dict["include"] = include

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_filters import SearchFilters
        from ..models.search_query import SearchQuery

        _src = dict(src_dict)
        _query = _src.pop("query", UNSET)
        query: SearchQuery | Unset
        if isinstance(_query, Unset):
            query = UNSET
        else:
            query = SearchQuery.from_dict(_query)

        _filters = _src.pop("filters", UNSET)
        filters: SearchFilters | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = SearchFilters.from_dict(_filters)

        _include = _src.pop("include", UNSET)
        include: list[IncludeExpansion] | Unset = UNSET
        if _include is not UNSET:
            include = []
            for include_item_data in _include:
                include_item = IncludeExpansion(include_item_data)

                include.append(include_item)

        search_stats_request = cls(
            query=query,
            filters=filters,
            include=include,
        )

        search_stats_request.additional_properties = _src
        return search_stats_request

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
