from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_key_scope import ApiKeyScope, check_api_key_scope

T = TypeVar("T", bound="CreateUserApiKeyResponse201")


@_attrs_define
class CreateUserApiKeyResponse201:
    """
    Attributes:
        id (str): Identifier for the key, for renaming or revoking it later
        name (str): The label supplied at creation
        key (str): The secret, returned **only here and never again**. It is
            stored hashed, so a reader who loses it must create another.
             Example: nade_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.
        scopes (list[ApiKeyScope]): The scopes actually granted
        created_at (datetime.datetime):
    """

    id: str
    name: str
    key: str
    scopes: list[ApiKeyScope]
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        key = self.key

        scopes = []
        for scopes_item_data in self.scopes:
            scopes_item: str = scopes_item_data
            scopes.append(scopes_item)

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "key": key,
                "scopes": scopes,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        id = _src.pop("id")

        name = _src.pop("name")

        key = _src.pop("key")

        scopes = []
        _scopes = _src.pop("scopes")
        for scopes_item_data in _scopes:
            scopes_item = check_api_key_scope(scopes_item_data)

            scopes.append(scopes_item)

        created_at = datetime.datetime.fromisoformat(_src.pop("createdAt"))

        create_user_api_key_response_201 = cls(
            id=id,
            name=name,
            key=key,
            scopes=scopes,
            created_at=created_at,
        )

        create_user_api_key_response_201.additional_properties = _src
        return create_user_api_key_response_201

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
