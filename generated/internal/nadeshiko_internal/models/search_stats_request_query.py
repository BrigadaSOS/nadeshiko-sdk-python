from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchStatsRequestQuery")


@_attrs_define
class SearchStatsRequestQuery:
    """What to search for (omit for queryless stats)

    Attributes:
        search (str | Unset): Search expression (supports boolean operators, wildcards, phrase matching) Example: 彼女.
        exact_match (bool | Unset): Whether to use exact phrase matching Default: False.
    """

    search: str | Unset = UNSET
    exact_match: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        search = self.search

        exact_match = self.exact_match

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if search is not UNSET:
            field_dict["search"] = search
        if exact_match is not UNSET:
            field_dict["exactMatch"] = exact_match

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        search = d.pop("search", UNSET)

        exact_match = d.pop("exactMatch", UNSET)

        search_stats_request_query = cls(
            search=search,
            exact_match=exact_match,
        )

        search_stats_request_query.additional_properties = d
        return search_stats_request_query

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
