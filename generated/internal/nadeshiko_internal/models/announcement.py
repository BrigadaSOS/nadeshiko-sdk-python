from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.announcement_type import AnnouncementType, check_announcement_type

T = TypeVar("T", bound="Announcement")


@_attrs_define
class Announcement:
    """Site-wide announcement banner

    Attributes:
        message (str): The banner text. Stored and returned verbatim; the web client renders a small inline markdown
            subset from it -- links, bold, italic, code spans and line breaks -- so `maxLength` counts the markup as well as
            the words. Anything outside that subset, raw HTML included, is shown as the characters it is made of rather than
            interpreted. Other clients are free to print it as plain text.
             Example: Scheduled maintenance tonight. See [the status page](/blog)..
        type_ (AnnouncementType):  Example: INFO.
        active (bool):  Example: True.
    """

    message: str
    type_: AnnouncementType
    active: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        type_: str = self.type_

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

        type_ = check_announcement_type(_src.pop("type"))

        active = _src.pop("active")

        announcement = cls(
            message=message,
            type_=type_,
            active=active,
        )

        announcement.additional_properties = _src
        return announcement

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
