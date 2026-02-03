from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MediaInfoData")


@_attrs_define
class MediaInfoData:
    """Complete information about a media/anime entry

    Attributes:
        id (int): Unique identifier for the media Example: 110316.
        anilist_id (int | None | Unset): AniList database ID for the media Example: 21459.
        tmdb_id (int | None | Unset): TMDB (The Movie Database) ID for the media Example: 63726.
        category (int | Unset): Media category (1=Anime, 2=Unknown, 3=J-Drama, 4=Audiobook) Example: 1.
        created_at (datetime.datetime | Unset): Timestamp when the media entry was created in the database Example:
            2024-01-15 10:30:00+00:00.
        updated_at (int | Unset): Timestamp when the media entry was last updated Example: 1705769100.
        romaji_name (str | Unset): Romaji transliteration of the media name Example: Steins;Gate.
        english_name (str | Unset): English translation of the media name Example: Steins;Gate.
        japanese_name (str | Unset): Original Japanese name of the media Example: シュタインズ・ゲート.
        airing_format (str | Unset): Format of the media release (e.g., TV, OVA, Movie) Example: TV.
        airing_status (str | Unset): Current airing status (FINISHED, RELEASING) Example: FINISHED.
        start_date (datetime.datetime | Unset): Start date of the media Example: 2011-04-06 00:00:00+00:00.
        end_date (datetime.datetime | None | Unset): End date of the media (null if unknown) Example: 2011-09-14
            00:00:00+00:00.
        folder_media_name (str | Unset): Folder name used for storing media files Example: steins-gate.
        genres (list[str] | Unset): List of genres associated with the media Example: ['Sci-Fi', 'Thriller', 'Romance'].
        cover (str | Unset): URL to the cover image Example: https://example.com/media/anime/steins-gate/cover.jpg.
        banner (str | Unset): URL to the banner image Example: https://example.com/media/anime/steins-gate/banner.jpg.
        version (str | Unset): Version identifier for the media entry Example: v1.0.
        num_segments (int | Unset): Total number of subtitle segments available Example: 18542.
        num_seasons (int | Unset): Total number of seasons available Example: 1.
        num_episodes (int | Unset): Total number of episodes available Example: 24.
    """

    id: int
    anilist_id: int | None | Unset = UNSET
    tmdb_id: int | None | Unset = UNSET
    category: int | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: int | Unset = UNSET
    romaji_name: str | Unset = UNSET
    english_name: str | Unset = UNSET
    japanese_name: str | Unset = UNSET
    airing_format: str | Unset = UNSET
    airing_status: str | Unset = UNSET
    start_date: datetime.datetime | Unset = UNSET
    end_date: datetime.datetime | None | Unset = UNSET
    folder_media_name: str | Unset = UNSET
    genres: list[str] | Unset = UNSET
    cover: str | Unset = UNSET
    banner: str | Unset = UNSET
    version: str | Unset = UNSET
    num_segments: int | Unset = UNSET
    num_seasons: int | Unset = UNSET
    num_episodes: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        anilist_id: int | None | Unset
        if isinstance(self.anilist_id, Unset):
            anilist_id = UNSET
        else:
            anilist_id = self.anilist_id

        tmdb_id: int | None | Unset
        if isinstance(self.tmdb_id, Unset):
            tmdb_id = UNSET
        else:
            tmdb_id = self.tmdb_id

        category = self.category

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at = self.updated_at

        romaji_name = self.romaji_name

        english_name = self.english_name

        japanese_name = self.japanese_name

        airing_format = self.airing_format

        airing_status = self.airing_status

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        folder_media_name = self.folder_media_name

        genres: list[str] | Unset = UNSET
        if not isinstance(self.genres, Unset):
            genres = self.genres

        cover = self.cover

        banner = self.banner

        version = self.version

        num_segments = self.num_segments

        num_seasons = self.num_seasons

        num_episodes = self.num_episodes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if anilist_id is not UNSET:
            field_dict["anilist_id"] = anilist_id
        if tmdb_id is not UNSET:
            field_dict["tmdb_id"] = tmdb_id
        if category is not UNSET:
            field_dict["category"] = category
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if romaji_name is not UNSET:
            field_dict["romaji_name"] = romaji_name
        if english_name is not UNSET:
            field_dict["english_name"] = english_name
        if japanese_name is not UNSET:
            field_dict["japanese_name"] = japanese_name
        if airing_format is not UNSET:
            field_dict["airing_format"] = airing_format
        if airing_status is not UNSET:
            field_dict["airing_status"] = airing_status
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if folder_media_name is not UNSET:
            field_dict["folder_media_name"] = folder_media_name
        if genres is not UNSET:
            field_dict["genres"] = genres
        if cover is not UNSET:
            field_dict["cover"] = cover
        if banner is not UNSET:
            field_dict["banner"] = banner
        if version is not UNSET:
            field_dict["version"] = version
        if num_segments is not UNSET:
            field_dict["num_segments"] = num_segments
        if num_seasons is not UNSET:
            field_dict["num_seasons"] = num_seasons
        if num_episodes is not UNSET:
            field_dict["num_episodes"] = num_episodes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_anilist_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        anilist_id = _parse_anilist_id(d.pop("anilist_id", UNSET))

        def _parse_tmdb_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tmdb_id = _parse_tmdb_id(d.pop("tmdb_id", UNSET))

        category = d.pop("category", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        updated_at = d.pop("updated_at", UNSET)

        romaji_name = d.pop("romaji_name", UNSET)

        english_name = d.pop("english_name", UNSET)

        japanese_name = d.pop("japanese_name", UNSET)

        airing_format = d.pop("airing_format", UNSET)

        airing_status = d.pop("airing_status", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.datetime | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        def _parse_end_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data)

                return end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))

        folder_media_name = d.pop("folder_media_name", UNSET)

        genres = cast(list[str], d.pop("genres", UNSET))

        cover = d.pop("cover", UNSET)

        banner = d.pop("banner", UNSET)

        version = d.pop("version", UNSET)

        num_segments = d.pop("num_segments", UNSET)

        num_seasons = d.pop("num_seasons", UNSET)

        num_episodes = d.pop("num_episodes", UNSET)

        media_info_data = cls(
            id=id,
            anilist_id=anilist_id,
            tmdb_id=tmdb_id,
            category=category,
            created_at=created_at,
            updated_at=updated_at,
            romaji_name=romaji_name,
            english_name=english_name,
            japanese_name=japanese_name,
            airing_format=airing_format,
            airing_status=airing_status,
            start_date=start_date,
            end_date=end_date,
            folder_media_name=folder_media_name,
            genres=genres,
            cover=cover,
            banner=banner,
            version=version,
            num_segments=num_segments,
            num_seasons=num_seasons,
            num_episodes=num_episodes,
        )

        media_info_data.additional_properties = d
        return media_info_data

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
