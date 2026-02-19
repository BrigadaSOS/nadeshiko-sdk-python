from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserLabFeature")


@_attrs_define
class UserLabFeature:
    """
    Attributes:
        key (str): Unique identifier for the lab feature
        name (str): Human-readable feature name
        description (str): Description of what the feature does
        enabled (bool): Whether the feature is globally available
        user_enabled (bool): Whether the user has opted in to this feature
    """

    key: str
    name: str
    description: str
    enabled: bool
    user_enabled: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        name = self.name

        description = self.description

        enabled = self.enabled

        user_enabled = self.user_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "name": name,
                "description": description,
                "enabled": enabled,
                "userEnabled": user_enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        name = d.pop("name")

        description = d.pop("description")

        enabled = d.pop("enabled")

        user_enabled = d.pop("userEnabled")

        user_lab_feature = cls(
            key=key,
            name=name,
            description=description,
            enabled=enabled,
            user_enabled=user_enabled,
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
