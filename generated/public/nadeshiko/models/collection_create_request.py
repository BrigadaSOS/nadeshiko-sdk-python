from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.collection_visibility import CollectionVisibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectionCreateRequest")


@_attrs_define
class CollectionCreateRequest:
    """Request body for creating a new collection

    Attributes:
        name (str): Name of the collection Example: My Study List.
        visibility (CollectionVisibility | Unset): Visibility of a collection Example: PRIVATE.
    """

    name: str
    visibility: CollectionVisibility | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        name = _src.pop("name")

        _visibility = _src.pop("visibility", UNSET)
        visibility: CollectionVisibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = CollectionVisibility(_visibility)

        collection_create_request = cls(
            name=name,
            visibility=visibility,
        )

        collection_create_request.additional_properties = _src
        return collection_create_request

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
