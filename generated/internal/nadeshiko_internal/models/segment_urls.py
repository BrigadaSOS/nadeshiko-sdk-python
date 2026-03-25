from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SegmentUrls")


@_attrs_define
class SegmentUrls:
    """URLs to media resources for this segment

    Attributes:
        image_url (str): URL to the subtitle image snapshot
        audio_url (str): URL to the audio clip for this segment
        video_url (str): URL to the video clip for this segment
    """

    image_url: str
    audio_url: str
    video_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_url = self.image_url

        audio_url = self.audio_url

        video_url = self.video_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "imageUrl": image_url,
                "audioUrl": audio_url,
                "videoUrl": video_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        image_url = _src.pop("imageUrl")

        audio_url = _src.pop("audioUrl")

        video_url = _src.pop("videoUrl")

        segment_urls = cls(
            image_url=image_url,
            audio_url=audio_url,
            video_url=video_url,
        )

        segment_urls.additional_properties = _src
        return segment_urls

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
