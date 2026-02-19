from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_admin_queue_response_200_metadata import GetAdminQueueResponse200Metadata
    from ..models.get_admin_queue_response_200_stats import GetAdminQueueResponse200Stats


T = TypeVar("T", bound="GetAdminQueueResponse200")


@_attrs_define
class GetAdminQueueResponse200:
    """
    Attributes:
        queue (str):  Example: es-sync-create.
        stats (GetAdminQueueResponse200Stats):
        metadata (GetAdminQueueResponse200Metadata):
    """

    queue: str
    stats: GetAdminQueueResponse200Stats
    metadata: GetAdminQueueResponse200Metadata
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
        from ..models.get_admin_queue_response_200_metadata import GetAdminQueueResponse200Metadata
        from ..models.get_admin_queue_response_200_stats import GetAdminQueueResponse200Stats

        d = dict(src_dict)
        queue = d.pop("queue")

        stats = GetAdminQueueResponse200Stats.from_dict(d.pop("stats"))

        metadata = GetAdminQueueResponse200Metadata.from_dict(d.pop("metadata"))

        get_admin_queue_response_200 = cls(
            queue=queue,
            stats=stats,
            metadata=metadata,
        )

        get_admin_queue_response_200.additional_properties = d
        return get_admin_queue_response_200

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
