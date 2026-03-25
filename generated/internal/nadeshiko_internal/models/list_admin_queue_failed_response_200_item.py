from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ListAdminQueueFailedResponse200Item")


@_attrs_define
class ListAdminQueueFailedResponse200Item:
    """
    Attributes:
        id (str): Job ID
        segment_id (int): The segment ID that failed to sync
        error (None | str): Error message from the last attempt
        created_on (datetime.datetime): When the job was created
    """

    id: str
    segment_id: int
    error: None | str
    created_on: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        segment_id = self.segment_id

        error: None | str
        error = self.error

        created_on = self.created_on.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "segmentId": segment_id,
                "error": error,
                "createdOn": created_on,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        id = _src.pop("id")

        segment_id = _src.pop("segmentId")

        def _parse_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error = _parse_error(_src.pop("error"))

        created_on = isoparse(_src.pop("createdOn"))

        list_admin_queue_failed_response_200_item = cls(
            id=id,
            segment_id=segment_id,
            error=error,
            created_on=created_on,
        )

        list_admin_queue_failed_response_200_item.additional_properties = _src
        return list_admin_queue_failed_response_200_item

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
