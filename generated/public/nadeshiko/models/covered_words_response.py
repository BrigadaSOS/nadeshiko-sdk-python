from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.covered_word import CoveredWord
    from ..models.covered_words_response_tier_stats import CoveredWordsResponseTierStats
    from ..models.cursor_pagination import CursorPagination


T = TypeVar("T", bound="CoveredWordsResponse")


@_attrs_define
class CoveredWordsResponse:
    """Paginated list of frequency-list words with coverage information

    Attributes:
        words (list[CoveredWord]):
        pagination (CursorPagination): Opaque cursor pagination metadata
        tier_stats (CoveredWordsResponseTierStats): Tier-level word counts (cached)
    """

    words: list[CoveredWord]
    pagination: CursorPagination
    tier_stats: CoveredWordsResponseTierStats
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        words = []
        for words_item_data in self.words:
            words_item = words_item_data.to_dict()
            words.append(words_item)

        pagination = self.pagination.to_dict()

        tier_stats = self.tier_stats.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "words": words,
                "pagination": pagination,
                "tierStats": tier_stats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.covered_word import CoveredWord
        from ..models.covered_words_response_tier_stats import CoveredWordsResponseTierStats
        from ..models.cursor_pagination import CursorPagination

        _src = dict(src_dict)
        words = []
        _words = _src.pop("words")
        for words_item_data in _words:
            words_item = CoveredWord.from_dict(words_item_data)

            words.append(words_item)

        pagination = CursorPagination.from_dict(_src.pop("pagination"))

        tier_stats = CoveredWordsResponseTierStats.from_dict(_src.pop("tierStats"))

        covered_words_response = cls(
            words=words,
            pagination=pagination,
            tier_stats=tier_stats,
        )

        covered_words_response.additional_properties = _src
        return covered_words_response

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
