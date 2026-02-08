from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_type import ListType
from ..models.list_visibility import ListVisibility






T = TypeVar("T", bound="List")



@_attrs_define
class List:
    """ Media collection list

        Attributes:
            id (int): List ID Example: 123.
            name (str): Name of the list Example: Bakuman Series.
            type_ (ListType): Type of list Example: SERIES.
            user_id (int): User ID who owns the list (1 = admin) Example: 1.
            visibility (ListVisibility): Visibility of the list Example: PUBLIC.
     """

    id: int
    name: str
    type_: ListType
    user_id: int
    visibility: ListVisibility
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_ = self.type_.value

        user_id = self.user_id

        visibility = self.visibility.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "type": type_,
            "userId": user_id,
            "visibility": visibility,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        type_ = ListType(d.pop("type"))




        user_id = d.pop("userId")

        visibility = ListVisibility(d.pop("visibility"))




        list_ = cls(
            id=id,
            name=name,
            type_=type_,
            user_id=user_id,
            visibility=visibility,
        )


        list_.additional_properties = d
        return list_

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
