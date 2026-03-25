from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PurgeAdminQueueFailedResponse200")


@_attrs_define
class PurgeAdminQueueFailedResponse200:
    """
    Attributes:
        success (bool):  Example: True.
        purged_count (int): Number of failed jobs deleted Example: 15.
        message (str):  Example: Purged 15 failed jobs from es-sync-create.
    """

    success: bool
    purged_count: int
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        purged_count = self.purged_count

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "purgedCount": purged_count,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        success = _src.pop("success")

        purged_count = _src.pop("purgedCount")

        message = _src.pop("message")

        purge_admin_queue_failed_response_200 = cls(
            success=success,
            purged_count=purged_count,
            message=message,
        )

        purge_admin_queue_failed_response_200.additional_properties = _src
        return purge_admin_queue_failed_response_200

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
