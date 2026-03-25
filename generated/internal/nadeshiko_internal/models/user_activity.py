from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.activity_type import ActivityType

T = TypeVar("T", bound="UserActivity")


@_attrs_define
class UserActivity:
    """
    Attributes:
        id (int):
        activity_type (ActivityType): Type of user activity
        segment_id (None | str):
        media_id (int | None):
        search_query (None | str):
        media_name (None | str):
        japanese_text (None | str):
        created_at (datetime.datetime):
    """

    id: int
    activity_type: ActivityType
    segment_id: None | str
    media_id: int | None
    search_query: None | str
    media_name: None | str
    japanese_text: None | str
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        activity_type = self.activity_type.value

        segment_id: None | str
        segment_id = self.segment_id

        media_id: int | None
        media_id = self.media_id

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
                "segmentId": segment_id,
                "mediaId": media_id,
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

        activity_type = ActivityType(_src.pop("activityType"))

        def _parse_segment_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        segment_id = _parse_segment_id(_src.pop("segmentId"))

        def _parse_media_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        media_id = _parse_media_id(_src.pop("mediaId"))

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

        created_at = isoparse(_src.pop("createdAt"))

        user_activity = cls(
            id=id,
            activity_type=activity_type,
            segment_id=segment_id,
            media_id=media_id,
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
