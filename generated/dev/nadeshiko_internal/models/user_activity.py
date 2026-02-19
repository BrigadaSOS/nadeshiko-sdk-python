from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.activity_type import ActivityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserActivity")


@_attrs_define
class UserActivity:
    """
    Attributes:
        id (int):
        activity_type (ActivityType): Type of user activity
        created_at (datetime.datetime):
        segment_uuid (None | str | Unset):
        media_id (int | None | Unset):
        search_query (None | str | Unset):
        anime_name (None | str | Unset):
        japanese_text (None | str | Unset):
    """

    id: int
    activity_type: ActivityType
    created_at: datetime.datetime
    segment_uuid: None | str | Unset = UNSET
    media_id: int | None | Unset = UNSET
    search_query: None | str | Unset = UNSET
    anime_name: None | str | Unset = UNSET
    japanese_text: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        activity_type = self.activity_type.value

        created_at = self.created_at.isoformat()

        segment_uuid: None | str | Unset
        if isinstance(self.segment_uuid, Unset):
            segment_uuid = UNSET
        else:
            segment_uuid = self.segment_uuid

        media_id: int | None | Unset
        if isinstance(self.media_id, Unset):
            media_id = UNSET
        else:
            media_id = self.media_id

        search_query: None | str | Unset
        if isinstance(self.search_query, Unset):
            search_query = UNSET
        else:
            search_query = self.search_query

        anime_name: None | str | Unset
        if isinstance(self.anime_name, Unset):
            anime_name = UNSET
        else:
            anime_name = self.anime_name

        japanese_text: None | str | Unset
        if isinstance(self.japanese_text, Unset):
            japanese_text = UNSET
        else:
            japanese_text = self.japanese_text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "activityType": activity_type,
                "createdAt": created_at,
            }
        )
        if segment_uuid is not UNSET:
            field_dict["segmentUuid"] = segment_uuid
        if media_id is not UNSET:
            field_dict["mediaId"] = media_id
        if search_query is not UNSET:
            field_dict["searchQuery"] = search_query
        if anime_name is not UNSET:
            field_dict["animeName"] = anime_name
        if japanese_text is not UNSET:
            field_dict["japaneseText"] = japanese_text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        activity_type = ActivityType(d.pop("activityType"))

        created_at = isoparse(d.pop("createdAt"))

        def _parse_segment_uuid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        segment_uuid = _parse_segment_uuid(d.pop("segmentUuid", UNSET))

        def _parse_media_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        media_id = _parse_media_id(d.pop("mediaId", UNSET))

        def _parse_search_query(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search_query = _parse_search_query(d.pop("searchQuery", UNSET))

        def _parse_anime_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        anime_name = _parse_anime_name(d.pop("animeName", UNSET))

        def _parse_japanese_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        japanese_text = _parse_japanese_text(d.pop("japaneseText", UNSET))

        user_activity = cls(
            id=id,
            activity_type=activity_type,
            created_at=created_at,
            segment_uuid=segment_uuid,
            media_id=media_id,
            search_query=search_query,
            anime_name=anime_name,
            japanese_text=japanese_text,
        )

        user_activity.additional_properties = d
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
