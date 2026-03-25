from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.segment_revision import SegmentRevision


T = TypeVar("T", bound="ListSegmentRevisionsResponse200")


@_attrs_define
class ListSegmentRevisionsResponse200:
    """
    Attributes:
        revisions (list[SegmentRevision]):
    """

    revisions: list[SegmentRevision]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        revisions = []
        for revisions_item_data in self.revisions:
            revisions_item = revisions_item_data.to_dict()
            revisions.append(revisions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "revisions": revisions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.segment_revision import SegmentRevision

        _src = dict(src_dict)
        revisions = []
        _revisions = _src.pop("revisions")
        for revisions_item_data in _revisions:
            revisions_item = SegmentRevision.from_dict(revisions_item_data)

            revisions.append(revisions_item)

        list_segment_revisions_response_200 = cls(
            revisions=revisions,
        )

        list_segment_revisions_response_200.additional_properties = _src
        return list_segment_revisions_response_200

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
