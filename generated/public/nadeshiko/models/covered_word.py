from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CoveredWord")


@_attrs_define
class CoveredWord:
    """A word from the frequency list with coverage information

    Attributes:
        rank (int): Frequency rank Example: 32.
        word (str): The Japanese word Example: 彼女.
        match_count (int): Number of matching sentences in the corpus Example: 1542.
    """

    rank: int
    word: str
    match_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rank = self.rank

        word = self.word

        match_count = self.match_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rank": rank,
                "word": word,
                "matchCount": match_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        rank = _src.pop("rank")

        word = _src.pop("word")

        match_count = _src.pop("matchCount")

        covered_word = cls(
            rank=rank,
            word=word,
            match_count=match_count,
        )

        covered_word.additional_properties = _src
        return covered_word

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
