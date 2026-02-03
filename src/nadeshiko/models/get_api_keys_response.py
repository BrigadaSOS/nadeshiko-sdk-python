from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.api_key import ApiKey
    from ..models.quota_info import QuotaInfo


T = TypeVar("T", bound="GetApiKeysResponse")


@_attrs_define
class GetApiKeysResponse:
    """List of API keys response

    Attributes:
        keys (list[ApiKey]): List of API keys
        quota (QuotaInfo): User quota information
    """

    keys: list[ApiKey]
    quota: QuotaInfo
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keys = []
        for keys_item_data in self.keys:
            keys_item = keys_item_data.to_dict()
            keys.append(keys_item)

        quota = self.quota.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keys": keys,
                "quota": quota,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_key import ApiKey
        from ..models.quota_info import QuotaInfo

        d = dict(src_dict)
        keys = []
        _keys = d.pop("keys")
        for keys_item_data in _keys:
            keys_item = ApiKey.from_dict(keys_item_data)

            keys.append(keys_item)

        quota = QuotaInfo.from_dict(d.pop("quota"))

        get_api_keys_response = cls(
            keys=keys,
            quota=quota,
        )

        get_api_keys_response.additional_properties = d
        return get_api_keys_response

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
