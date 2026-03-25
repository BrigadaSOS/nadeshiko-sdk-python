from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.media_create_request_category import MediaCreateRequestCategory
from ..models.media_create_request_storage import MediaCreateRequestStorage
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.character_input import CharacterInput
    from ..models.external_id import ExternalId


T = TypeVar("T", bound="MediaCreateRequest")


@_attrs_define
class MediaCreateRequest:
    """Request body for creating a new media entry

    Attributes:
        name_ja (str): Original Japanese name of the media Example: バクマン。.
        name_romaji (str): Romaji transliteration of the media name Example: Bakuman..
        name_en (str): English name of the media Example: Bakuman..
        airing_format (str): Format of the media release (e.g., TV, OVA, Movie) Example: TV.
        airing_status (str): Current airing status (FINISHED, RELEASING, NOT_YET_RELEASED, CANCELLED) Example: FINISHED.
        genres (list[str]): List of genres associated with the media Example: ['Comedy', 'Drama', 'Romance', 'Slice of
            Life'].
        storage (MediaCreateRequestStorage): Storage backend for media assets Default: MediaCreateRequestStorage.R2.
            Example: R2.
        start_date (datetime.date): Start date of the media (first airing/release) Example: 2010-10-02.
        category (MediaCreateRequestCategory): Media category Example: ANIME.
        version (str): Version of the media-sub-splitter used Example: 6.
        hash_salt (str): Hash salt used when generating the hash for the related media assets Example:
            ba0cbe173ed310528f16130273662a60.
        season_name (str): Airing season label for the media Example: FALL.
        season_year (int): Airing year for the media Example: 2010.
        external_ids (ExternalId | Unset): Map of external IDs keyed by source. Only sources with values are included.
        end_date (datetime.date | Unset): End date of the media (last airing/release) Example: 2011-04-02.
        studio (str | Unset): Animation studio that produced the media Example: J.C.STAFF.
        storage_base_path (str | Unset): Base path for R2/CDN storage (e.g. "media/21459") Example: media/21459.
        characters (list[CharacterInput] | Unset): List of characters appearing in the media with their voice actors
    """

    name_ja: str
    name_romaji: str
    name_en: str
    airing_format: str
    airing_status: str
    genres: list[str]
    start_date: datetime.date
    category: MediaCreateRequestCategory
    version: str
    hash_salt: str
    season_name: str
    season_year: int
    storage: MediaCreateRequestStorage = MediaCreateRequestStorage.R2
    external_ids: ExternalId | Unset = UNSET
    end_date: datetime.date | Unset = UNSET
    studio: str | Unset = UNSET
    storage_base_path: str | Unset = UNSET
    characters: list[CharacterInput] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name_ja = self.name_ja

        name_romaji = self.name_romaji

        name_en = self.name_en

        airing_format = self.airing_format

        airing_status = self.airing_status

        genres = self.genres

        storage = self.storage.value

        start_date = self.start_date.isoformat()

        category = self.category.value

        version = self.version

        hash_salt = self.hash_salt

        season_name = self.season_name

        season_year = self.season_year

        external_ids: dict[str, Any] | Unset = UNSET
        if not isinstance(self.external_ids, Unset):
            external_ids = self.external_ids.to_dict()

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        studio = self.studio

        storage_base_path = self.storage_base_path

        characters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.characters, Unset):
            characters = []
            for characters_item_data in self.characters:
                characters_item = characters_item_data.to_dict()
                characters.append(characters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nameJa": name_ja,
                "nameRomaji": name_romaji,
                "nameEn": name_en,
                "airingFormat": airing_format,
                "airingStatus": airing_status,
                "genres": genres,
                "storage": storage,
                "startDate": start_date,
                "category": category,
                "version": version,
                "hashSalt": hash_salt,
                "seasonName": season_name,
                "seasonYear": season_year,
            }
        )
        if external_ids is not UNSET:
            field_dict["externalIds"] = external_ids
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if studio is not UNSET:
            field_dict["studio"] = studio
        if storage_base_path is not UNSET:
            field_dict["storageBasePath"] = storage_base_path
        if characters is not UNSET:
            field_dict["characters"] = characters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.character_input import CharacterInput
        from ..models.external_id import ExternalId

        _src = dict(src_dict)
        name_ja = _src.pop("nameJa")

        name_romaji = _src.pop("nameRomaji")

        name_en = _src.pop("nameEn")

        airing_format = _src.pop("airingFormat")

        airing_status = _src.pop("airingStatus")

        genres = cast(list[str], _src.pop("genres"))

        storage = MediaCreateRequestStorage(_src.pop("storage"))

        start_date = isoparse(_src.pop("startDate")).date()

        category = MediaCreateRequestCategory(_src.pop("category"))

        version = _src.pop("version")

        hash_salt = _src.pop("hashSalt")

        season_name = _src.pop("seasonName")

        season_year = _src.pop("seasonYear")

        _external_ids = _src.pop("externalIds", UNSET)
        external_ids: ExternalId | Unset
        if isinstance(_external_ids, Unset):
            external_ids = UNSET
        else:
            external_ids = ExternalId.from_dict(_external_ids)

        _end_date = _src.pop("endDate", UNSET)
        end_date: datetime.date | Unset
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date).date()

        studio = _src.pop("studio", UNSET)

        storage_base_path = _src.pop("storageBasePath", UNSET)

        _characters = _src.pop("characters", UNSET)
        characters: list[CharacterInput] | Unset = UNSET
        if _characters is not UNSET:
            characters = []
            for characters_item_data in _characters:
                characters_item = CharacterInput.from_dict(characters_item_data)

                characters.append(characters_item)

        media_create_request = cls(
            name_ja=name_ja,
            name_romaji=name_romaji,
            name_en=name_en,
            airing_format=airing_format,
            airing_status=airing_status,
            genres=genres,
            storage=storage,
            start_date=start_date,
            category=category,
            version=version,
            hash_salt=hash_salt,
            season_name=season_name,
            season_year=season_year,
            external_ids=external_ids,
            end_date=end_date,
            studio=studio,
            storage_base_path=storage_base_path,
            characters=characters,
        )

        media_create_request.additional_properties = _src
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
