from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.media_create_request_category import MediaCreateRequestCategory
from ..models.media_create_request_storage import MediaCreateRequestStorage
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.character_input import CharacterInput
  from ..models.list_input import ListInput





T = TypeVar("T", bound="MediaCreateRequest")



@_attrs_define
class MediaCreateRequest:
    """ Request body for creating a new media entry

        Attributes:
            anilist_id (int): AniList database ID for the media Example: 7674.
            japanese_name (str): Original Japanese name of the media Example: バクマン。.
            romaji_name (str): Romaji transliteration of the media name Example: Bakuman..
            english_name (str): English translation of the media name Example: Bakuman..
            airing_format (str): Format of the media release (e.g., TV, OVA, Movie) Example: TV.
            airing_status (str): Current airing status (FINISHED, RELEASING, NOT_YET_RELEASED, CANCELLED) Example: FINISHED.
            genres (list[str]): List of genres associated with the media Example: ['Comedy', 'Drama', 'Romance', 'Slice of
                Life'].
            storage (MediaCreateRequestStorage): Storage backend for media assets Default: MediaCreateRequestStorage.R2.
                Example: r2.
            start_date (datetime.date): Start date of the media (first airing/release) Example: 2010-10-02.
            category (MediaCreateRequestCategory): Media category Example: ANIME.
            version (str): Version of the media-sub-splitter used Example: 6.
            hash_salt (str): Hash salt used when generating the hash for the related media assets Example:
                ba0cbe173ed310528f16130273662a60.
            studio (str): Animation studio that produced the media Example: J.C.STAFF.
            season_name (str): Season when the media aired (WINTER, SPRING, SUMMER, FALL) Example: FALL.
            season_year (int): Year when the media aired Example: 2010.
            end_date (datetime.date | Unset): End date of the media (last airing/release) Example: 2011-04-02.
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
    start_date: datetime.date
    category: MediaCreateRequestCategory
    version: str
    hash_salt: str
    studio: str
    season_name: str
    season_year: int
    storage: MediaCreateRequestStorage = MediaCreateRequestStorage.R2
    end_date: datetime.date | Unset = UNSET
    characters: list[CharacterInput] | Unset = UNSET
    lists: list[ListInput] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.character_input import CharacterInput
        from ..models.list_input import ListInput
        anilist_id = self.anilist_id

        japanese_name = self.japanese_name

        romaji_name = self.romaji_name

        english_name = self.english_name

        airing_format = self.airing_format

        airing_status = self.airing_status

        genres = self.genres



        storage = self.storage.value

        start_date = self.start_date.isoformat()

        category = self.category.value

        version = self.version

        hash_salt = self.hash_salt

        studio = self.studio

        season_name = self.season_name

        season_year = self.season_year

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

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
        field_dict.update({
            "anilistId": anilist_id,
            "japaneseName": japanese_name,
            "romajiName": romaji_name,
            "englishName": english_name,
            "airingFormat": airing_format,
            "airingStatus": airing_status,
            "genres": genres,
            "storage": storage,
            "startDate": start_date,
            "category": category,
            "version": version,
            "hashSalt": hash_salt,
            "studio": studio,
            "seasonName": season_name,
            "seasonYear": season_year,
        })
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
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


        storage = MediaCreateRequestStorage(d.pop("storage"))




        start_date = isoparse(d.pop("startDate")).date()




        category = MediaCreateRequestCategory(d.pop("category"))




        version = d.pop("version")

        hash_salt = d.pop("hashSalt")

        studio = d.pop("studio")

        season_name = d.pop("seasonName")

        season_year = d.pop("seasonYear")

        _end_date = d.pop("endDate", UNSET)
        end_date: datetime.date | Unset
        if isinstance(_end_date,  Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date).date()




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
            storage=storage,
            start_date=start_date,
            category=category,
            version=version,
            hash_salt=hash_salt,
            studio=studio,
            season_name=season_name,
            season_year=season_year,
            end_date=end_date,
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
