from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminQueueShowResponse200Metadata")


@_attrs_define
class AdminQueueShowResponse200Metadata:
    """
    Attributes:
        policy (str):  Example: standard.
        partition (bool):
        created_on (datetime.datetime):
        updated_on (datetime.datetime):
        singletons_active (list[str]):
        table (str):  Example: job.
        dead_letter (None | str | Unset):
        warning_queue_size (int | None | Unset):
        retry_limit (int | None | Unset):  Example: 5.
        retry_delay (int | None | Unset): Initial retry delay in seconds Example: 1.
        retry_backoff (bool | None | Unset):  Example: True.
        retry_delay_max (int | None | Unset):
        expire_in_seconds (int | None | Unset):  Example: 3600.
        retention_seconds (int | None | Unset):  Example: 86400.
        delete_after_seconds (int | None | Unset):
    """

    policy: str
    partition: bool
    created_on: datetime.datetime
    updated_on: datetime.datetime
    singletons_active: list[str]
    table: str
    dead_letter: None | str | Unset = UNSET
    warning_queue_size: int | None | Unset = UNSET
    retry_limit: int | None | Unset = UNSET
    retry_delay: int | None | Unset = UNSET
    retry_backoff: bool | None | Unset = UNSET
    retry_delay_max: int | None | Unset = UNSET
    expire_in_seconds: int | None | Unset = UNSET
    retention_seconds: int | None | Unset = UNSET
    delete_after_seconds: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        policy = self.policy

        partition = self.partition

        created_on = self.created_on.isoformat()

        updated_on = self.updated_on.isoformat()

        singletons_active = self.singletons_active

        table = self.table

        dead_letter: None | str | Unset
        if isinstance(self.dead_letter, Unset):
            dead_letter = UNSET
        else:
            dead_letter = self.dead_letter

        warning_queue_size: int | None | Unset
        if isinstance(self.warning_queue_size, Unset):
            warning_queue_size = UNSET
        else:
            warning_queue_size = self.warning_queue_size

        retry_limit: int | None | Unset
        if isinstance(self.retry_limit, Unset):
            retry_limit = UNSET
        else:
            retry_limit = self.retry_limit

        retry_delay: int | None | Unset
        if isinstance(self.retry_delay, Unset):
            retry_delay = UNSET
        else:
            retry_delay = self.retry_delay

        retry_backoff: bool | None | Unset
        if isinstance(self.retry_backoff, Unset):
            retry_backoff = UNSET
        else:
            retry_backoff = self.retry_backoff

        retry_delay_max: int | None | Unset
        if isinstance(self.retry_delay_max, Unset):
            retry_delay_max = UNSET
        else:
            retry_delay_max = self.retry_delay_max

        expire_in_seconds: int | None | Unset
        if isinstance(self.expire_in_seconds, Unset):
            expire_in_seconds = UNSET
        else:
            expire_in_seconds = self.expire_in_seconds

        retention_seconds: int | None | Unset
        if isinstance(self.retention_seconds, Unset):
            retention_seconds = UNSET
        else:
            retention_seconds = self.retention_seconds

        delete_after_seconds: int | None | Unset
        if isinstance(self.delete_after_seconds, Unset):
            delete_after_seconds = UNSET
        else:
            delete_after_seconds = self.delete_after_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "policy": policy,
                "partition": partition,
                "createdOn": created_on,
                "updatedOn": updated_on,
                "singletonsActive": singletons_active,
                "table": table,
            }
        )
        if dead_letter is not UNSET:
            field_dict["deadLetter"] = dead_letter
        if warning_queue_size is not UNSET:
            field_dict["warningQueueSize"] = warning_queue_size
        if retry_limit is not UNSET:
            field_dict["retryLimit"] = retry_limit
        if retry_delay is not UNSET:
            field_dict["retryDelay"] = retry_delay
        if retry_backoff is not UNSET:
            field_dict["retryBackoff"] = retry_backoff
        if retry_delay_max is not UNSET:
            field_dict["retryDelayMax"] = retry_delay_max
        if expire_in_seconds is not UNSET:
            field_dict["expireInSeconds"] = expire_in_seconds
        if retention_seconds is not UNSET:
            field_dict["retentionSeconds"] = retention_seconds
        if delete_after_seconds is not UNSET:
            field_dict["deleteAfterSeconds"] = delete_after_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        policy = d.pop("policy")

        partition = d.pop("partition")

        created_on = isoparse(d.pop("createdOn"))

        updated_on = isoparse(d.pop("updatedOn"))

        singletons_active = cast(list[str], d.pop("singletonsActive"))

        table = d.pop("table")

        def _parse_dead_letter(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dead_letter = _parse_dead_letter(d.pop("deadLetter", UNSET))

        def _parse_warning_queue_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        warning_queue_size = _parse_warning_queue_size(d.pop("warningQueueSize", UNSET))

        def _parse_retry_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retry_limit = _parse_retry_limit(d.pop("retryLimit", UNSET))

        def _parse_retry_delay(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retry_delay = _parse_retry_delay(d.pop("retryDelay", UNSET))

        def _parse_retry_backoff(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        retry_backoff = _parse_retry_backoff(d.pop("retryBackoff", UNSET))

        def _parse_retry_delay_max(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retry_delay_max = _parse_retry_delay_max(d.pop("retryDelayMax", UNSET))

        def _parse_expire_in_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expire_in_seconds = _parse_expire_in_seconds(d.pop("expireInSeconds", UNSET))

        def _parse_retention_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retention_seconds = _parse_retention_seconds(d.pop("retentionSeconds", UNSET))

        def _parse_delete_after_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        delete_after_seconds = _parse_delete_after_seconds(d.pop("deleteAfterSeconds", UNSET))

        admin_queue_show_response_200_metadata = cls(
            policy=policy,
            partition=partition,
            created_on=created_on,
            updated_on=updated_on,
            singletons_active=singletons_active,
            table=table,
            dead_letter=dead_letter,
            warning_queue_size=warning_queue_size,
            retry_limit=retry_limit,
            retry_delay=retry_delay,
            retry_backoff=retry_backoff,
            retry_delay_max=retry_delay_max,
            expire_in_seconds=expire_in_seconds,
            retention_seconds=retention_seconds,
            delete_after_seconds=delete_after_seconds,
        )

        admin_queue_show_response_200_metadata.additional_properties = d
        return admin_queue_show_response_200_metadata

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
