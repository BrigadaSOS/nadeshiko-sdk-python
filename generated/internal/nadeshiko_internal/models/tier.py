from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Tier")


@_attrs_define
class Tier:
    """
    Attributes:
        id (str): Stable slug referenced by an account's `tierId` Example: plus.
        display_name (str):  Example: Plus.
        monthly_quota_limit (int): API calls allowed per calendar month on this tier Example: 25000.
        sort_order (int): Display order; the id is a slug, not a rank Example: 10.
        rate_limit_max (int | None | Unset): Per-key burst allowance stamped onto keys created while on this tier.
            Null inherits the deployment-wide default.
        rate_limit_window_ms (int | None | Unset): Window for `rateLimitMax`, in milliseconds. Null inherits the
            default.
    """

    id: str
    display_name: str
    monthly_quota_limit: int
    sort_order: int
    rate_limit_max: int | None | Unset = UNSET
    rate_limit_window_ms: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        display_name = self.display_name

        monthly_quota_limit = self.monthly_quota_limit

        sort_order = self.sort_order

        rate_limit_max: int | None | Unset
        if isinstance(self.rate_limit_max, Unset):
            rate_limit_max = UNSET
        else:
            rate_limit_max = self.rate_limit_max

        rate_limit_window_ms: int | None | Unset
        if isinstance(self.rate_limit_window_ms, Unset):
            rate_limit_window_ms = UNSET
        else:
            rate_limit_window_ms = self.rate_limit_window_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "displayName": display_name,
                "monthlyQuotaLimit": monthly_quota_limit,
                "sortOrder": sort_order,
            }
        )
        if rate_limit_max is not UNSET:
            field_dict["rateLimitMax"] = rate_limit_max
        if rate_limit_window_ms is not UNSET:
            field_dict["rateLimitWindowMs"] = rate_limit_window_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        id = _src.pop("id")

        display_name = _src.pop("displayName")

        monthly_quota_limit = _src.pop("monthlyQuotaLimit")

        sort_order = _src.pop("sortOrder")

        def _parse_rate_limit_max(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rate_limit_max = _parse_rate_limit_max(_src.pop("rateLimitMax", UNSET))

        def _parse_rate_limit_window_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rate_limit_window_ms = _parse_rate_limit_window_ms(_src.pop("rateLimitWindowMs", UNSET))

        tier = cls(
            id=id,
            display_name=display_name,
            monthly_quota_limit=monthly_quota_limit,
            sort_order=sort_order,
            rate_limit_max=rate_limit_max,
            rate_limit_window_ms=rate_limit_window_ms,
        )

        tier.additional_properties = _src
        return tier

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
