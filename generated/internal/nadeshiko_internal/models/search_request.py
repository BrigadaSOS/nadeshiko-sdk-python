from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.include_expansion import IncludeExpansion, check_include_expansion
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_filters import SearchFilters
    from ..models.search_query import SearchQuery
    from ..models.search_sort import SearchSort


T = TypeVar("T", bound="SearchRequest")


@_attrs_define
class SearchRequest:
    """Search request. All fields are optional — omit `query` for queryless browse (segments matching filters only).

    Attributes:
        query (SearchQuery | Unset): What to search for (omit for queryless browse/stats)
        take (int | Unset): Max number of entries per response Default: 10.
        cursor (str | Unset): Opaque cursor token returned from the previous search page Example: eyJraW...N119.
        sort (SearchSort | Unset): Sort configuration
        prefer_media (list[str] | Unset): Public IDs of titles the caller wants first, used **only** to break ties.

            Segments Elasticsearch ranked equally are reordered so the ones from these
            titles come first; nothing crosses a rank boundary. Which segments land on
            a page, how many there are and the cursor that walks to the next one are
            all exactly what they would have been without this field — only the order
            within an already-tied run changes.

            Sent by the web client for a signed-in reader, from the titles they have
            favourited and the ones their activity says they know. Ignored unless
            `sort.mode` is `RELEVANCE`, since every other mode sorts on a key the
            caller asked for by name. Unknown IDs are ignored rather than rejected.
             Example: ['V1StGXR8_Z5d'].
        filters (SearchFilters | Unset): Search filters for narrowing segment results
        include (list[IncludeExpansion] | Unset): Optional resources to expand in the response `includes` block
    """

    query: SearchQuery | Unset = UNSET
    take: int | Unset = 10
    cursor: str | Unset = UNSET
    sort: SearchSort | Unset = UNSET
    prefer_media: list[str] | Unset = UNSET
    filters: SearchFilters | Unset = UNSET
    include: list[IncludeExpansion] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        take = self.take

        cursor = self.cursor

        sort: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort.to_dict()

        prefer_media: list[str] | Unset = UNSET
        if not isinstance(self.prefer_media, Unset):
            prefer_media = self.prefer_media

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        include: list[str] | Unset = UNSET
        if not isinstance(self.include, Unset):
            include = []
            for include_item_data in self.include:
                include_item: str = include_item_data
                include.append(include_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query is not UNSET:
            field_dict["query"] = query
        if take is not UNSET:
            field_dict["take"] = take
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if sort is not UNSET:
            field_dict["sort"] = sort
        if prefer_media is not UNSET:
            field_dict["preferMedia"] = prefer_media
        if filters is not UNSET:
            field_dict["filters"] = filters
        if include is not UNSET:
            field_dict["include"] = include

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_filters import SearchFilters
        from ..models.search_query import SearchQuery
        from ..models.search_sort import SearchSort

        _src = dict(src_dict)
        _query = _src.pop("query", UNSET)
        query: SearchQuery | Unset
        if isinstance(_query, Unset):
            query = UNSET
        else:
            query = SearchQuery.from_dict(_query)

        take = _src.pop("take", UNSET)

        cursor = _src.pop("cursor", UNSET)

        _sort = _src.pop("sort", UNSET)
        sort: SearchSort | Unset
        if isinstance(_sort, Unset):
            sort = UNSET
        else:
            sort = SearchSort.from_dict(_sort)

        prefer_media = cast(list[str], _src.pop("preferMedia", UNSET))

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
                include_item = check_include_expansion(include_item_data)

                include.append(include_item)

        search_request = cls(
            query=query,
            take=take,
            cursor=cursor,
            sort=sort,
            prefer_media=prefer_media,
            filters=filters,
            include=include,
        )

        search_request.additional_properties = _src
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
