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
        segment_uuid (str | Unset):
        media_id (int | Unset):
        anime_name (str | Unset):
        japanese_text (str | Unset):
    """

    activity_type: TrackUserActivityBodyActivityType
    segment_uuid: str | Unset = UNSET
    media_id: int | Unset = UNSET
    anime_name: str | Unset = UNSET
    japanese_text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity_type = self.activity_type.value

        segment_uuid = self.segment_uuid

        media_id = self.media_id

        anime_name = self.anime_name

        japanese_text = self.japanese_text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "activityType": activity_type,
            }
        )
        if segment_uuid is not UNSET:
            field_dict["segmentUuid"] = segment_uuid
        if media_id is not UNSET:
            field_dict["mediaId"] = media_id
        if anime_name is not UNSET:
            field_dict["animeName"] = anime_name
        if japanese_text is not UNSET:
            field_dict["japaneseText"] = japanese_text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        activity_type = TrackUserActivityBodyActivityType(d.pop("activityType"))

        segment_uuid = d.pop("segmentUuid", UNSET)

        media_id = d.pop("mediaId", UNSET)

        anime_name = d.pop("animeName", UNSET)

        japanese_text = d.pop("japaneseText", UNSET)

        track_user_activity_body = cls(
            activity_type=activity_type,
            segment_uuid=segment_uuid,
            media_id=media_id,
            anime_name=anime_name,
            japanese_text=japanese_text,
        )

        track_user_activity_body.additional_properties = d
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
