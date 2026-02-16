from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JapaneseContent")


@_attrs_define
class JapaneseContent:
    """Japanese content with optional character count

    Attributes:
        content (str): Original Japanese content Example: 僕は僕で、君は君だ。.
        character_count (int | Unset): Number of characters in the Japanese content Example: 10.
    """

    content: str
    character_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        character_count = self.character_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
            }
        )
        if character_count is not UNSET:
            field_dict["characterCount"] = character_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content")

        character_count = d.pop("characterCount", UNSET)

        japanese_content = cls(
            content=content,
            character_count=character_count,
        )

        japanese_content.additional_properties = d
        return japanese_content

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
