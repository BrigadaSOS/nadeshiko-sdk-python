from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SegmentTextEs")


@_attrs_define
class SegmentTextEs:
    """
    Attributes:
        content (str): Spanish translation Example: Yo soy yo, y tú eres tú..
        is_machine_translated (bool): Whether the translation was machine-translated
        highlight (str | Unset): Spanish content with search terms highlighted
    """

    content: str
    is_machine_translated: bool
    highlight: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        is_machine_translated = self.is_machine_translated

        highlight = self.highlight

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "isMachineTranslated": is_machine_translated,
            }
        )
        if highlight is not UNSET:
            field_dict["highlight"] = highlight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content")

        is_machine_translated = d.pop("isMachineTranslated")

        highlight = d.pop("highlight", UNSET)

        segment_text_es = cls(
            content=content,
            is_machine_translated=is_machine_translated,
            highlight=highlight,
        )

        segment_text_es.additional_properties = d
        return segment_text_es

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
