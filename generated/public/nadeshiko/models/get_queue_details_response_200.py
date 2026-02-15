from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetQueueDetailsResponse200")



@_attrs_define
class GetQueueDetailsResponse200:
    """ 
        Attributes:
            queue (str | Unset):  Example: es-sync-create.
            size (int | Unset): Current queue size (pending jobs) Example: 10.
            created (int | Unset): Total jobs created Example: 1250.
            failed (int | Unset): Total failed jobs Example: 5.
            complete (int | Unset): Total completed jobs Example: 1235.
            expired (int | Unset): Total expired jobs Example: 2.
            cancelled (int | Unset): Total cancelled jobs Example: 3.
     """

    queue: str | Unset = UNSET
    size: int | Unset = UNSET
    created: int | Unset = UNSET
    failed: int | Unset = UNSET
    complete: int | Unset = UNSET
    expired: int | Unset = UNSET
    cancelled: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        queue = self.queue

        size = self.size

        created = self.created

        failed = self.failed

        complete = self.complete

        expired = self.expired

        cancelled = self.cancelled


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if queue is not UNSET:
            field_dict["queue"] = queue
        if size is not UNSET:
            field_dict["size"] = size
        if created is not UNSET:
            field_dict["created"] = created
        if failed is not UNSET:
            field_dict["failed"] = failed
        if complete is not UNSET:
            field_dict["complete"] = complete
        if expired is not UNSET:
            field_dict["expired"] = expired
        if cancelled is not UNSET:
            field_dict["cancelled"] = cancelled

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        queue = d.pop("queue", UNSET)

        size = d.pop("size", UNSET)

        created = d.pop("created", UNSET)

        failed = d.pop("failed", UNSET)

        complete = d.pop("complete", UNSET)

        expired = d.pop("expired", UNSET)

        cancelled = d.pop("cancelled", UNSET)

        get_queue_details_response_200 = cls(
            queue=queue,
            size=size,
            created=created,
            failed=failed,
            complete=complete,
            expired=expired,
            cancelled=cancelled,
        )


        get_queue_details_response_200.additional_properties = d
        return get_queue_details_response_200

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
