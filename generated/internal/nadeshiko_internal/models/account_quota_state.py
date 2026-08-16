from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_quota_state_quota_source import (
    AccountQuotaStateQuotaSource,
    check_account_quota_state_quota_source,
)

T = TypeVar("T", bound="AccountQuotaState")


@_attrs_define
class AccountQuotaState:
    """
    Attributes:
        user_id (int):  Example: 328.
        tier_id (None | str): The tier this account sits on, or null if it has none Example: plus.
        quota_override (int | None): Per-account limit that wins over the tier when set
        monthly_quota_limit (int): The limit actually in force, after applying the resolution order Example: 25000.
        quota_source (AccountQuotaStateQuotaSource): Which step of the resolution order produced `monthlyQuotaLimit`.
            `legacy_column` and `default` mean the tier did not resolve, and are worth
            investigating rather than displaying.
             Example: tier.
        quota_used (int): Calls billed to this account in the current period Example: 4927.
        period_yyyymm (int): The billing period, as YYYYMM in UTC Example: 202608.
    """

    user_id: int
    tier_id: None | str
    quota_override: int | None
    monthly_quota_limit: int
    quota_source: AccountQuotaStateQuotaSource
    quota_used: int
    period_yyyymm: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        tier_id: None | str
        tier_id = self.tier_id

        quota_override: int | None
        quota_override = self.quota_override

        monthly_quota_limit = self.monthly_quota_limit

        quota_source: str = self.quota_source

        quota_used = self.quota_used

        period_yyyymm = self.period_yyyymm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "tierId": tier_id,
                "quotaOverride": quota_override,
                "monthlyQuotaLimit": monthly_quota_limit,
                "quotaSource": quota_source,
                "quotaUsed": quota_used,
                "periodYyyymm": period_yyyymm,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        user_id = _src.pop("userId")

        def _parse_tier_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tier_id = _parse_tier_id(_src.pop("tierId"))

        def _parse_quota_override(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        quota_override = _parse_quota_override(_src.pop("quotaOverride"))

        monthly_quota_limit = _src.pop("monthlyQuotaLimit")

        quota_source = check_account_quota_state_quota_source(_src.pop("quotaSource"))

        quota_used = _src.pop("quotaUsed")

        period_yyyymm = _src.pop("periodYyyymm")

        account_quota_state = cls(
            user_id=user_id,
            tier_id=tier_id,
            quota_override=quota_override,
            monthly_quota_limit=monthly_quota_limit,
            quota_source=quota_source,
            quota_used=quota_used,
            period_yyyymm=period_yyyymm,
        )

        account_quota_state.additional_properties = _src
        return account_quota_state

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
