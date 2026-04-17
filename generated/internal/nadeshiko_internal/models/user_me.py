from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_me_quota import UserMeQuota
    from ..models.user_me_user import UserMeUser


T = TypeVar("T", bound="UserMe")


@_attrs_define
class UserMe:
    """
    Attributes:
        user (UserMeUser):
        quota (UserMeQuota):
    """

    user: UserMeUser
    quota: UserMeQuota
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user.to_dict()

        quota = self.quota.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
                "quota": quota,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_me_quota import UserMeQuota
        from ..models.user_me_user import UserMeUser

        _src = dict(src_dict)
        user = UserMeUser.from_dict(_src.pop("user"))

        quota = UserMeQuota.from_dict(_src.pop("quota"))

        user_me = cls(
            user=user,
            quota=quota,
        )

        user_me.additional_properties = _src
        return user_me

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
