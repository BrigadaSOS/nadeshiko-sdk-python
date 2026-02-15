from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="GetFailedJobsResponse200Item")



@_attrs_define
class GetFailedJobsResponse200Item:
    """ 
        Attributes:
            id (str | Unset): Job ID
            segment_id (int | Unset): The segment ID that failed to sync
            error (None | str | Unset): Error message from the last attempt
            created_on (datetime.datetime | Unset): When the job was created
     """

    id: str | Unset = UNSET
    segment_id: int | Unset = UNSET
    error: None | str | Unset = UNSET
    created_on: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        segment_id = self.segment_id

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        created_on: str | Unset = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if segment_id is not UNSET:
            field_dict["segmentId"] = segment_id
        if error is not UNSET:
            field_dict["error"] = error
        if created_on is not UNSET:
            field_dict["createdOn"] = created_on

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        segment_id = d.pop("segmentId", UNSET)

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))


        _created_on = d.pop("createdOn", UNSET)
        created_on: datetime.datetime | Unset
        if isinstance(_created_on,  Unset):
            created_on = UNSET
        else:
            created_on = isoparse(_created_on)




        get_failed_jobs_response_200_item = cls(
            id=id,
            segment_id=segment_id,
            error=error,
            created_on=created_on,
        )


        get_failed_jobs_response_200_item.additional_properties = d
        return get_failed_jobs_response_200_item

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
