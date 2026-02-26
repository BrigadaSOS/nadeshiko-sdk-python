from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserLabFeature")


@_attrs_define
class UserLabFeature:
    """
    Attributes:
        key (str): Unique identifier for the feature
        active (bool): Whether this feature is currently active for the user
        user_controllable (bool): Whether the user can toggle this feature (lab=true, flag=false)
        name (str | Unset): Human-readable feature name (only present for labs)
        description (str | Unset): Description of what the feature does (only present for labs)
    """

    key: str
    active: bool
    user_controllable: bool
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        active = self.active

        user_controllable = self.user_controllable

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "active": active,
                "userControllable": user_controllable,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        active = d.pop("active")

        user_controllable = d.pop("userControllable")

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        user_lab_feature = cls(
            key=key,
            active=active,
            user_controllable=user_controllable,
            name=name,
            description=description,
        )

        user_lab_feature.additional_properties = d
        return user_lab_feature

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
