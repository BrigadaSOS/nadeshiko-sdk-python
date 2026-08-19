from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserMeQuotaBurst")


@_attrs_define
class UserMeQuotaBurst:
    """The OTHER limit. Separate from the monthly allowance and enforced per
    API key over a short window, so a caller can exhaust it with plenty of
    month left -- which is why both are surfaced together, and why the two
    429s carry an `X-RateLimit-Reason` telling them apart.

        Attributes:
            max_ (int): Requests allowed per key within `windowMs`. Example: 150.
            window_ms (int): Length of the burst window, in milliseconds. Example: 60000.
    """

    max_: int
    window_ms: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_ = self.max_

        window_ms = self.window_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "max": max_,
                "windowMs": window_ms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        max_ = _src.pop("max")

        window_ms = _src.pop("windowMs")

        user_me_quota_burst = cls(
            max_=max_,
            window_ms=window_ms,
        )

        user_me_quota_burst.additional_properties = _src
        return user_me_quota_burst

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
