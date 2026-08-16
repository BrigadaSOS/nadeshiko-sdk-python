from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_key_scope import ApiKeyScope, check_api_key_scope

T = TypeVar("T", bound="CreateUserApiKeyBody")


@_attrs_define
class CreateUserApiKeyBody:
    """
    Attributes:
        name (str): Label shown in the reader's key list. Not secret. Example: Entei (read-only).
        scopes (list[ApiKeyScope]): Capabilities to grant. Must be non-empty and free of duplicates.
             Example: ['READ_MEDIA'].
    """

    name: str
    scopes: list[ApiKeyScope]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        scopes = []
        for scopes_item_data in self.scopes:
            scopes_item: str = scopes_item_data
            scopes.append(scopes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "scopes": scopes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        name = _src.pop("name")

        scopes = []
        _scopes = _src.pop("scopes")
        for scopes_item_data in _scopes:
            scopes_item = check_api_key_scope(scopes_item_data)

            scopes.append(scopes_item)

        create_user_api_key_body = cls(
            name=name,
            scopes=scopes,
        )

        create_user_api_key_body.additional_properties = _src
        return create_user_api_key_body

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
