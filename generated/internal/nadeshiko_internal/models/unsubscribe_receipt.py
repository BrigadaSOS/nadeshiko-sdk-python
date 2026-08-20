from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UnsubscribeReceipt")


@_attrs_define
class UnsubscribeReceipt:
    """
    Attributes:
        unsubscribed (bool): Always `true` when the token was readable. A token for an account that has
            since been deleted also answers `true`: the end state the caller asked for
            already holds, and there is nothing for them to act on.
             Example: True.
    """

    unsubscribed: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unsubscribed = self.unsubscribed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unsubscribed": unsubscribed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        unsubscribed = _src.pop("unsubscribed")

        unsubscribe_receipt = cls(
            unsubscribed=unsubscribed,
        )

        unsubscribe_receipt.additional_properties = _src
        return unsubscribe_receipt

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
