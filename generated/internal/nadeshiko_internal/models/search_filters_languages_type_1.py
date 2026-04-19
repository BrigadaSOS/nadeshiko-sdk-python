from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_filters_languages_type_1_exclude_item import (
    SearchFiltersLanguagesType1ExcludeItem,
    check_search_filters_languages_type_1_exclude_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchFiltersLanguagesType1")


@_attrs_define
class SearchFiltersLanguagesType1:
    """Legacy exclude-based filter. Prefer the array form.

    Attributes:
        exclude (list[SearchFiltersLanguagesType1ExcludeItem] | Unset):
    """

    exclude: list[SearchFiltersLanguagesType1ExcludeItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exclude: list[str] | Unset = UNSET
        if not isinstance(self.exclude, Unset):
            exclude = []
            for exclude_item_data in self.exclude:
                exclude_item: str = exclude_item_data
                exclude.append(exclude_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exclude is not UNSET:
            field_dict["exclude"] = exclude

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        _exclude = _src.pop("exclude", UNSET)
        exclude: list[SearchFiltersLanguagesType1ExcludeItem] | Unset = UNSET
        if _exclude is not UNSET:
            exclude = []
            for exclude_item_data in _exclude:
                exclude_item = check_search_filters_languages_type_1_exclude_item(exclude_item_data)

                exclude.append(exclude_item)

        search_filters_languages_type_1 = cls(
            exclude=exclude,
        )

        search_filters_languages_type_1.additional_properties = _src
        return search_filters_languages_type_1

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
