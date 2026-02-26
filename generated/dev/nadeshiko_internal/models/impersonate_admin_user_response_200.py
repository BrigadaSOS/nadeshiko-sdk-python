from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.impersonate_admin_user_response_200_user import (
        ImpersonateAdminUserResponse200User,
    )


T = TypeVar("T", bound="ImpersonateAdminUserResponse200")


@_attrs_define
class ImpersonateAdminUserResponse200:
    """
    Attributes:
        message (str):
        user (ImpersonateAdminUserResponse200User):
    """

    message: str
    user: ImpersonateAdminUserResponse200User
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.impersonate_admin_user_response_200_user import (
            ImpersonateAdminUserResponse200User,
        )

        d = dict(src_dict)
        message = d.pop("message")

        user = ImpersonateAdminUserResponse200User.from_dict(d.pop("user"))

        impersonate_admin_user_response_200 = cls(
            message=message,
            user=user,
        )

        impersonate_admin_user_response_200.additional_properties = d
        return impersonate_admin_user_response_200

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
