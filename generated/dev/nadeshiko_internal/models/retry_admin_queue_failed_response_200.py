from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RetryAdminQueueFailedResponse200")


@_attrs_define
class RetryAdminQueueFailedResponse200:
    """
    Attributes:
        success (bool | Unset):  Example: True.
        retried_count (int | Unset): Number of jobs queued for retry Example: 5.
        message (str | Unset):  Example: Retried 5 failed jobs from es-sync-create.
    """

    success: bool | Unset = UNSET
    retried_count: int | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        retried_count = self.retried_count

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if retried_count is not UNSET:
            field_dict["retriedCount"] = retried_count
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success", UNSET)

        retried_count = d.pop("retriedCount", UNSET)

        message = d.pop("message", UNSET)

        retry_admin_queue_failed_response_200 = cls(
            success=success,
            retried_count=retried_count,
            message=message,
        )

        retry_admin_queue_failed_response_200.additional_properties = d
        return retry_admin_queue_failed_response_200

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
