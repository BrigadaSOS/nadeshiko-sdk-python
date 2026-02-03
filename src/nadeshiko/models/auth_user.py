from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_role import UserRole


T = TypeVar("T", bound="AuthUser")


@_attrs_define
class AuthUser:
    """Authenticated user information

    Attributes:
        id (int | Unset): User ID
        username (str | Unset): User's display name
        email (str | Unset): User's email address
        roles (list[UserRole] | Unset): User's roles
    """

    id: int | Unset = UNSET
    username: str | Unset = UNSET
    email: str | Unset = UNSET
    roles: list[UserRole] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        username = self.username

        email = self.email

        roles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.to_dict()
                roles.append(roles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if username is not UNSET:
            field_dict["username"] = username
        if email is not UNSET:
            field_dict["email"] = email
        if roles is not UNSET:
            field_dict["roles"] = roles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_role import UserRole

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        username = d.pop("username", UNSET)

        email = d.pop("email", UNSET)

        _roles = d.pop("roles", UNSET)
        roles: list[UserRole] | Unset = UNSET
        if _roles is not UNSET:
            roles = []
            for roles_item_data in _roles:
                roles_item = UserRole.from_dict(roles_item_data)

                roles.append(roles_item)

        auth_user = cls(
            id=id,
            username=username,
            email=email,
            roles=roles,
        )

        auth_user.additional_properties = d
        return auth_user

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
