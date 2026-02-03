from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.quota_info_quota_limit_type_1 import QuotaInfoQuotaLimitType1

T = TypeVar("T", bound="QuotaInfo")


@_attrs_define
class QuotaInfo:
    """User quota information

    Attributes:
        quota_used (int): Number of API requests used this month
        quota_limit (int | QuotaInfoQuotaLimitType1):
    """

    quota_used: int
    quota_limit: int | QuotaInfoQuotaLimitType1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quota_used = self.quota_used

        quota_limit: int | str
        if isinstance(self.quota_limit, QuotaInfoQuotaLimitType1):
            quota_limit = self.quota_limit.value
        else:
            quota_limit = self.quota_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quotaUsed": quota_used,
                "quotaLimit": quota_limit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        quota_used = d.pop("quotaUsed")

        def _parse_quota_limit(data: object) -> int | QuotaInfoQuotaLimitType1:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                quota_limit_type_1 = QuotaInfoQuotaLimitType1(data)

                return quota_limit_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(int | QuotaInfoQuotaLimitType1, data)

        quota_limit = _parse_quota_limit(d.pop("quotaLimit"))

        quota_info = cls(
            quota_used=quota_used,
            quota_limit=quota_limit,
        )

        quota_info.additional_properties = d
        return quota_info

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
