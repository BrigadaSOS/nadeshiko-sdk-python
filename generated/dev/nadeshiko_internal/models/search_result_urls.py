from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchResultUrls")


@_attrs_define
class SearchResultUrls:
    """URLs to media resources for a segment

    Attributes:
        image_url (str | Unset): URL to the subtitle image snapshot Example: https://example.com/media/anime/steins-
            gate/segments/1133.jpg.
        audio_url (str | Unset): URL to the audio clip for this segment Example: https://example.com/media/anime/steins-
            gate/audio/1133.mp3.
        video_url (str | Unset): URL to the video clip for this segment Example: https://example.com/media/anime/steins-
            gate/video/1133.mp4.
    """

    image_url: str | Unset = UNSET
    audio_url: str | Unset = UNSET
    video_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_url = self.image_url

        audio_url = self.audio_url

        video_url = self.video_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if audio_url is not UNSET:
            field_dict["audioUrl"] = audio_url
        if video_url is not UNSET:
            field_dict["videoUrl"] = video_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image_url = d.pop("imageUrl", UNSET)

        audio_url = d.pop("audioUrl", UNSET)

        video_url = d.pop("videoUrl", UNSET)

        search_result_urls = cls(
            image_url=image_url,
            audio_url=audio_url,
            video_url=video_url,
        )

        search_result_urls.additional_properties = d
        return search_result_urls

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
