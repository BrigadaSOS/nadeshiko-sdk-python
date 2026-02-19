from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAdminReviewAllowlistEntryBody")


@_attrs_define
class CreateAdminReviewAllowlistEntryBody:
    """
    Attributes:
        check_name (str): Check name to allowlist for
        media_id (int): Media ID to allowlist
        episode_number (int | Unset): Episode number (for episode-level checks)
        reason (str | Unset): Reason for allowlisting
    """

    check_name: str
    media_id: int
    episode_number: int | Unset = UNSET
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        check_name = self.check_name

        media_id = self.media_id

        episode_number = self.episode_number

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "checkName": check_name,
                "mediaId": media_id,
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
        check_name = d.pop("checkName")

        media_id = d.pop("mediaId")

        episode_number = d.pop("episodeNumber", UNSET)

        reason = d.pop("reason", UNSET)

        create_admin_review_allowlist_entry_body = cls(
            check_name=check_name,
            media_id=media_id,
            episode_number=episode_number,
            reason=reason,
        )

        create_admin_review_allowlist_entry_body.additional_properties = d
        return create_admin_review_allowlist_entry_body

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
