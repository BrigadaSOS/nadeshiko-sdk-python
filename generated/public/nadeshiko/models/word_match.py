from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.word_match_media import WordMatchMedia


T = TypeVar("T", bound="WordMatch")


@_attrs_define
class WordMatch:
    """Word matching result with occurrences across media

    Attributes:
        word (str): The word that was searched for Example: 彼女.
        is_match (bool): Indicates whether the word was found in any segment Example: True.
        match_count (int): Total number of times this word appears across all media Example: 1523.
        media (list[WordMatchMedia]): List of media containing this word
    """

    word: str
    is_match: bool
    match_count: int
    media: list[WordMatchMedia]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        word = self.word

        is_match = self.is_match

        match_count = self.match_count

        media = []
        for media_item_data in self.media:
            media_item = media_item_data.to_dict()
            media.append(media_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "word": word,
                "isMatch": is_match,
                "matchCount": match_count,
                "media": media,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.word_match_media import WordMatchMedia

        _src = dict(src_dict)
        word = _src.pop("word")

        is_match = _src.pop("isMatch")

        match_count = _src.pop("matchCount")

        media = []
        _media = _src.pop("media")
        for media_item_data in _media:
            media_item = WordMatchMedia.from_dict(media_item_data)

            media.append(media_item)

        word_match = cls(
            word=word,
            is_match=is_match,
            match_count=match_count,
            media=media,
        )

        word_match.additional_properties = _src
        return word_match

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
