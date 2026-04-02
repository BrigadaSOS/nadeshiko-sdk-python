from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.covered_word import CoveredWord
    from ..models.get_covered_words_response_200_tier_stats import (
        GetCoveredWordsResponse200TierStats,
    )


T = TypeVar("T", bound="GetCoveredWordsResponse200")


@_attrs_define
class GetCoveredWordsResponse200:
    """
    Attributes:
        words (list[CoveredWord]):
        next_cursor (int | None): Rank cursor for the next page, or null if this is the last page
        tier_stats (GetCoveredWordsResponse200TierStats): Tier-level word counts (cached)
    """

    words: list[CoveredWord]
    next_cursor: int | None
    tier_stats: GetCoveredWordsResponse200TierStats
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        words = []
        for words_item_data in self.words:
            words_item = words_item_data.to_dict()
            words.append(words_item)

        next_cursor: int | None
        next_cursor = self.next_cursor

        tier_stats = self.tier_stats.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "words": words,
                "nextCursor": next_cursor,
                "tierStats": tier_stats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.covered_word import CoveredWord
        from ..models.get_covered_words_response_200_tier_stats import (
            GetCoveredWordsResponse200TierStats,
        )

        _src = dict(src_dict)
        words = []
        _words = _src.pop("words")
        for words_item_data in _words:
            words_item = CoveredWord.from_dict(words_item_data)

            words.append(words_item)

        def _parse_next_cursor(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        next_cursor = _parse_next_cursor(_src.pop("nextCursor"))

        tier_stats = GetCoveredWordsResponse200TierStats.from_dict(_src.pop("tierStats"))

        get_covered_words_response_200 = cls(
            words=words,
            next_cursor=next_cursor,
            tier_stats=tier_stats,
        )

        get_covered_words_response_200.additional_properties = _src
        return get_covered_words_response_200

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
