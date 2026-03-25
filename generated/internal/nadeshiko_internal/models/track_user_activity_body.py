from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.track_user_activity_body_activity_type import TrackUserActivityBodyActivityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TrackUserActivityBody")


@_attrs_define
class TrackUserActivityBody:
    """
    Attributes:
        activity_type (TrackUserActivityBodyActivityType):
        segment_id (str | Unset):
        media_id (int | Unset):
        media_name (str | Unset):
        japanese_text (str | Unset):
        search_query (str | Unset):
    """

    activity_type: TrackUserActivityBodyActivityType
    segment_id: str | Unset = UNSET
    media_id: int | Unset = UNSET
    media_name: str | Unset = UNSET
    japanese_text: str | Unset = UNSET
    search_query: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity_type = self.activity_type.value

        segment_id = self.segment_id

        media_id = self.media_id

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
        if segment_id is not UNSET:
            field_dict["segmentId"] = segment_id
        if media_id is not UNSET:
            field_dict["mediaId"] = media_id
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
        activity_type = TrackUserActivityBodyActivityType(_src.pop("activityType"))

        segment_id = _src.pop("segmentId", UNSET)

        media_id = _src.pop("mediaId", UNSET)

        media_name = _src.pop("mediaName", UNSET)

        japanese_text = _src.pop("japaneseText", UNSET)

        search_query = _src.pop("searchQuery", UNSET)

        track_user_activity_body = cls(
            activity_type=activity_type,
            segment_id=segment_id,
            media_id=media_id,
            media_name=media_name,
            japanese_text=japanese_text,
            search_query=search_query,
        )

        track_user_activity_body.additional_properties = _src
        return track_user_activity_body

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
