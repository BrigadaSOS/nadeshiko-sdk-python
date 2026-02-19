from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.include_expansion import IncludeExpansion
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_filters import SearchFilters
    from ..models.search_request_query import SearchRequestQuery
    from ..models.search_request_sort import SearchRequestSort


T = TypeVar("T", bound="SearchRequest")


@_attrs_define
class SearchRequest:
    """
    Attributes:
        query (SearchRequestQuery | Unset): What to search for (omit for queryless browse)
        limit (int | Unset): Max amount of entries by response Default: 10.
        cursor (list[float] | Unset): Current page of search Example: [23.31727, 7].
        sort (SearchRequestSort | Unset): Sort configuration
        filters (SearchFilters | Unset): Search filters for narrowing segment results
        include (list[IncludeExpansion] | Unset): Resources to expand in the response includes block
    """

    query: SearchRequestQuery | Unset = UNSET
    limit: int | Unset = 10
    cursor: list[float] | Unset = UNSET
    sort: SearchRequestSort | Unset = UNSET
    filters: SearchFilters | Unset = UNSET
    include: list[IncludeExpansion] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        limit = self.limit

        cursor: list[float] | Unset = UNSET
        if not isinstance(self.cursor, Unset):
            cursor = self.cursor

        sort: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort.to_dict()

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
        if limit is not UNSET:
            field_dict["limit"] = limit
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if sort is not UNSET:
            field_dict["sort"] = sort
        if filters is not UNSET:
            field_dict["filters"] = filters
        if include is not UNSET:
            field_dict["include"] = include

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_filters import SearchFilters
        from ..models.search_request_query import SearchRequestQuery
        from ..models.search_request_sort import SearchRequestSort

        d = dict(src_dict)
        _query = d.pop("query", UNSET)
        query: SearchRequestQuery | Unset
        if isinstance(_query, Unset):
            query = UNSET
        else:
            query = SearchRequestQuery.from_dict(_query)

        limit = d.pop("limit", UNSET)

        cursor = cast(list[float], d.pop("cursor", UNSET))

        _sort = d.pop("sort", UNSET)
        sort: SearchRequestSort | Unset
        if isinstance(_sort, Unset):
            sort = UNSET
        else:
            sort = SearchRequestSort.from_dict(_sort)

        _filters = d.pop("filters", UNSET)
        filters: SearchFilters | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = SearchFilters.from_dict(_filters)

        _include = d.pop("include", UNSET)
        include: list[IncludeExpansion] | Unset = UNSET
        if _include is not UNSET:
            include = []
            for include_item_data in _include:
                include_item = IncludeExpansion(include_item_data)

                include.append(include_item)

        search_request = cls(
            query=query,
            limit=limit,
            cursor=cursor,
            sort=sort,
            filters=filters,
            include=include,
        )

        search_request.additional_properties = d
        return search_request

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
