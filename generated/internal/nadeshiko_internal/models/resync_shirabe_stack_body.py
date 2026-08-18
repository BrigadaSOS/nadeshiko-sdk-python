from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ResyncShirabeStackBody")


@_attrs_define
class ResyncShirabeStackBody:
    """
    Attributes:
        stack_fingerprint (str): The fingerprint Shirabe returned on the lookup.
    """

    stack_fingerprint: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stack_fingerprint = self.stack_fingerprint

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stackFingerprint": stack_fingerprint,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        stack_fingerprint = _src.pop("stackFingerprint")

        resync_shirabe_stack_body = cls(
            stack_fingerprint=stack_fingerprint,
        )

        resync_shirabe_stack_body.additional_properties = _src
        return resync_shirabe_stack_body

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
