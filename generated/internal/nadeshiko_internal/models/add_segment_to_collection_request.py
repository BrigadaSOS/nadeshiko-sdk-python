from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddSegmentToCollectionRequest")


@_attrs_define
class AddSegmentToCollectionRequest:
    """
    Attributes:
        segment_public_id (str): Segment public ID Example: V1StGXR8_Z5d.
        note (str | Unset): Optional annotation
    """

    segment_public_id: str
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        segment_public_id = self.segment_public_id

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "segmentPublicId": segment_public_id,
            }
        )
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        segment_public_id = _src.pop("segmentPublicId")

        note = _src.pop("note", UNSET)

        add_segment_to_collection_request = cls(
            segment_public_id=segment_public_id,
            note=note,
        )

        add_segment_to_collection_request.additional_properties = _src
        return add_segment_to_collection_request

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
