from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.report_target_episode_type import ReportTargetEpisodeType

T = TypeVar("T", bound="ReportTargetEpisode")


@_attrs_define
class ReportTargetEpisode:
    """
    Attributes:
        type_ (ReportTargetEpisodeType): Report target type Example: EPISODE.
        media_id (str): publicId of the media this report targets Example: V1StGXR8_Z5d.
        episode_number (int): Episode number this report targets Example: 5.
    """

    type_: ReportTargetEpisodeType
    media_id: str
    episode_number: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        media_id = self.media_id

        episode_number = self.episode_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "mediaId": media_id,
                "episodeNumber": episode_number,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        type_ = ReportTargetEpisodeType(_src.pop("type"))

        media_id = _src.pop("mediaId")

        episode_number = _src.pop("episodeNumber")

        report_target_episode = cls(
            type_=type_,
            media_id=media_id,
            episode_number=episode_number,
        )

        report_target_episode.additional_properties = _src
        return report_target_episode

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
