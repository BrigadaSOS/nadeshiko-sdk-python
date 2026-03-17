from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.segment import Segment


T = TypeVar("T", bound="CollectionWithSegmentsSegmentsItem")


@_attrs_define
class CollectionWithSegmentsSegmentsItem:
    """
    Attributes:
        position (int): Position in the collection Example: 1.
        note (None | str): User annotation
        result (Segment): Segment with content, optional highlights, and media URLs
    """

    position: int
    note: None | str
    result: Segment
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        position = self.position

        note: None | str
        note = self.note

        result = self.result.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position": position,
                "note": note,
                "result": result,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.segment import Segment

        d = dict(src_dict)
        position = d.pop("position")

        def _parse_note(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        note = _parse_note(d.pop("note"))

        result = Segment.from_dict(d.pop("result"))

        collection_with_segments_segments_item = cls(
            position=position,
            note=note,
            result=result,
        )

        collection_with_segments_segments_item.additional_properties = d
        return collection_with_segments_segments_item

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
