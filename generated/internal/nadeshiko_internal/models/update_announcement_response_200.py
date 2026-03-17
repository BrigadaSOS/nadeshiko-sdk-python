from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_announcement_response_200_type import UpdateAnnouncementResponse200Type

T = TypeVar("T", bound="UpdateAnnouncementResponse200")


@_attrs_define
class UpdateAnnouncementResponse200:
    """
    Attributes:
        message (str):
        type_ (UpdateAnnouncementResponse200Type):
        active (bool):
    """

    message: str
    type_: UpdateAnnouncementResponse200Type
    active: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        type_ = self.type_.value

        active = self.active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "type": type_,
                "active": active,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        type_ = UpdateAnnouncementResponse200Type(d.pop("type"))

        active = d.pop("active")

        update_announcement_response_200 = cls(
            message=message,
            type_=type_,
            active=active,
        )

        update_announcement_response_200.additional_properties = d
        return update_announcement_response_200

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
