from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_request_sort_mode import SearchRequestSortMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchRequestSort")


@_attrs_define
class SearchRequestSort:
    """Sort configuration

    Attributes:
        mode (SearchRequestSortMode | Unset): Sort mode Default: SearchRequestSortMode.NONE.
        seed (int | Unset): Non-negative integer seed for deterministic random sorting (only used when mode is RANDOM)
            Example: 42.
    """

    mode: SearchRequestSortMode | Unset = SearchRequestSortMode.NONE
    seed: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        seed = self.seed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode
        if seed is not UNSET:
            field_dict["seed"] = seed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        _mode = _src.pop("mode", UNSET)
        mode: SearchRequestSortMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = SearchRequestSortMode(_mode)

        seed = _src.pop("seed", UNSET)

        search_request_sort = cls(
            mode=mode,
            seed=seed,
        )

        search_request_sort.additional_properties = _src
        return search_request_sort

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
