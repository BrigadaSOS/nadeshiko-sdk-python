from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="UserQuotaResponse")


@_attrs_define
class UserQuotaResponse:
    """
    Attributes:
        quota_used (int): Number of API requests used in the current billing period. Example: 342.
        quota_limit (int): Maximum number of API requests allowed in the current billing period. Example: 2500.
        quota_remaining (int): Number of API requests remaining in the current billing period. Example: 2158.
        period_yyyymm (int): Current billing period in YYYYMM format. Example: 202602.
        period_start (datetime.datetime): Start of the current billing period (UTC). Example: 2026-02-01T00:00:00.000Z.
        period_end (datetime.datetime): End of the current billing period (UTC). Example: 2026-02-28T23:59:59.999Z.
    """

    quota_used: int
    quota_limit: int
    quota_remaining: int
    period_yyyymm: int
    period_start: datetime.datetime
    period_end: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quota_used = self.quota_used

        quota_limit = self.quota_limit

        quota_remaining = self.quota_remaining

        period_yyyymm = self.period_yyyymm

        period_start = self.period_start.isoformat()

        period_end = self.period_end.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quotaUsed": quota_used,
                "quotaLimit": quota_limit,
                "quotaRemaining": quota_remaining,
                "periodYyyymm": period_yyyymm,
                "periodStart": period_start,
                "periodEnd": period_end,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        quota_used = d.pop("quotaUsed")

        quota_limit = d.pop("quotaLimit")

        quota_remaining = d.pop("quotaRemaining")

        period_yyyymm = d.pop("periodYyyymm")

        period_start = isoparse(d.pop("periodStart"))

        period_end = isoparse(d.pop("periodEnd"))

        user_quota_response = cls(
            quota_used=quota_used,
            quota_limit=quota_limit,
            quota_remaining=quota_remaining,
            period_yyyymm=period_yyyymm,
            period_start=period_start,
            period_end=period_end,
        )

        user_quota_response.additional_properties = d
        return user_quota_response

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
