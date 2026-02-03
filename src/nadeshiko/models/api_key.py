from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.api_key_permission import ApiKeyPermission


T = TypeVar("T", bound="ApiKey")


@_attrs_define
class ApiKey:
    """API key information

    Attributes:
        id (int): API key ID
        name (str): API key name
        is_active (bool): Whether the API key is active
        created_at (datetime.datetime): Creation timestamp
        hint (str): API key hint (last 4 characters)
        permissions (list[ApiKeyPermission]): API key permissions
    """

    id: int
    name: str
    is_active: bool
    created_at: datetime.datetime
    hint: str
    permissions: list[ApiKeyPermission]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        is_active = self.is_active

        created_at = self.created_at.isoformat()

        hint = self.hint

        permissions = []
        for permissions_item_data in self.permissions:
            permissions_item = permissions_item_data.to_dict()
            permissions.append(permissions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "isActive": is_active,
                "createdAt": created_at,
                "hint": hint,
                "permissions": permissions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_key_permission import ApiKeyPermission

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        is_active = d.pop("isActive")

        created_at = isoparse(d.pop("createdAt"))

        hint = d.pop("hint")

        permissions = []
        _permissions = d.pop("permissions")
        for permissions_item_data in _permissions:
            permissions_item = ApiKeyPermission.from_dict(permissions_item_data)

            permissions.append(permissions_item)

        api_key = cls(
            id=id,
            name=name,
            is_active=is_active,
            created_at=created_at,
            hint=hint,
            permissions=permissions,
        )

        api_key.additional_properties = d
        return api_key

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
