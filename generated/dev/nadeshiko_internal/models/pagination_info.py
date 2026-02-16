from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pagination_info_estimated_total_hits_relation import (
    PaginationInfoEstimatedTotalHitsRelation,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PaginationInfo")


@_attrs_define
class PaginationInfo:
    """Pagination metadata for search results

    Attributes:
        page_size (int | Unset): Number of results returned in this page Example: 20.
        has_more (bool | Unset): Whether there are more results after this page Example: True.
        estimated_total_hits (int | Unset): Estimated total number of matching segments Example: 12456.
        estimated_total_hits_relation (PaginationInfoEstimatedTotalHitsRelation | Unset): Whether estimatedTotalHits is
            exact or a lower bound Example: LOWER_BOUND.
    """

    page_size: int | Unset = UNSET
    has_more: bool | Unset = UNSET
    estimated_total_hits: int | Unset = UNSET
    estimated_total_hits_relation: PaginationInfoEstimatedTotalHitsRelation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_size = self.page_size

        has_more = self.has_more

        estimated_total_hits = self.estimated_total_hits

        estimated_total_hits_relation: str | Unset = UNSET
        if not isinstance(self.estimated_total_hits_relation, Unset):
            estimated_total_hits_relation = self.estimated_total_hits_relation.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if has_more is not UNSET:
            field_dict["hasMore"] = has_more
        if estimated_total_hits is not UNSET:
            field_dict["estimatedTotalHits"] = estimated_total_hits
        if estimated_total_hits_relation is not UNSET:
            field_dict["estimatedTotalHitsRelation"] = estimated_total_hits_relation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page_size = d.pop("pageSize", UNSET)

        has_more = d.pop("hasMore", UNSET)

        estimated_total_hits = d.pop("estimatedTotalHits", UNSET)

        _estimated_total_hits_relation = d.pop("estimatedTotalHitsRelation", UNSET)
        estimated_total_hits_relation: PaginationInfoEstimatedTotalHitsRelation | Unset
        if isinstance(_estimated_total_hits_relation, Unset):
            estimated_total_hits_relation = UNSET
        else:
            estimated_total_hits_relation = PaginationInfoEstimatedTotalHitsRelation(
                _estimated_total_hits_relation
            )

        pagination_info = cls(
            page_size=page_size,
            has_more=has_more,
            estimated_total_hits=estimated_total_hits,
            estimated_total_hits_relation=estimated_total_hits_relation,
        )

        pagination_info.additional_properties = d
        return pagination_info

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
