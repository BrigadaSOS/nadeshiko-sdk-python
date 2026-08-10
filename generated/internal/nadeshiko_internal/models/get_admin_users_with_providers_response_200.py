from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.admin_user_with_providers import AdminUserWithProviders


T = TypeVar("T", bound="GetAdminUsersWithProvidersResponse200")


@_attrs_define
class GetAdminUsersWithProvidersResponse200:
    """
    Attributes:
        users (list[AdminUserWithProviders]):
        total (int): Total number of active accounts matching the search
    """

    users: list[AdminUserWithProviders]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()
            users.append(users_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "users": users,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admin_user_with_providers import AdminUserWithProviders

        _src = dict(src_dict)
        users = []
        _users = _src.pop("users")
        for users_item_data in _users:
            users_item = AdminUserWithProviders.from_dict(users_item_data)

            users.append(users_item)

        total = _src.pop("total")

        get_admin_users_with_providers_response_200 = cls(
            users=users,
            total=total,
        )

        get_admin_users_with_providers_response_200.additional_properties = _src
        return get_admin_users_with_providers_response_200

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
