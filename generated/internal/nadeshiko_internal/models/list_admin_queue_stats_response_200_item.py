from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListAdminQueueStatsResponse200Item")


@_attrs_define
class ListAdminQueueStatsResponse200Item:
    """
    Attributes:
        queue (str):  Example: es-sync-create.
        stuck_count (int): Number of jobs currently pending/active Example: 5.
        failed_count (int): Number of failed jobs Example: 2.
    """

    queue: str
    stuck_count: int
    failed_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        queue = self.queue

        stuck_count = self.stuck_count

        failed_count = self.failed_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "queue": queue,
                "stuckCount": stuck_count,
                "failedCount": failed_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        queue = _src.pop("queue")

        stuck_count = _src.pop("stuckCount")

        failed_count = _src.pop("failedCount")

        list_admin_queue_stats_response_200_item = cls(
            queue=queue,
            stuck_count=stuck_count,
            failed_count=failed_count,
        )

        list_admin_queue_stats_response_200_item.additional_properties = _src
        return list_admin_queue_stats_response_200_item

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
