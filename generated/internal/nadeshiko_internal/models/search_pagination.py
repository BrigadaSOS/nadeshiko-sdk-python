from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_pagination_estimated_total_hits_relation import (
    SearchPaginationEstimatedTotalHitsRelation,
)

T = TypeVar("T", bound="SearchPagination")


@_attrs_define
class SearchPagination:
    """Pagination metadata for search results

    Attributes:
        has_more (bool): Whether there are more results after this page Example: True.
        estimated_total_hits (int): Estimated total number of matching segments Example: 12456.
        estimated_total_hits_relation (SearchPaginationEstimatedTotalHitsRelation): Whether `estimatedTotalHits` is
            exact or a lower bound.
            - `EXACT`: the value is the precise total
            - `AT_LEAST`: at least this many matches exist (true total may be higher)
             Example: AT_LEAST.
        cursor (None | str): Opaque cursor token to pass on the next request to fetch the following page
    """

    has_more: bool
    estimated_total_hits: int
    estimated_total_hits_relation: SearchPaginationEstimatedTotalHitsRelation
    cursor: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        has_more = self.has_more

        estimated_total_hits = self.estimated_total_hits

        estimated_total_hits_relation = self.estimated_total_hits_relation.value

        cursor: None | str
        cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hasMore": has_more,
                "estimatedTotalHits": estimated_total_hits,
                "estimatedTotalHitsRelation": estimated_total_hits_relation,
                "cursor": cursor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        has_more = _src.pop("hasMore")

        estimated_total_hits = _src.pop("estimatedTotalHits")

        estimated_total_hits_relation = SearchPaginationEstimatedTotalHitsRelation(
            _src.pop("estimatedTotalHitsRelation")
        )

        def _parse_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cursor = _parse_cursor(_src.pop("cursor"))

        search_pagination = cls(
            has_more=has_more,
            estimated_total_hits=estimated_total_hits,
            estimated_total_hits_relation=estimated_total_hits_relation,
            cursor=cursor,
        )

        search_pagination.additional_properties = _src
        return search_pagination

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
