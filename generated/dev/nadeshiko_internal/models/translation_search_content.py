from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TranslationSearchContent")


@_attrs_define
class TranslationSearchContent:
    """Translation content in search results with optional highlight

    Attributes:
        is_machine_translated (bool): Whether the translation was machine-translated
        content (str | Unset): Translated content Example: I am me, and you are you..
        highlight (str | Unset): Translated content with search terms highlighted Example: <em>I</em> am <em>me</em>,
            and <em>you</em> are <em>you</em>..
    """

    is_machine_translated: bool
    content: str | Unset = UNSET
    highlight: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_machine_translated = self.is_machine_translated

        content = self.content

        highlight = self.highlight

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isMachineTranslated": is_machine_translated,
            }
        )
        if content is not UNSET:
            field_dict["content"] = content
        if highlight is not UNSET:
            field_dict["highlight"] = highlight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_machine_translated = d.pop("isMachineTranslated")

        content = d.pop("content", UNSET)

        highlight = d.pop("highlight", UNSET)

        translation_search_content = cls(
            is_machine_translated=is_machine_translated,
            content=content,
            highlight=highlight,
        )

        translation_search_content.additional_properties = d
        return translation_search_content

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
