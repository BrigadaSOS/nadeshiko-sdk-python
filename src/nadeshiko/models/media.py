from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.media_category import MediaCategory
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_ import List
    from ..models.media_character import MediaCharacter


T = TypeVar("T", bound="Media")


@_attrs_define
class Media:
    """Media entry with full metadata

    Attributes:
        id (int): Unique identifier for the media Example: 7674.
        anilist_id (int): AniList database ID for the media Example: 7674.
        japanese_name (str): Original Japanese name of the media Example: バクマン。.
        romaji_name (str): Romaji transliteration of the media name Example: Bakuman..
        english_name (str): English translation of the media name Example: Bakuman..
        airing_format (str): Format of the media release (e.g., TV, OVA, Movie) Example: TV.
        airing_status (str): Current airing status (FINISHED, RELEASING, NOT_YET_RELEASED, CANCELLED) Example: FINISHED.
        genres (list[str]): List of genres associated with the media Example: ['Comedy', 'Drama', 'Romance', 'Slice of
            Life'].
        cover_url (str): Full URL to the cover image Example: https://cdn.example.com/media/anime/bakuman/cover.webp.
        banner_url (str): Full URL to the banner image Example: https://cdn.example.com/media/anime/bakuman/banner.webp.
        start_date (datetime.datetime): Start date of the media (first airing/release) Example: 2010-10-02
            00:00:00+00:00.
        category (MediaCategory): Media category Example: ANIME.
        version (str): Version identifier for the media entry Example: 6.
        studio (str): Animation studio that produced the media Example: J.C.STAFF.
        season_name (str): Season when the media aired (WINTER, SPRING, SUMMER, FALL) Example: FALL.
        season_year (int): Year when the media aired Example: 2010.
        end_date (datetime.datetime | None | Unset): End date of the media (last airing/release) Example: 2011-04-02
            00:00:00+00:00.
        num_segments (int | Unset): Total number of subtitle segments available
        num_episodes (int | Unset): Total number of episodes available Example: 25.
        characters (list[MediaCharacter] | Unset): Characters appearing in the media with their voice actors
        lists (list[List] | Unset): Lists that contain this media
    """

    id: int
    anilist_id: int
    japanese_name: str
    romaji_name: str
    english_name: str
    airing_format: str
    airing_status: str
    genres: list[str]
    cover_url: str
    banner_url: str
    start_date: datetime.datetime
    category: MediaCategory
    version: str
    studio: str
    season_name: str
    season_year: int
    end_date: datetime.datetime | None | Unset = UNSET
    num_segments: int | Unset = UNSET
    num_episodes: int | Unset = UNSET
    characters: list[MediaCharacter] | Unset = UNSET
    lists: list[List] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        anilist_id = self.anilist_id

        japanese_name = self.japanese_name

        romaji_name = self.romaji_name

        english_name = self.english_name

        airing_format = self.airing_format

        airing_status = self.airing_status

        genres = self.genres

        cover_url = self.cover_url

        banner_url = self.banner_url

        start_date = self.start_date.isoformat()

        category = self.category.value

        version = self.version

        studio = self.studio

        season_name = self.season_name

        season_year = self.season_year

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        num_segments = self.num_segments

        num_episodes = self.num_episodes

        characters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.characters, Unset):
            characters = []
            for characters_item_data in self.characters:
                characters_item = characters_item_data.to_dict()
                characters.append(characters_item)

        lists: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lists, Unset):
            lists = []
            for lists_item_data in self.lists:
                lists_item = lists_item_data.to_dict()
                lists.append(lists_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "anilistId": anilist_id,
                "japaneseName": japanese_name,
                "romajiName": romaji_name,
                "englishName": english_name,
                "airingFormat": airing_format,
                "airingStatus": airing_status,
                "genres": genres,
                "coverUrl": cover_url,
                "bannerUrl": banner_url,
                "startDate": start_date,
                "category": category,
                "version": version,
                "studio": studio,
                "seasonName": season_name,
                "seasonYear": season_year,
            }
        )
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if num_segments is not UNSET:
            field_dict["numSegments"] = num_segments
        if num_episodes is not UNSET:
            field_dict["numEpisodes"] = num_episodes
        if characters is not UNSET:
            field_dict["characters"] = characters
        if lists is not UNSET:
            field_dict["lists"] = lists

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_ import List
        from ..models.media_character import MediaCharacter

        d = dict(src_dict)
        id = d.pop("id")

        anilist_id = d.pop("anilistId")

        japanese_name = d.pop("japaneseName")

        romaji_name = d.pop("romajiName")

        english_name = d.pop("englishName")

        airing_format = d.pop("airingFormat")

        airing_status = d.pop("airingStatus")

        genres = cast(list[str], d.pop("genres"))

        cover_url = d.pop("coverUrl")

        banner_url = d.pop("bannerUrl")

        start_date = isoparse(d.pop("startDate"))

        category = MediaCategory(d.pop("category"))

        version = d.pop("version")

        studio = d.pop("studio")

        season_name = d.pop("seasonName")

        season_year = d.pop("seasonYear")

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

        end_date = _parse_end_date(d.pop("endDate", UNSET))

        num_segments = d.pop("numSegments", UNSET)

        num_episodes = d.pop("numEpisodes", UNSET)

        _characters = d.pop("characters", UNSET)
        characters: list[MediaCharacter] | Unset = UNSET
        if _characters is not UNSET:
            characters = []
            for characters_item_data in _characters:
                characters_item = MediaCharacter.from_dict(characters_item_data)

                characters.append(characters_item)

        _lists = d.pop("lists", UNSET)
        lists: list[List] | Unset = UNSET
        if _lists is not UNSET:
            lists = []
            for lists_item_data in _lists:
                lists_item = List.from_dict(lists_item_data)

                lists.append(lists_item)

        media = cls(
            id=id,
            anilist_id=anilist_id,
            japanese_name=japanese_name,
            romaji_name=romaji_name,
            english_name=english_name,
            airing_format=airing_format,
            airing_status=airing_status,
            genres=genres,
            cover_url=cover_url,
            banner_url=banner_url,
            start_date=start_date,
            category=category,
            version=version,
            studio=studio,
            season_name=season_name,
            season_year=season_year,
            end_date=end_date,
            num_segments=num_segments,
            num_episodes=num_episodes,
            characters=characters,
            lists=lists,
        )

        media.additional_properties = d
        return media

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
