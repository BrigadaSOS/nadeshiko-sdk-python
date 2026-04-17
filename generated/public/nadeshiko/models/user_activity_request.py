from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_activity_request_activity_type import UserActivityRequestActivityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserActivityRequest")


@_attrs_define
class UserActivityRequest:
    """Request body for tracking a user activity event

    Attributes:
        activity_type (UserActivityRequestActivityType):
        segment_public_id (str | Unset):
        media_public_id (str | Unset):
        media_name (str | Unset):
        japanese_text (str | Unset):
        search_query (str | Unset):
    """

    activity_type: UserActivityRequestActivityType
    segment_public_id: str | Unset = UNSET
    media_public_id: str | Unset = UNSET
    media_name: str | Unset = UNSET
    japanese_text: str | Unset = UNSET
    search_query: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity_type = self.activity_type.value

        segment_public_id = self.segment_public_id

        media_public_id = self.media_public_id

        media_name = self.media_name

        japanese_text = self.japanese_text

        search_query = self.search_query

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "activityType": activity_type,
            }
        )
        if segment_public_id is not UNSET:
            field_dict["segmentPublicId"] = segment_public_id
        if media_public_id is not UNSET:
            field_dict["mediaPublicId"] = media_public_id
        if media_name is not UNSET:
            field_dict["mediaName"] = media_name
        if japanese_text is not UNSET:
            field_dict["japaneseText"] = japanese_text
        if search_query is not UNSET:
            field_dict["searchQuery"] = search_query

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        activity_type = UserActivityRequestActivityType(_src.pop("activityType"))

        segment_public_id = _src.pop("segmentPublicId", UNSET)

        media_public_id = _src.pop("mediaPublicId", UNSET)

        media_name = _src.pop("mediaName", UNSET)

        japanese_text = _src.pop("japaneseText", UNSET)

        search_query = _src.pop("searchQuery", UNSET)

        user_activity_request = cls(
            activity_type=activity_type,
            segment_public_id=segment_public_id,
            media_public_id=media_public_id,
            media_name=media_name,
            japanese_text=japanese_text,
            search_query=search_query,
        )

        user_activity_request.additional_properties = _src
        return user_activity_request

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
