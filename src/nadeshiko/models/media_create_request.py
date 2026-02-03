from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.media_create_request_category import MediaCreateRequestCategory
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.character_input import CharacterInput
    from ..models.list_input import ListInput


T = TypeVar("T", bound="MediaCreateRequest")


@_attrs_define
class MediaCreateRequest:
    """Request body for creating a new media entry

    Attributes:
        anilist_id (int): AniList database ID for the media Example: 7674.
        japanese_name (str): Original Japanese name of the media Example: バクマン。.
        romaji_name (str): Romaji transliteration of the media name Example: Bakuman..
        english_name (str): English translation of the media name Example: Bakuman..
        airing_format (str): Format of the media release (e.g., TV, OVA, Movie) Example: TV.
        airing_status (str): Current airing status (FINISHED, RELEASING, NOT_YET_RELEASED, CANCELLED) Example: FINISHED.
        genres (list[str]): List of genres associated with the media Example: ['Comedy', 'Drama', 'Romance', 'Slice of
            Life'].
        category (MediaCreateRequestCategory): Media category Example: ANIME.
        version (str): Version of the media-sub-splitter used Example: 6.
        studio (str): Animation studio that produced the media Example: J.C.STAFF.
        season_name (str): Season when the media aired (WINTER, SPRING, SUMMER, FALL) Example: FALL.
        season_year (int): Year when the media aired Example: 2010.
        cover_url (str | Unset): Full URL to the cover image Example:
            https://cdn.example.com/media/anime/bakuman/cover.webp.
        banner_url (str | Unset): Full URL to the banner image Example:
            https://cdn.example.com/media/anime/bakuman/banner.webp.
        start_date (datetime.datetime | Unset): Start date of the media (first airing/release) Example: 2010-10-02
            00:00:00+00:00.
        end_date (datetime.datetime | Unset): End date of the media (last airing/release) Example: 2011-04-02
            00:00:00+00:00.
        hash_salt (str | Unset): Hash salt used when generating the hash for the related media assets Example:
            ba0cbe173ed310528f16130273662a60.
        characters (list[CharacterInput] | Unset): List of characters appearing in the media with their voice actors
        lists (list[ListInput] | Unset): Lists to add this media to (e.g., series, franchise)
    """

    anilist_id: int
    japanese_name: str
    romaji_name: str
    english_name: str
    airing_format: str
    airing_status: str
    genres: list[str]
    category: MediaCreateRequestCategory
    version: str
    studio: str
    season_name: str
    season_year: int
    cover_url: str | Unset = UNSET
    banner_url: str | Unset = UNSET
    start_date: datetime.datetime | Unset = UNSET
    end_date: datetime.datetime | Unset = UNSET
    hash_salt: str | Unset = UNSET
    characters: list[CharacterInput] | Unset = UNSET
    lists: list[ListInput] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        anilist_id = self.anilist_id

        japanese_name = self.japanese_name

        romaji_name = self.romaji_name

        english_name = self.english_name

        airing_format = self.airing_format

        airing_status = self.airing_status

        genres = self.genres

        category = self.category.value

        version = self.version

        studio = self.studio

        season_name = self.season_name

        season_year = self.season_year

        cover_url = self.cover_url

        banner_url = self.banner_url

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        hash_salt = self.hash_salt

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
                "anilistId": anilist_id,
                "japaneseName": japanese_name,
                "romajiName": romaji_name,
                "englishName": english_name,
                "airingFormat": airing_format,
                "airingStatus": airing_status,
                "genres": genres,
                "category": category,
                "version": version,
                "studio": studio,
                "seasonName": season_name,
                "seasonYear": season_year,
            }
        )
        if cover_url is not UNSET:
            field_dict["coverUrl"] = cover_url
        if banner_url is not UNSET:
            field_dict["bannerUrl"] = banner_url
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if hash_salt is not UNSET:
            field_dict["hashSalt"] = hash_salt
        if characters is not UNSET:
            field_dict["characters"] = characters
        if lists is not UNSET:
            field_dict["lists"] = lists

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.character_input import CharacterInput
        from ..models.list_input import ListInput

        d = dict(src_dict)
        anilist_id = d.pop("anilistId")

        japanese_name = d.pop("japaneseName")

        romaji_name = d.pop("romajiName")

        english_name = d.pop("englishName")

        airing_format = d.pop("airingFormat")

        airing_status = d.pop("airingStatus")

        genres = cast(list[str], d.pop("genres"))

        category = MediaCreateRequestCategory(d.pop("category"))

        version = d.pop("version")

        studio = d.pop("studio")

        season_name = d.pop("seasonName")

        season_year = d.pop("seasonYear")

        cover_url = d.pop("coverUrl", UNSET)

        banner_url = d.pop("bannerUrl", UNSET)

        _start_date = d.pop("startDate", UNSET)
        start_date: datetime.datetime | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _end_date = d.pop("endDate", UNSET)
        end_date: datetime.datetime | Unset
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        hash_salt = d.pop("hashSalt", UNSET)

        _characters = d.pop("characters", UNSET)
        characters: list[CharacterInput] | Unset = UNSET
        if _characters is not UNSET:
            characters = []
            for characters_item_data in _characters:
                characters_item = CharacterInput.from_dict(characters_item_data)

                characters.append(characters_item)

        _lists = d.pop("lists", UNSET)
        lists: list[ListInput] | Unset = UNSET
        if _lists is not UNSET:
            lists = []
            for lists_item_data in _lists:
                lists_item = ListInput.from_dict(lists_item_data)

                lists.append(lists_item)

        media_create_request = cls(
            anilist_id=anilist_id,
            japanese_name=japanese_name,
            romaji_name=romaji_name,
            english_name=english_name,
            airing_format=airing_format,
            airing_status=airing_status,
            genres=genres,
            category=category,
            version=version,
            studio=studio,
            season_name=season_name,
            season_year=season_year,
            cover_url=cover_url,
            banner_url=banner_url,
            start_date=start_date,
            end_date=end_date,
            hash_salt=hash_salt,
            characters=characters,
            lists=lists,
        )

        media_create_request.additional_properties = d
        return media_create_request

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
