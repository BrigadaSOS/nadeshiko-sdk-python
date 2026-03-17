from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_collection_body_visibility import UpdateCollectionBodyVisibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCollectionBody")


@_attrs_define
class UpdateCollectionBody:
    """
    Attributes:
        name (str | Unset):  Example: Updated Collection Name.
        visibility (UpdateCollectionBodyVisibility | Unset):  Example: PUBLIC.
    """

    name: str | Unset = UNSET
    visibility: UpdateCollectionBodyVisibility | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: UpdateCollectionBodyVisibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = UpdateCollectionBodyVisibility(_visibility)

        update_collection_body = cls(
            name=name,
            visibility=visibility,
        )

        update_collection_body.additional_properties = d
        return update_collection_body

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
