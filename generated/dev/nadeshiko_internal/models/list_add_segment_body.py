from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListAddSegmentBody")


@_attrs_define
class ListAddSegmentBody:
    """
    Attributes:
        segment_uuid (str): UUID of the segment to add Example: 3fd94cef-a3e1-31ae-bc8d-e743f03e9c7e.
        note (str | Unset): Optional annotation
    """

    segment_uuid: str
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        segment_uuid = self.segment_uuid

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "segmentUuid": segment_uuid,
            }
        )
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        segment_uuid = d.pop("segmentUuid")

        note = d.pop("note", UNSET)

        list_add_segment_body = cls(
            segment_uuid=segment_uuid,
            note=note,
        )

        list_add_segment_body.additional_properties = d
        return list_add_segment_body

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
