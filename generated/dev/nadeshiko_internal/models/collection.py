from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.collection_visibility import CollectionVisibility

T = TypeVar("T", bound="Collection")


@_attrs_define
class Collection:
    """User segment collection

    Attributes:
        id (int): Collection ID Example: 123.
        name (str): Name of the collection Example: Study Favorites.
        user_id (int): User ID who owns the collection Example: 1.
        visibility (CollectionVisibility): Visibility of the collection Example: PRIVATE.
    """

    id: int
    name: str
    user_id: int
    visibility: CollectionVisibility
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        user_id = self.user_id

        visibility = self.visibility.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "userId": user_id,
                "visibility": visibility,
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

        collection = cls(
            id=id,
            name=name,
            user_id=user_id,
            visibility=visibility,
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
