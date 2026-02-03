from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MediaInfoPath")


@_attrs_define
class MediaInfoPath:
    """URLs to media resources for a segment

    Attributes:
        path_image (str | Unset): URL to the subtitle image snapshot Example: https://example.com/media/anime/steins-
            gate/segments/1133.jpg.
        path_audio (str | Unset): URL to the audio clip for this segment Example:
            https://example.com/media/anime/steins-gate/audio/1133.mp3.
        path_video (str | Unset): URL to the video clip for this segment Example:
            https://example.com/media/anime/steins-gate/video/1133.mp4.
    """

    path_image: str | Unset = UNSET
    path_audio: str | Unset = UNSET
    path_video: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path_image = self.path_image

        path_audio = self.path_audio

        path_video = self.path_video

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path_image is not UNSET:
            field_dict["path_image"] = path_image
        if path_audio is not UNSET:
            field_dict["path_audio"] = path_audio
        if path_video is not UNSET:
            field_dict["path_video"] = path_video

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path_image = d.pop("path_image", UNSET)

        path_audio = d.pop("path_audio", UNSET)

        path_video = d.pop("path_video", UNSET)

        media_info_path = cls(
            path_image=path_image,
            path_audio=path_audio,
            path_video=path_video,
        )

        media_info_path.additional_properties = d
        return media_info_path

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
