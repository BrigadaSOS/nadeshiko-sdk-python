from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchQuery")


@_attrs_define
class SearchQuery:
    """What to search for (omit for queryless browse/stats)

    Attributes:
        search (str | Unset): Search expression (supports boolean operators, wildcards, phrase matching) Example: (猫 OR
            犬) AND 好き.
        exact_match (bool | Unset): Require exact phrase matching (disables fuzzy and partial matches) Default: False.
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
        _src = dict(src_dict)
        search = _src.pop("search", UNSET)

        exact_match = _src.pop("exactMatch", UNSET)

        search_query = cls(
            search=search,
            exact_match=exact_match,
        )

        search_query.additional_properties = _src
        return search_query

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
