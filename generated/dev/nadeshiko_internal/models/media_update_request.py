from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.media_update_request_category import MediaUpdateRequestCategory
from ..models.media_update_request_storage import MediaUpdateRequestStorage
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.character_input import CharacterInput
    from ..models.external_id import ExternalId
    from ..models.list_input import ListInput


T = TypeVar("T", bound="MediaUpdateRequest")


@_attrs_define
class MediaUpdateRequest:
    """Request body for updating an existing media entry (all fields optional)

    Attributes:
        external_ids (ExternalId | Unset): Map of external IDs keyed by source. Only sources with values are included.
        name_ja (str | Unset): Original Japanese name of the media Example: バクマン。.
        name_romaji (str | Unset): Romaji transliteration of the media name Example: Bakuman..
        name_en (str | Unset): English name of the media Example: Bakuman..
        airing_format (str | Unset): Format of the media release (e.g., TV, OVA, Movie) Example: TV.
        airing_status (str | Unset): Current airing status (FINISHED, RELEASING, NOT_YET_RELEASED, CANCELLED) Example:
            FINISHED.
        genres (list[str] | Unset): List of genres associated with the media Example: ['Comedy', 'Drama', 'Romance',
            'Slice of Life'].
        storage (MediaUpdateRequestStorage | Unset): Storage backend for media assets Default:
            MediaUpdateRequestStorage.R2. Example: R2.
        start_date (datetime.date | Unset): Start date of the media (first airing/release) Example: 2010-10-02.
        end_date (datetime.date | Unset): End date of the media (last airing/release) Example: 2011-04-02.
        category (MediaUpdateRequestCategory | Unset): Media category Example: ANIME.
        version (str | Unset): Version of the media-sub-splitter used Example: 6.
        hash_salt (str | Unset): Hash salt used when generating the hash for the related media assets Example:
            ba0cbe173ed310528f16130273662a60.
        studio (str | Unset): Animation studio that produced the media Example: J.C.STAFF.
        season_name (str | Unset): Airing season label for the media Example: FALL.
        season_year (int | Unset): Airing year for the media Example: 2010.
        characters (list[CharacterInput] | Unset): List of characters appearing in the media with their voice actors
        lists (list[ListInput] | Unset): Lists to add this media to (e.g., series, franchise)
        segment_count (int | Unset): Total number of subtitle segments available Example: 1234.
    """

    external_ids: ExternalId | Unset = UNSET
    name_ja: str | Unset = UNSET
    name_romaji: str | Unset = UNSET
    name_en: str | Unset = UNSET
    airing_format: str | Unset = UNSET
    airing_status: str | Unset = UNSET
    genres: list[str] | Unset = UNSET
    storage: MediaUpdateRequestStorage | Unset = MediaUpdateRequestStorage.R2
    start_date: datetime.date | Unset = UNSET
    end_date: datetime.date | Unset = UNSET
    category: MediaUpdateRequestCategory | Unset = UNSET
    version: str | Unset = UNSET
    hash_salt: str | Unset = UNSET
    studio: str | Unset = UNSET
    season_name: str | Unset = UNSET
    season_year: int | Unset = UNSET
    characters: list[CharacterInput] | Unset = UNSET
    lists: list[ListInput] | Unset = UNSET
    segment_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_ids: dict[str, Any] | Unset = UNSET
        if not isinstance(self.external_ids, Unset):
            external_ids = self.external_ids.to_dict()

        name_ja = self.name_ja

        name_romaji = self.name_romaji

        name_en = self.name_en

        airing_format = self.airing_format

        airing_status = self.airing_status

        genres: list[str] | Unset = UNSET
        if not isinstance(self.genres, Unset):
            genres = self.genres

        storage: str | Unset = UNSET
        if not isinstance(self.storage, Unset):
            storage = self.storage.value

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        version = self.version

        hash_salt = self.hash_salt

        studio = self.studio

        season_name = self.season_name

        season_year = self.season_year

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

        segment_count = self.segment_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if external_ids is not UNSET:
            field_dict["externalIds"] = external_ids
        if name_ja is not UNSET:
            field_dict["nameJa"] = name_ja
        if name_romaji is not UNSET:
            field_dict["nameRomaji"] = name_romaji
        if name_en is not UNSET:
            field_dict["nameEn"] = name_en
        if airing_format is not UNSET:
            field_dict["airingFormat"] = airing_format
        if airing_status is not UNSET:
            field_dict["airingStatus"] = airing_status
        if genres is not UNSET:
            field_dict["genres"] = genres
        if storage is not UNSET:
            field_dict["storage"] = storage
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if category is not UNSET:
            field_dict["category"] = category
        if version is not UNSET:
            field_dict["version"] = version
        if hash_salt is not UNSET:
            field_dict["hashSalt"] = hash_salt
        if studio is not UNSET:
            field_dict["studio"] = studio
        if season_name is not UNSET:
            field_dict["seasonName"] = season_name
        if season_year is not UNSET:
            field_dict["seasonYear"] = season_year
        if characters is not UNSET:
            field_dict["characters"] = characters
        if lists is not UNSET:
            field_dict["lists"] = lists
        if segment_count is not UNSET:
            field_dict["segmentCount"] = segment_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.character_input import CharacterInput
        from ..models.external_id import ExternalId
        from ..models.list_input import ListInput

        d = dict(src_dict)
        _external_ids = d.pop("externalIds", UNSET)
        external_ids: ExternalId | Unset
        if isinstance(_external_ids, Unset):
            external_ids = UNSET
        else:
            external_ids = ExternalId.from_dict(_external_ids)

        name_ja = d.pop("nameJa", UNSET)

        name_romaji = d.pop("nameRomaji", UNSET)

        name_en = d.pop("nameEn", UNSET)

        airing_format = d.pop("airingFormat", UNSET)

        airing_status = d.pop("airingStatus", UNSET)

        genres = cast(list[str], d.pop("genres", UNSET))

        _storage = d.pop("storage", UNSET)
        storage: MediaUpdateRequestStorage | Unset
        if isinstance(_storage, Unset):
            storage = UNSET
        else:
            storage = MediaUpdateRequestStorage(_storage)

        _start_date = d.pop("startDate", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()

        _end_date = d.pop("endDate", UNSET)
        end_date: datetime.date | Unset
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date).date()

        _category = d.pop("category", UNSET)
        category: MediaUpdateRequestCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = MediaUpdateRequestCategory(_category)

        version = d.pop("version", UNSET)

        hash_salt = d.pop("hashSalt", UNSET)

        studio = d.pop("studio", UNSET)

        season_name = d.pop("seasonName", UNSET)

        season_year = d.pop("seasonYear", UNSET)

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

        segment_count = d.pop("segmentCount", UNSET)

        media_update_request = cls(
            external_ids=external_ids,
            name_ja=name_ja,
            name_romaji=name_romaji,
            name_en=name_en,
            airing_format=airing_format,
            airing_status=airing_status,
            genres=genres,
            storage=storage,
            start_date=start_date,
            end_date=end_date,
            category=category,
            version=version,
            hash_salt=hash_salt,
            studio=studio,
            season_name=season_name,
            season_year=season_year,
            characters=characters,
            lists=lists,
            segment_count=segment_count,
        )

        media_update_request.additional_properties = d
        return media_update_request

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
