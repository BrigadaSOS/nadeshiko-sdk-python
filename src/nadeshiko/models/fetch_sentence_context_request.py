from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FetchSentenceContextRequest")


@_attrs_define
class FetchSentenceContextRequest:
    """
    Attributes:
        media_id (int): Media ID Example: 110316.
        season (int): Season number Example: 1.
        episode (int): Episode number Example: 5.
        segment_position (int): Segment position in the episode Example: 1133.
        limit (int | Unset): Number of surrounding segments to retrieve Default: 5. Example: 5.
    """

    media_id: int
    season: int
    episode: int
    segment_position: int
    limit: int | Unset = 5
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media_id = self.media_id

        season = self.season

        episode = self.episode

        segment_position = self.segment_position

        limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "media_id": media_id,
                "season": season,
                "episode": episode,
                "segment_position": segment_position,
            }
        )
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        media_id = d.pop("media_id")

        season = d.pop("season")

        episode = d.pop("episode")

        segment_position = d.pop("segment_position")

        limit = d.pop("limit", UNSET)

        fetch_sentence_context_request = cls(
            media_id=media_id,
            season=season,
            episode=episode,
            segment_position=segment_position,
            limit=limit,
        )

        fetch_sentence_context_request.additional_properties = d
        return fetch_sentence_context_request

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
