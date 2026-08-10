from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.admin_user_with_providers_role import (
    AdminUserWithProvidersRole,
    check_admin_user_with_providers_role,
)

T = TypeVar("T", bound="AdminUserWithProviders")


@_attrs_define
class AdminUserWithProviders:
    """
    Attributes:
        id (int): Internal user ID. Example: 42.
        name (str): The user's display name. Example: tanaka_san.
        email (str): The user's email address. Example: tanaka@example.com.
        role (AdminUserWithProvidersRole): The user's account tier or role. Example: USER.
        email_verified (bool): Whether the account's email address has been verified.
        banned (bool): Whether the account is currently banned.
        ban_reason (None | str): Reason recorded when the account was banned, if any.
        created_at (datetime.datetime): When the account was created. Example: 2024-03-15T10:00:00.000Z.
        updated_at (datetime.datetime): When the account was last modified. Example: 2024-03-15T10:00:00.000Z.
        providers (list[str]): Linked authentication providers (empty when the account has none).
    """

    id: int
    name: str
    email: str
    role: AdminUserWithProvidersRole
    email_verified: bool
    banned: bool
    ban_reason: None | str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    providers: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        email = self.email

        role: str = self.role

        email_verified = self.email_verified

        banned = self.banned

        ban_reason: None | str
        ban_reason = self.ban_reason

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        providers = self.providers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "email": email,
                "role": role,
                "emailVerified": email_verified,
                "banned": banned,
                "banReason": ban_reason,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "providers": providers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        id = _src.pop("id")

        name = _src.pop("name")

        email = _src.pop("email")

        role = check_admin_user_with_providers_role(_src.pop("role"))

        email_verified = _src.pop("emailVerified")

        banned = _src.pop("banned")

        def _parse_ban_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ban_reason = _parse_ban_reason(_src.pop("banReason"))

        created_at = datetime.datetime.fromisoformat(_src.pop("createdAt"))

        updated_at = datetime.datetime.fromisoformat(_src.pop("updatedAt"))

        providers = cast(list[str], _src.pop("providers"))

        admin_user_with_providers = cls(
            id=id,
            name=name,
            email=email,
            role=role,
            email_verified=email_verified,
            banned=banned,
            ban_reason=ban_reason,
            created_at=created_at,
            updated_at=updated_at,
            providers=providers,
        )

        admin_user_with_providers.additional_properties = _src
        return admin_user_with_providers

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
