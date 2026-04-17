from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SegmentTextEn")


@_attrs_define
class SegmentTextEn:
    """
    Attributes:
        content (str): English translation Example: I am me, and you are you..
        is_machine_translated (bool): Whether the translation was machine-translated
        highlight (None | str): English `content` with `<mark>` tags wrapping terms that matched a search query. Only
            populated on segments returned from a search endpoint that matched this language.
    """

    content: str
    is_machine_translated: bool
    highlight: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        is_machine_translated = self.is_machine_translated

        highlight: None | str
        highlight = self.highlight

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "isMachineTranslated": is_machine_translated,
                "highlight": highlight,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        content = _src.pop("content")

        is_machine_translated = _src.pop("isMachineTranslated")

        def _parse_highlight(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        highlight = _parse_highlight(_src.pop("highlight"))

        segment_text_en = cls(
            content=content,
            is_machine_translated=is_machine_translated,
            highlight=highlight,
        )

        segment_text_en.additional_properties = _src
        return segment_text_en

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
