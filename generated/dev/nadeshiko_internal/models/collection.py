from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.collection_visibility import CollectionVisibility

T = TypeVar("T", bound="Collection")


@_attrs_define
class Collection:
    """User segment collection

    Attributes:
        id (int): Collection ID Example: 123.
        name (str): Name of the collection Example: Study Favorites.
        visibility (CollectionVisibility): Visibility of the collection Example: PRIVATE.
        segment_count (int): Number of segments in the collection Example: 42.
        created_at (datetime.datetime): When the collection was created
        updated_at (datetime.datetime | None): When the collection was last updated
    """

    id: int
    name: str
    visibility: CollectionVisibility
    segment_count: int
    created_at: datetime.datetime
    updated_at: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        visibility = self.visibility.value

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
                "id": id,
                "name": name,
                "visibility": visibility,
                "segmentCount": segment_count,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        visibility = CollectionVisibility(d.pop("visibility"))

        segment_count = d.pop("segmentCount")

        created_at = isoparse(d.pop("createdAt"))

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

        updated_at = _parse_updated_at(d.pop("updatedAt"))

        collection = cls(
            id=id,
            name=name,
            visibility=visibility,
            segment_count=segment_count,
            created_at=created_at,
            updated_at=updated_at,
        )

        collection.additional_properties = d
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
