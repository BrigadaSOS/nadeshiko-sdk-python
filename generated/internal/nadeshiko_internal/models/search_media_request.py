from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_media_filters import SearchMediaFilters


T = TypeVar("T", bound="SearchMediaRequest")


@_attrs_define
class SearchMediaRequest:
    """
    Attributes:
        query (str): Search term to match against media names (English, Japanese, romaji) Example: steins.
        take (int | Unset): Maximum number of results to return Default: 10.
        filters (SearchMediaFilters | Unset): Filters for narrowing media search results
    """

    query: str
    take: int | Unset = 10
    filters: SearchMediaFilters | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        take = self.take

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if take is not UNSET:
            field_dict["take"] = take
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_media_filters import SearchMediaFilters

        _src = dict(src_dict)
        query = _src.pop("query")

        take = _src.pop("take", UNSET)

        _filters = _src.pop("filters", UNSET)
        filters: SearchMediaFilters | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = SearchMediaFilters.from_dict(_filters)

        search_media_request = cls(
            query=query,
            take=take,
            filters=filters,
        )

        search_media_request.additional_properties = _src
        return search_media_request

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
