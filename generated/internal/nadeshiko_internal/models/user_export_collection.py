from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.collection_type import CollectionType
from ..models.collection_visibility import CollectionVisibility

T = TypeVar("T", bound="UserExportCollection")


@_attrs_define
class UserExportCollection:
    """
    Attributes:
        id (int): Collection ID Example: 123.
        public_id (str): Public identifier for the collection Example: V1StGXR8_Z5d.
        name (str): Name of the collection Example: Study Favorites.
        type_ (CollectionType): Type of the collection Example: USER.
        visibility (CollectionVisibility): Visibility of the collection Example: PRIVATE.
        segment_count (int): Number of segments in the collection Example: 42.
        created_at (datetime.datetime): When the collection was created
        updated_at (datetime.datetime | None): When the collection was last updated
        segment_ids (list[int]): Segment IDs in saved order
    """

    id: int
    public_id: str
    name: str
    type_: CollectionType
    visibility: CollectionVisibility
    segment_count: int
    created_at: datetime.datetime
    updated_at: datetime.datetime | None
    segment_ids: list[int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        public_id = self.public_id

        name = self.name

        type_ = self.type_.value

        visibility = self.visibility.value

        segment_count = self.segment_count

        created_at = self.created_at.isoformat()

        updated_at: None | str
        if isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        segment_ids = self.segment_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "publicId": public_id,
                "name": name,
                "type": type_,
                "visibility": visibility,
                "segmentCount": segment_count,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "segmentIds": segment_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        id = _src.pop("id")

        public_id = _src.pop("publicId")

        name = _src.pop("name")

        type_ = CollectionType(_src.pop("type"))

        visibility = CollectionVisibility(_src.pop("visibility"))

        segment_count = _src.pop("segmentCount")

        created_at = isoparse(_src.pop("createdAt"))

        def _parse_updated_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        updated_at = _parse_updated_at(_src.pop("updatedAt"))

        segment_ids = cast(list[int], _src.pop("segmentIds"))

        user_export_collection = cls(
            id=id,
            public_id=public_id,
            name=name,
            type_=type_,
            visibility=visibility,
            segment_count=segment_count,
            created_at=created_at,
            updated_at=updated_at,
            segment_ids=segment_ids,
        )

        user_export_collection.additional_properties = _src
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
