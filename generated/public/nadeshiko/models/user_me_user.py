from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserMeUser")


@_attrs_define
class UserMeUser:
    """
    Attributes:
        username (str): The user's display name. Example: tanaka_san.
        created_at (datetime.datetime): When the account was created. Example: 2024-03-15T10:00:00.000Z.
        role (str): The user's account tier or role. Example: USER.
    """

    username: str
    created_at: datetime.datetime
    role: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        created_at = self.created_at.isoformat()

        role = self.role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "createdAt": created_at,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        username = _src.pop("username")

        created_at = datetime.datetime.fromisoformat(_src.pop("createdAt"))

        role = _src.pop("role")

        user_me_user = cls(
            username=username,
            created_at=created_at,
            role=role,
        )

        user_me_user.additional_properties = _src
        return user_me_user

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
