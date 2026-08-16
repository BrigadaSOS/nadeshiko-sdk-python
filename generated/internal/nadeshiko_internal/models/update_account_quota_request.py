from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAccountQuotaRequest")


@_attrs_define
class UpdateAccountQuotaRequest:
    """At least one property must be present. Send `quotaOverride: null` to clear an
    override and fall back to the tier.

        Attributes:
            tier_id (str | Unset): Slug of an existing tier Example: plus.
            quota_override (int | None | Unset): Per-account monthly limit, taking precedence over the tier. Null clears it.
                 Example: 50000.
            reason (str | Unset): Why the change is being made. Recorded on the audit log line so the number
                is reviewable later; the old model's whole problem was that a raised limit
                carried no record of the decision behind it.
                 Example: Support ticket #412 - open-source dictionary integration.
    """

    tier_id: str | Unset = UNSET
    quota_override: int | None | Unset = UNSET
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tier_id = self.tier_id

        quota_override: int | None | Unset
        if isinstance(self.quota_override, Unset):
            quota_override = UNSET
        else:
            quota_override = self.quota_override

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tier_id is not UNSET:
            field_dict["tierId"] = tier_id
        if quota_override is not UNSET:
            field_dict["quotaOverride"] = quota_override
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        tier_id = _src.pop("tierId", UNSET)

        def _parse_quota_override(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        quota_override = _parse_quota_override(_src.pop("quotaOverride", UNSET))

        reason = _src.pop("reason", UNSET)

        update_account_quota_request = cls(
            tier_id=tier_id,
            quota_override=quota_override,
            reason=reason,
        )

        update_account_quota_request.additional_properties = _src
        return update_account_quota_request

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
