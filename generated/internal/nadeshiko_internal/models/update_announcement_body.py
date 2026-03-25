from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_announcement_body_type import UpdateAnnouncementBodyType

T = TypeVar("T", bound="UpdateAnnouncementBody")


@_attrs_define
class UpdateAnnouncementBody:
    """
    Attributes:
        message (str):
        type_ (UpdateAnnouncementBodyType):
        active (bool):
    """

    message: str
    type_: UpdateAnnouncementBodyType
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
        _src = dict(src_dict)
        message = _src.pop("message")

        type_ = UpdateAnnouncementBodyType(_src.pop("type"))

        active = _src.pop("active")

        update_announcement_body = cls(
            message=message,
            type_=type_,
            active=active,
        )

        update_announcement_body.additional_properties = _src
        return update_announcement_body

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
