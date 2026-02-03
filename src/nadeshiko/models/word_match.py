from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.word_match_media import WordMatchMedia


T = TypeVar("T", bound="WordMatch")


@_attrs_define
class WordMatch:
    """Word matching result with occurrences across media

    Attributes:
        word (str | Unset): The word that was searched for Example: 彼女.
        is_match (bool | Unset): Indicates whether the word was found in any segment Example: True.
        total_matches (int | Unset): Total number of times this word appears across all media Example: 1523.
        media (list[WordMatchMedia] | Unset): List of media containing this word
    """

    word: str | Unset = UNSET
    is_match: bool | Unset = UNSET
    total_matches: int | Unset = UNSET
    media: list[WordMatchMedia] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        word = self.word

        is_match = self.is_match

        total_matches = self.total_matches

        media: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.media, Unset):
            media = []
            for media_item_data in self.media:
                media_item = media_item_data.to_dict()
                media.append(media_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if word is not UNSET:
            field_dict["word"] = word
        if is_match is not UNSET:
            field_dict["is_match"] = is_match
        if total_matches is not UNSET:
            field_dict["total_matches"] = total_matches
        if media is not UNSET:
            field_dict["media"] = media

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.word_match_media import WordMatchMedia

        d = dict(src_dict)
        word = d.pop("word", UNSET)

        is_match = d.pop("is_match", UNSET)

        total_matches = d.pop("total_matches", UNSET)

        _media = d.pop("media", UNSET)
        media: list[WordMatchMedia] | Unset = UNSET
        if _media is not UNSET:
            media = []
            for media_item_data in _media:
                media_item = WordMatchMedia.from_dict(media_item_data)

                media.append(media_item)

        word_match = cls(
            word=word,
            is_match=is_match,
            total_matches=total_matches,
            media=media,
        )

        word_match.additional_properties = d
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
