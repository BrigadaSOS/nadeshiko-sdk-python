from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.collection_visibility import CollectionVisibility

T = TypeVar("T", bound="UserExportCollection")


@_attrs_define
class UserExportCollection:
    """
    Attributes:
        id (int): Collection ID Example: 123.
        name (str): Name of the collection Example: Study Favorites.
        user_id (int): User ID who owns the collection Example: 1.
        visibility (CollectionVisibility): Visibility of the collection Example: PRIVATE.
        segment_uuids (list[UUID]): Segment UUIDs in saved order
    """

    id: int
    name: str
    user_id: int
    visibility: CollectionVisibility
    segment_uuids: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        user_id = self.user_id

        visibility = self.visibility.value

        segment_uuids = []
        for segment_uuids_item_data in self.segment_uuids:
            segment_uuids_item = str(segment_uuids_item_data)
            segment_uuids.append(segment_uuids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "userId": user_id,
                "visibility": visibility,
                "segmentUuids": segment_uuids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        user_id = d.pop("userId")

        visibility = CollectionVisibility(d.pop("visibility"))

        segment_uuids = []
        _segment_uuids = d.pop("segmentUuids")
        for segment_uuids_item_data in _segment_uuids:
            segment_uuids_item = UUID(segment_uuids_item_data)

            segment_uuids.append(segment_uuids_item)

        user_export_collection = cls(
            id=id,
            name=name,
            user_id=user_id,
            visibility=visibility,
            segment_uuids=segment_uuids,
        )

        user_export_collection.additional_properties = d
        return user_export_collection

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
