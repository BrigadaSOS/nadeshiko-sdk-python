from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_filters_languages_exclude_item import SearchFiltersLanguagesExcludeItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchFiltersLanguages")


@_attrs_define
class SearchFiltersLanguages:
    """Language inclusion/exclusion for search matching

    Attributes:
        exclude (list[SearchFiltersLanguagesExcludeItem] | Unset): Language codes to exclude from search matching (e.g.,
            ["en"], ["es"], ["en","es"])
    """

    exclude: list[SearchFiltersLanguagesExcludeItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exclude: list[str] | Unset = UNSET
        if not isinstance(self.exclude, Unset):
            exclude = []
            for exclude_item_data in self.exclude:
                exclude_item = exclude_item_data.value
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
        exclude: list[SearchFiltersLanguagesExcludeItem] | Unset = UNSET
        if _exclude is not UNSET:
            exclude = []
            for exclude_item_data in _exclude:
                exclude_item = SearchFiltersLanguagesExcludeItem(exclude_item_data)

                exclude.append(exclude_item)

        search_filters_languages = cls(
            exclude=exclude,
        )

        search_filters_languages.additional_properties = _src
        return search_filters_languages

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
