from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.search_multiple_response_includes import SearchMultipleResponseIncludes
    from ..models.word_match import WordMatch


T = TypeVar("T", bound="SearchMultipleResponse")


@_attrs_define
class SearchMultipleResponse:
    """
    Attributes:
        results (list[WordMatch]):
        includes (SearchMultipleResponseIncludes):
    """

    results: list[WordMatch]
    includes: SearchMultipleResponseIncludes
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        includes = self.includes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "includes": includes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_multiple_response_includes import SearchMultipleResponseIncludes
        from ..models.word_match import WordMatch

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = WordMatch.from_dict(results_item_data)

            results.append(results_item)

        includes = SearchMultipleResponseIncludes.from_dict(d.pop("includes"))

        search_multiple_response = cls(
            results=results,
            includes=includes,
        )

        search_multiple_response.additional_properties = d
        return search_multiple_response

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
