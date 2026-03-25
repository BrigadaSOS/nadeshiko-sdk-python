from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WordMatchMedia")


@_attrs_define
class WordMatchMedia:
    """Media match count entry

    Attributes:
        media_id (int): Media identifier (look up full details in includes.media) Example: 110316.
        match_count (int): Number of times the word appears in this media Example: 234.
    """

    media_id: int
    match_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media_id = self.media_id

        match_count = self.match_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mediaId": media_id,
                "matchCount": match_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        media_id = _src.pop("mediaId")

        match_count = _src.pop("matchCount")

        word_match_media = cls(
            media_id=media_id,
            match_count=match_count,
        )

        word_match_media.additional_properties = _src
        return word_match_media

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
