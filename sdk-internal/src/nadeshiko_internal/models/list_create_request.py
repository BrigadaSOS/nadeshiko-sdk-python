from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_create_request_type import ListCreateRequestType
from ..models.list_create_request_visibility import ListCreateRequestVisibility
from ..types import UNSET, Unset






T = TypeVar("T", bound="ListCreateRequest")



@_attrs_define
class ListCreateRequest:
    """ Request body for creating a new standalone list

        Attributes:
            name (str): Name of the list Example: My Watchlist.
            type_ (ListCreateRequestType | Unset): Type of list Example: CUSTOM.
            user_id (int | Unset): User ID who owns the list (1 = admin) Example: 1.
            visibility (ListCreateRequestVisibility | Unset): Visibility of the list Example: PUBLIC.
     """

    name: str
    type_: ListCreateRequestType | Unset = UNSET
    user_id: int | Unset = UNSET
    visibility: ListCreateRequestVisibility | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        user_id = self.user_id

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        _type_ = d.pop("type", UNSET)
        type_: ListCreateRequestType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = ListCreateRequestType(_type_)




        user_id = d.pop("userId", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: ListCreateRequestVisibility | Unset
        if isinstance(_visibility,  Unset):
            visibility = UNSET
        else:
            visibility = ListCreateRequestVisibility(_visibility)




        list_create_request = cls(
            name=name,
            type_=type_,
            user_id=user_id,
            visibility=visibility,
        )


        list_create_request.additional_properties = d
        return list_create_request

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
