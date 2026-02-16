from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SegmentUpdateRequestEn")


@_attrs_define
class SegmentUpdateRequestEn:
    """
    Attributes:
        content (str | Unset): English translation of the segment content Example: I am me, and you are you..
        is_machine_translated (bool | Unset): Whether the English translation was machine-translated Default: False.
    """

    content: str | Unset = UNSET
    is_machine_translated: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        is_machine_translated = self.is_machine_translated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if is_machine_translated is not UNSET:
            field_dict["isMachineTranslated"] = is_machine_translated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content", UNSET)

        is_machine_translated = d.pop("isMachineTranslated", UNSET)

        segment_update_request_en = cls(
            content=content,
            is_machine_translated=is_machine_translated,
        )

        segment_update_request_en.additional_properties = d
        return segment_update_request_en

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
