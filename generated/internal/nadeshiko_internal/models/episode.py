from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Episode")


@_attrs_define
class Episode:
    """
    Attributes:
        media_id (int): ID of the media this episode belongs to Example: 7674.
        episode_number (int): Episode number within the media Example: 1.
        segment_count (int): Number of segments in this episode Example: 450.
        title_en (None | str | Unset): English title of the episode Example: The Beginning.
        title_romaji (None | str | Unset): Romanized title of the episode Example: Hajimari.
        title_ja (None | str | Unset): Japanese title of the episode Example: 始まり.
        description (None | str | Unset): Episode description or synopsis Example: The hero begins their journey.
        aired_at (datetime.datetime | None | Unset): When the episode originally aired Example: 2024-01-15T09:00:00Z.
        length_seconds (int | None | Unset): Episode duration in seconds Example: 1420.
        thumbnail_url (None | str | Unset): URL to episode thumbnail image Example:
            https://example.com/thumbnails/episode1.jpg.
    """

    media_id: int
    episode_number: int
    segment_count: int
    title_en: None | str | Unset = UNSET
    title_romaji: None | str | Unset = UNSET
    title_ja: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    aired_at: datetime.datetime | None | Unset = UNSET
    length_seconds: int | None | Unset = UNSET
    thumbnail_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media_id = self.media_id

        episode_number = self.episode_number

        segment_count = self.segment_count

        title_en: None | str | Unset
        if isinstance(self.title_en, Unset):
            title_en = UNSET
        else:
            title_en = self.title_en

        title_romaji: None | str | Unset
        if isinstance(self.title_romaji, Unset):
            title_romaji = UNSET
        else:
            title_romaji = self.title_romaji

        title_ja: None | str | Unset
        if isinstance(self.title_ja, Unset):
            title_ja = UNSET
        else:
            title_ja = self.title_ja

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        aired_at: None | str | Unset
        if isinstance(self.aired_at, Unset):
            aired_at = UNSET
        elif isinstance(self.aired_at, datetime.datetime):
            aired_at = self.aired_at.isoformat()
        else:
            aired_at = self.aired_at

        length_seconds: int | None | Unset
        if isinstance(self.length_seconds, Unset):
            length_seconds = UNSET
        else:
            length_seconds = self.length_seconds

        thumbnail_url: None | str | Unset
        if isinstance(self.thumbnail_url, Unset):
            thumbnail_url = UNSET
        else:
            thumbnail_url = self.thumbnail_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mediaId": media_id,
                "episodeNumber": episode_number,
                "segmentCount": segment_count,
            }
        )
        if title_en is not UNSET:
            field_dict["titleEn"] = title_en
        if title_romaji is not UNSET:
            field_dict["titleRomaji"] = title_romaji
        if title_ja is not UNSET:
            field_dict["titleJa"] = title_ja
        if description is not UNSET:
            field_dict["description"] = description
        if aired_at is not UNSET:
            field_dict["airedAt"] = aired_at
        if length_seconds is not UNSET:
            field_dict["lengthSeconds"] = length_seconds
        if thumbnail_url is not UNSET:
            field_dict["thumbnailUrl"] = thumbnail_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        media_id = _src.pop("mediaId")

        episode_number = _src.pop("episodeNumber")

        segment_count = _src.pop("segmentCount")

        def _parse_title_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title_en = _parse_title_en(_src.pop("titleEn", UNSET))

        def _parse_title_romaji(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title_romaji = _parse_title_romaji(_src.pop("titleRomaji", UNSET))

        def _parse_title_ja(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title_ja = _parse_title_ja(_src.pop("titleJa", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(_src.pop("description", UNSET))

        def _parse_aired_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                aired_at_type_0 = isoparse(data)

                return aired_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        aired_at = _parse_aired_at(_src.pop("airedAt", UNSET))

        def _parse_length_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        length_seconds = _parse_length_seconds(_src.pop("lengthSeconds", UNSET))

        def _parse_thumbnail_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail_url = _parse_thumbnail_url(_src.pop("thumbnailUrl", UNSET))

        episode = cls(
            media_id=media_id,
            episode_number=episode_number,
            segment_count=segment_count,
            title_en=title_en,
            title_romaji=title_romaji,
            title_ja=title_ja,
            description=description,
            aired_at=aired_at,
            length_seconds=length_seconds,
            thumbnail_url=thumbnail_url,
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
