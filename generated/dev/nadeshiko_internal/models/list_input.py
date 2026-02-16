from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_input_list_type import ListInputListType
from ..models.list_input_list_visibility import ListInputListVisibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListInput")


@_attrs_define
class ListInput:
    """List data for adding media to a list

    Attributes:
        position (int): Position/order of media in the list (1-indexed) Example: 1.
        list_id (int | None | Unset): Existing list ID (if adding to existing list) Example: 123.
        list_name (None | str | Unset): Name for new list (if creating new list) Example: Bakuman Series.
        list_type (ListInputListType | Unset): Type of list (if creating new list) Example: SERIES.
        list_visibility (ListInputListVisibility | Unset): Visibility of list (if creating new list) Example: PUBLIC.
    """

    position: int
    list_id: int | None | Unset = UNSET
    list_name: None | str | Unset = UNSET
    list_type: ListInputListType | Unset = UNSET
    list_visibility: ListInputListVisibility | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        position = self.position

        list_id: int | None | Unset
        if isinstance(self.list_id, Unset):
            list_id = UNSET
        else:
            list_id = self.list_id

        list_name: None | str | Unset
        if isinstance(self.list_name, Unset):
            list_name = UNSET
        else:
            list_name = self.list_name

        list_type: str | Unset = UNSET
        if not isinstance(self.list_type, Unset):
            list_type = self.list_type.value

        list_visibility: str | Unset = UNSET
        if not isinstance(self.list_visibility, Unset):
            list_visibility = self.list_visibility.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position": position,
            }
        )
        if list_id is not UNSET:
            field_dict["listId"] = list_id
        if list_name is not UNSET:
            field_dict["listName"] = list_name
        if list_type is not UNSET:
            field_dict["listType"] = list_type
        if list_visibility is not UNSET:
            field_dict["listVisibility"] = list_visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        position = d.pop("position")

        def _parse_list_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        list_id = _parse_list_id(d.pop("listId", UNSET))

        def _parse_list_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        list_name = _parse_list_name(d.pop("listName", UNSET))

        _list_type = d.pop("listType", UNSET)
        list_type: ListInputListType | Unset
        if isinstance(_list_type, Unset):
            list_type = UNSET
        else:
            list_type = ListInputListType(_list_type)

        _list_visibility = d.pop("listVisibility", UNSET)
        list_visibility: ListInputListVisibility | Unset
        if isinstance(_list_visibility, Unset):
            list_visibility = UNSET
        else:
            list_visibility = ListInputListVisibility(_list_visibility)

        list_input = cls(
            position=position,
            list_id=list_id,
            list_name=list_name,
            list_type=list_type,
            list_visibility=list_visibility,
        )

        list_input.additional_properties = d
        return list_input

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
