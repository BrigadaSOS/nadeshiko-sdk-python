from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReviewAllowlist")


@_attrs_define
class ReviewAllowlist:
    """
    Attributes:
        id (int): Allowlist entry ID
        check_name (str): Name of the check this entry applies to Example: lowSegmentMedia.
        media_id (int): Media ID to exclude Example: 42.
        created_at (datetime.datetime): When this entry was created
        episode_number (int | None | Unset): Episode number to exclude (null for media-level checks)
        reason (None | str | Unset): Why this was allowlisted Example: Known short OVA series.
    """

    id: int
    check_name: str
    media_id: int
    created_at: datetime.datetime
    episode_number: int | None | Unset = UNSET
    reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        check_name = self.check_name

        media_id = self.media_id

        created_at = self.created_at.isoformat()

        episode_number: int | None | Unset
        if isinstance(self.episode_number, Unset):
            episode_number = UNSET
        else:
            episode_number = self.episode_number

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "checkName": check_name,
                "mediaId": media_id,
                "createdAt": created_at,
            }
        )
        if episode_number is not UNSET:
            field_dict["episodeNumber"] = episode_number
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        check_name = d.pop("checkName")

        media_id = d.pop("mediaId")

        created_at = isoparse(d.pop("createdAt"))

        def _parse_episode_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        episode_number = _parse_episode_number(d.pop("episodeNumber", UNSET))

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        review_allowlist = cls(
            id=id,
            check_name=check_name,
            media_id=media_id,
            created_at=created_at,
            episode_number=episode_number,
            reason=reason,
        )

        review_allowlist.additional_properties = d
        return review_allowlist

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
