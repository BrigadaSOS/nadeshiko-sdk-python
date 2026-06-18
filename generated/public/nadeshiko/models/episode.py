from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Episode")


@_attrs_define
class Episode:
    """Episode entry with metadata and dialogue segment count

    Attributes:
        media_public_id (str): Media public ID this episode belongs to Example: V1StGXR8_Z5d.
        episode_number (int): Episode number within the media (0 for movies/specials) Example: 1.
        title_en (None | str): English title of the episode Example: The Beginning.
        title_romaji (None | str): Romanized title of the episode Example: Hajimari.
        title_ja (None | str): Japanese title of the episode Example: 始まり.
        description (None | str): Episode description or synopsis Example: The hero begins their journey.
        aired_at (datetime.datetime | None): When the episode originally aired Example: 2024-01-15T09:00:00Z.
        length_seconds (int | None): Episode duration in seconds Example: 1420.
        thumbnail_url (None | str): URL to episode thumbnail image Example: https://example.com/thumbnails/episode1.jpg.
        external_video_id (None | str): External source video identifier for this episode Example: ZJFMStE1Tjo.
        segment_count (int): Number of segments in this episode Example: 450.
    """

    media_public_id: str
    episode_number: int
    title_en: None | str
    title_romaji: None | str
    title_ja: None | str
    description: None | str
    aired_at: datetime.datetime | None
    length_seconds: int | None
    thumbnail_url: None | str
    external_video_id: None | str
    segment_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media_public_id = self.media_public_id

        episode_number = self.episode_number

        title_en: None | str
        title_en = self.title_en

        title_romaji: None | str
        title_romaji = self.title_romaji

        title_ja: None | str
        title_ja = self.title_ja

        description: None | str
        description = self.description

        aired_at: None | str
        if isinstance(self.aired_at, datetime.datetime):
            aired_at = self.aired_at.isoformat()
        else:
            aired_at = self.aired_at

        length_seconds: int | None
        length_seconds = self.length_seconds

        thumbnail_url: None | str
        thumbnail_url = self.thumbnail_url

        external_video_id: None | str
        external_video_id = self.external_video_id

        segment_count = self.segment_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mediaPublicId": media_public_id,
                "episodeNumber": episode_number,
                "titleEn": title_en,
                "titleRomaji": title_romaji,
                "titleJa": title_ja,
                "description": description,
                "airedAt": aired_at,
                "lengthSeconds": length_seconds,
                "thumbnailUrl": thumbnail_url,
                "externalVideoId": external_video_id,
                "segmentCount": segment_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        media_public_id = _src.pop("mediaPublicId")

        episode_number = _src.pop("episodeNumber")

        def _parse_title_en(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title_en = _parse_title_en(_src.pop("titleEn"))

        def _parse_title_romaji(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title_romaji = _parse_title_romaji(_src.pop("titleRomaji"))

        def _parse_title_ja(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title_ja = _parse_title_ja(_src.pop("titleJa"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(_src.pop("description"))

        def _parse_aired_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                aired_at_type_0 = datetime.datetime.fromisoformat(data)

                return aired_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        aired_at = _parse_aired_at(_src.pop("airedAt"))

        def _parse_length_seconds(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        length_seconds = _parse_length_seconds(_src.pop("lengthSeconds"))

        def _parse_thumbnail_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        thumbnail_url = _parse_thumbnail_url(_src.pop("thumbnailUrl"))

        def _parse_external_video_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        external_video_id = _parse_external_video_id(_src.pop("externalVideoId"))

        segment_count = _src.pop("segmentCount")

        episode = cls(
            media_public_id=media_public_id,
            episode_number=episode_number,
            title_en=title_en,
            title_romaji=title_romaji,
            title_ja=title_ja,
            description=description,
            aired_at=aired_at,
            length_seconds=length_seconds,
            thumbnail_url=thumbnail_url,
            external_video_id=external_video_id,
            segment_count=segment_count,
        )

        episode.additional_properties = _src
        return episode

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
