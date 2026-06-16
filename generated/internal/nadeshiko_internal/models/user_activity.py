from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_type import ActivityType, check_activity_type

T = TypeVar("T", bound="UserActivity")


@_attrs_define
class UserActivity:
    """
    Attributes:
        id (int):
        activity_type (ActivityType): Type of user activity
        segment_public_id (None | str):
        media_public_id (None | str):
        search_query (None | str):
        media_name (None | str):
        japanese_text (None | str):
        created_at (datetime.datetime):
    """

    id: int
    activity_type: ActivityType
    segment_public_id: None | str
    media_public_id: None | str
    search_query: None | str
    media_name: None | str
    japanese_text: None | str
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        activity_type: str = self.activity_type

        segment_public_id: None | str
        segment_public_id = self.segment_public_id

        media_public_id: None | str
        media_public_id = self.media_public_id

        search_query: None | str
        search_query = self.search_query

        media_name: None | str
        media_name = self.media_name

        japanese_text: None | str
        japanese_text = self.japanese_text

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "activityType": activity_type,
                "segmentPublicId": segment_public_id,
                "mediaPublicId": media_public_id,
                "searchQuery": search_query,
                "mediaName": media_name,
                "japaneseText": japanese_text,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        id = _src.pop("id")

        activity_type = check_activity_type(_src.pop("activityType"))

        def _parse_segment_public_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        segment_public_id = _parse_segment_public_id(_src.pop("segmentPublicId"))

        def _parse_media_public_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        media_public_id = _parse_media_public_id(_src.pop("mediaPublicId"))

        def _parse_search_query(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        search_query = _parse_search_query(_src.pop("searchQuery"))

        def _parse_media_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        media_name = _parse_media_name(_src.pop("mediaName"))

        def _parse_japanese_text(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        japanese_text = _parse_japanese_text(_src.pop("japaneseText"))

        created_at = datetime.datetime.fromisoformat(_src.pop("createdAt"))

        user_activity = cls(
            id=id,
            activity_type=activity_type,
            segment_public_id=segment_public_id,
            media_public_id=media_public_id,
            search_query=search_query,
            media_name=media_name,
            japanese_text=japanese_text,
            created_at=created_at,
        )

        user_activity.additional_properties = _src
        return user_activity

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
