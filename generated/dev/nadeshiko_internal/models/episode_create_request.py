from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EpisodeCreateRequest")


@_attrs_define
class EpisodeCreateRequest:
    """
    Attributes:
        episode_number (int): Episode number within the media (must be unique for this media) Example: 1.
        title_en (str | Unset): English title of the episode Example: The Beginning.
        title_romaji (str | Unset): Romanized title of the episode Example: Hajimari.
        title_ja (str | Unset): Japanese title of the episode Example: 始まり.
        description (str | Unset): Episode description or synopsis Example: The hero begins their journey.
        aired_at (datetime.datetime | Unset): When the episode originally aired Example: 2024-01-15T09:00:00Z.
        length_seconds (int | Unset): Episode duration in seconds Example: 1420.
        thumbnail_url (str | Unset): URL to episode thumbnail image Example:
            https://example.com/thumbnails/episode1.jpg.
    """

    episode_number: int
    title_en: str | Unset = UNSET
    title_romaji: str | Unset = UNSET
    title_ja: str | Unset = UNSET
    description: str | Unset = UNSET
    aired_at: datetime.datetime | Unset = UNSET
    length_seconds: int | Unset = UNSET
    thumbnail_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        episode_number = self.episode_number

        title_en = self.title_en

        title_romaji = self.title_romaji

        title_ja = self.title_ja

        description = self.description

        aired_at: str | Unset = UNSET
        if not isinstance(self.aired_at, Unset):
            aired_at = self.aired_at.isoformat()

        length_seconds = self.length_seconds

        thumbnail_url = self.thumbnail_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "episodeNumber": episode_number,
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
        d = dict(src_dict)
        episode_number = d.pop("episodeNumber")

        title_en = d.pop("titleEn", UNSET)

        title_romaji = d.pop("titleRomaji", UNSET)

        title_ja = d.pop("titleJa", UNSET)

        description = d.pop("description", UNSET)

        _aired_at = d.pop("airedAt", UNSET)
        aired_at: datetime.datetime | Unset
        if isinstance(_aired_at, Unset):
            aired_at = UNSET
        else:
            aired_at = isoparse(_aired_at)

        length_seconds = d.pop("lengthSeconds", UNSET)

        thumbnail_url = d.pop("thumbnailUrl", UNSET)

        episode_create_request = cls(
            episode_number=episode_number,
            title_en=title_en,
            title_romaji=title_romaji,
            title_ja=title_ja,
            description=description,
            aired_at=aired_at,
            length_seconds=length_seconds,
            thumbnail_url=thumbnail_url,
        )

        episode_create_request.additional_properties = d
        return episode_create_request

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
