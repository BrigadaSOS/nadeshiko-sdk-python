from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.collection_type import CollectionType, check_collection_type
from ..models.collection_visibility import CollectionVisibility, check_collection_visibility

T = TypeVar("T", bound="Collection")


@_attrs_define
class Collection:
    """User segment collection

    Attributes:
        public_id (str): Public ID for the collection Example: V1StGXR8_Z5d.
        name (str): Name of the collection Example: Study Favorites.
        type_ (CollectionType): Type of the collection Example: USER.
        visibility (CollectionVisibility): Visibility of a collection Example: PRIVATE.
        segment_count (int): Number of segments in the collection Example: 42.
        created_at (datetime.datetime): When the collection was created
        updated_at (datetime.datetime | None): When the collection was last updated
    """

    public_id: str
    name: str
    type_: CollectionType
    visibility: CollectionVisibility
    segment_count: int
    created_at: datetime.datetime
    updated_at: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_id = self.public_id

        name = self.name

        type_: str = self.type_

        visibility: str = self.visibility

        segment_count = self.segment_count

        created_at = self.created_at.isoformat()

        updated_at: None | str
        if isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "publicId": public_id,
                "name": name,
                "type": type_,
                "visibility": visibility,
                "segmentCount": segment_count,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        public_id = _src.pop("publicId")

        name = _src.pop("name")

        type_ = check_collection_type(_src.pop("type"))

        visibility = check_collection_visibility(_src.pop("visibility"))

        segment_count = _src.pop("segmentCount")

        created_at = datetime.datetime.fromisoformat(_src.pop("createdAt"))

        def _parse_updated_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        updated_at = _parse_updated_at(_src.pop("updatedAt"))

        collection = cls(
            public_id=public_id,
            name=name,
            type_=type_,
            visibility=visibility,
            segment_count=segment_count,
            created_at=created_at,
            updated_at=updated_at,
        )

        collection.additional_properties = _src
        return collection

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
