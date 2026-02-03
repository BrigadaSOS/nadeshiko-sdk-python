from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_role import UserRole


T = TypeVar("T", bound="UserInfoResponseUser")


@_attrs_define
class UserInfoResponseUser:
    """
    Attributes:
        username (str): User's display name
        email (str): User's email address
        roles (list[UserRole]): User's roles
    """

    username: str
    email: str
    roles: list[UserRole]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        email = self.email

        roles = []
        for roles_item_data in self.roles:
            roles_item = roles_item_data.to_dict()
            roles.append(roles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "email": email,
                "roles": roles,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_role import UserRole

        d = dict(src_dict)
        username = d.pop("username")

        email = d.pop("email")

        roles = []
        _roles = d.pop("roles")
        for roles_item_data in _roles:
            roles_item = UserRole.from_dict(roles_item_data)

            roles.append(roles_item)

        user_info_response_user = cls(
            username=username,
            email=email,
            roles=roles,
        )

        user_info_response_user.additional_properties = d
        return user_info_response_user

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
