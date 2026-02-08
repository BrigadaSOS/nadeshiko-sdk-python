from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetQueueStatsResponse200Item")



@_attrs_define
class GetQueueStatsResponse200Item:
    """ 
        Attributes:
            queue (str | Unset):  Example: es-sync-create.
            stuck_count (int | Unset): Number of jobs currently pending/active Example: 5.
            failed_count (int | Unset): Number of failed jobs Example: 2.
     """

    queue: str | Unset = UNSET
    stuck_count: int | Unset = UNSET
    failed_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        queue = self.queue

        stuck_count = self.stuck_count

        failed_count = self.failed_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if queue is not UNSET:
            field_dict["queue"] = queue
        if stuck_count is not UNSET:
            field_dict["stuckCount"] = stuck_count
        if failed_count is not UNSET:
            field_dict["failedCount"] = failed_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        queue = d.pop("queue", UNSET)

        stuck_count = d.pop("stuckCount", UNSET)

        failed_count = d.pop("failedCount", UNSET)

        get_queue_stats_response_200_item = cls(
            queue=queue,
            stuck_count=stuck_count,
            failed_count=failed_count,
        )


        get_queue_stats_response_200_item.additional_properties = d
        return get_queue_stats_response_200_item

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
