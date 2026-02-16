from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JapaneseSearchContent")


@_attrs_define
class JapaneseSearchContent:
    """Japanese content in search results with optional highlight

    Attributes:
        content (str): Original Japanese content of the segment Example: 僕は僕で、君は君だ。.
        highlight (str | Unset): Japanese content with search terms highlighted Example:
            <em>僕</em>は<em>僕</em>で、<em>君</em>は<em>君</em>だ。.
    """

    content: str
    highlight: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        highlight = self.highlight

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
            }
        )
        if highlight is not UNSET:
            field_dict["highlight"] = highlight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content")

        highlight = d.pop("highlight", UNSET)

        japanese_search_content = cls(
            content=content,
            highlight=highlight,
        )

        japanese_search_content.additional_properties = d
        return japanese_search_content

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
