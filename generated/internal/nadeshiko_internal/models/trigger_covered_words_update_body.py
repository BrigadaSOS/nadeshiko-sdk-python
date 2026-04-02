from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TriggerCoveredWordsUpdateBody")


@_attrs_define
class TriggerCoveredWordsUpdateBody:
    """
    Attributes:
        max_rank (int | Unset): Maximum frequency rank to check (defaults to all words) Default: 999999.
        only_uncovered (bool | Unset): Only check words that currently have zero matches (faster for incremental
            updates) Default: False.
    """

    max_rank: int | Unset = 999999
    only_uncovered: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_rank = self.max_rank

        only_uncovered = self.only_uncovered

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_rank is not UNSET:
            field_dict["maxRank"] = max_rank
        if only_uncovered is not UNSET:
            field_dict["onlyUncovered"] = only_uncovered

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        max_rank = _src.pop("maxRank", UNSET)

        only_uncovered = _src.pop("onlyUncovered", UNSET)

        trigger_covered_words_update_body = cls(
            max_rank=max_rank,
            only_uncovered=only_uncovered,
        )

        trigger_covered_words_update_body.additional_properties = _src
        return trigger_covered_words_update_body

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
