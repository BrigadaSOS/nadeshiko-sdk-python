from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_me_quota_burst import UserMeQuotaBurst
    from ..models.user_me_quota_tier_type_0 import UserMeQuotaTierType0


T = TypeVar("T", bound="UserMeQuota")


@_attrs_define
class UserMeQuota:
    """
    Attributes:
        used (int): Number of API requests used this month. Example: 342.
        limit (int): Maximum number of API requests allowed per month. Example: 5000.
        remaining (int): Number of API requests remaining this month. Example: 4658.
        period_yyyymm (int): Current month in YYYYMM format. Example: 202602.
        period_start (datetime.datetime): Start of the current month (UTC). Example: 2026-02-01T00:00:00.000Z.
        period_end (datetime.datetime): End of the current month (UTC). Example: 2026-02-28T23:59:59.999Z.
        tier (None | UserMeQuotaTierType0): The quota tier this account sits on. Null when the account is on none,
            or when an override is in force and the tier no longer describes the
            limit.
        burst (UserMeQuotaBurst): The OTHER limit. Separate from the monthly allowance and enforced per
            API key over a short window, so a caller can exhaust it with plenty of
            month left -- which is why both are surfaced together, and why the two
            429s carry an `X-RateLimit-Reason` telling them apart.
    """

    used: int
    limit: int
    remaining: int
    period_yyyymm: int
    period_start: datetime.datetime
    period_end: datetime.datetime
    tier: None | UserMeQuotaTierType0
    burst: UserMeQuotaBurst
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_me_quota_tier_type_0 import UserMeQuotaTierType0

        used = self.used

        limit = self.limit

        remaining = self.remaining

        period_yyyymm = self.period_yyyymm

        period_start = self.period_start.isoformat()

        period_end = self.period_end.isoformat()

        tier: dict[str, Any] | None
        if isinstance(self.tier, UserMeQuotaTierType0):
            tier = self.tier.to_dict()
        else:
            tier = self.tier

        burst = self.burst.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "used": used,
                "limit": limit,
                "remaining": remaining,
                "periodYyyymm": period_yyyymm,
                "periodStart": period_start,
                "periodEnd": period_end,
                "tier": tier,
                "burst": burst,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_me_quota_burst import UserMeQuotaBurst
        from ..models.user_me_quota_tier_type_0 import UserMeQuotaTierType0

        _src = dict(src_dict)
        used = _src.pop("used")

        limit = _src.pop("limit")

        remaining = _src.pop("remaining")

        period_yyyymm = _src.pop("periodYyyymm")

        period_start = datetime.datetime.fromisoformat(_src.pop("periodStart"))

        period_end = datetime.datetime.fromisoformat(_src.pop("periodEnd"))

        def _parse_tier(data: object) -> None | UserMeQuotaTierType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tier_type_0 = UserMeQuotaTierType0.from_dict(data)

                return tier_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UserMeQuotaTierType0, data)

        tier = _parse_tier(_src.pop("tier"))

        burst = UserMeQuotaBurst.from_dict(_src.pop("burst"))

        user_me_quota = cls(
            used=used,
            limit=limit,
            remaining=remaining,
            period_yyyymm=period_yyyymm,
            period_start=period_start,
            period_end=period_end,
            tier=tier,
            burst=burst,
        )

        user_me_quota.additional_properties = _src
        return user_me_quota

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
