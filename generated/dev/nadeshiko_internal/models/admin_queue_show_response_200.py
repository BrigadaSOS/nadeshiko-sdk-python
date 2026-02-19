from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.admin_queue_show_response_200_metadata import AdminQueueShowResponse200Metadata
    from ..models.admin_queue_show_response_200_stats import AdminQueueShowResponse200Stats


T = TypeVar("T", bound="AdminQueueShowResponse200")


@_attrs_define
class AdminQueueShowResponse200:
    """
    Attributes:
        queue (str):  Example: es-sync-create.
        stats (AdminQueueShowResponse200Stats):
        metadata (AdminQueueShowResponse200Metadata):
    """

    queue: str
    stats: AdminQueueShowResponse200Stats
    metadata: AdminQueueShowResponse200Metadata
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        queue = self.queue

        stats = self.stats.to_dict()

        metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "queue": queue,
                "stats": stats,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admin_queue_show_response_200_metadata import (
            AdminQueueShowResponse200Metadata,
        )
        from ..models.admin_queue_show_response_200_stats import AdminQueueShowResponse200Stats

        d = dict(src_dict)
        queue = d.pop("queue")

        stats = AdminQueueShowResponse200Stats.from_dict(d.pop("stats"))

        metadata = AdminQueueShowResponse200Metadata.from_dict(d.pop("metadata"))

        admin_queue_show_response_200 = cls(
            queue=queue,
            stats=stats,
            metadata=metadata,
        )

        admin_queue_show_response_200.additional_properties = d
        return admin_queue_show_response_200

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
