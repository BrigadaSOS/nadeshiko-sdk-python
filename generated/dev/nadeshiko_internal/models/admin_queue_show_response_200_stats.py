from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AdminQueueShowResponse200Stats")


@_attrs_define
class AdminQueueShowResponse200Stats:
    """
    Attributes:
        deferred (int): Jobs scheduled for future execution (`start_after > now()`) Example: 1.
        queued (int): Jobs currently queued and waiting to be processed Example: 10.
        active (int): Jobs currently being processed Example: 2.
        total (int): Total jobs currently stored in the queue table Example: 13.
    """

    deferred: int
    queued: int
    active: int
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deferred = self.deferred

        queued = self.queued

        active = self.active

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deferred": deferred,
                "queued": queued,
                "active": active,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deferred = d.pop("deferred")

        queued = d.pop("queued")

        active = d.pop("active")

        total = d.pop("total")

        admin_queue_show_response_200_stats = cls(
            deferred=deferred,
            queued=queued,
            active=active,
            total=total,
        )

        admin_queue_show_response_200_stats.additional_properties = d
        return admin_queue_show_response_200_stats

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
