from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.category import Category, check_category
from ..models.media_update_request_airing_format import (
    MediaUpdateRequestAiringFormat,
    check_media_update_request_airing_format,
)
from ..models.media_update_request_airing_status import (
    MediaUpdateRequestAiringStatus,
    check_media_update_request_airing_status,
)
from ..models.media_update_request_season_name import (
    MediaUpdateRequestSeasonName,
    check_media_update_request_season_name,
)
from ..models.media_update_request_storage import (
    MediaUpdateRequestStorage,
    check_media_update_request_storage,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_id import ExternalId


T = TypeVar("T", bound="MediaUpdateRequest")


@_attrs_define
class MediaUpdateRequest:
    """Request body for updating an existing media entry (all fields optional)

    Attributes:
        external_ids (ExternalId | Unset): External IDs for this media, keyed by source. Every source appears as a key;
            absent mappings are represented with a null value.
        name_ja (str | Unset): Original Japanese name of the media Example: バクマン。.
        name_romaji (str | Unset): Romaji transliteration of the media name Example: Bakuman..
        name_en (str | Unset): English name of the media Example: Bakuman..
        airing_format (MediaUpdateRequestAiringFormat | Unset): Format of the media release Example: TV.
        airing_status (MediaUpdateRequestAiringStatus | Unset): Current airing status Example: FINISHED.
        genres (list[str] | Unset): List of genres associated with the media Example: ['Comedy', 'Drama', 'Romance',
            'Slice of Life'].
        storage (MediaUpdateRequestStorage | Unset): Storage backend for media assets Example: R2.
        start_date (datetime.date | Unset): Start date of the media (first airing/release) Example: 2010-10-02.
        end_date (datetime.date | None | Unset): End date of the media (last airing/release). Pass `null` to clear
            (return the show to ongoing). Example: 2011-04-02.
        category (Category | Unset): Media category type Example: ANIME.
        version (str | Unset): Version of the media-sub-splitter used Example: 6.
        hash_salt (str | Unset): Hash salt used when generating the hash for the related media assets Example:
            ba0cbe173ed310528f16130273662a60.
        studio (None | str | Unset): Animation studio that produced the media. Pass `null` to clear back to unknown.
            Example: J.C.STAFF.
        season_name (MediaUpdateRequestSeasonName | Unset): Airing season label for the media Example: FALL.
        season_year (int | Unset): Airing year for the media Example: 2010.
        storage_base_path (str | Unset): Base path for R2/CDN storage (e.g. "media/21459") Example: media/21459.
        segment_count (int | Unset): Total number of subtitle segments available Example: 1234.
    """

    external_ids: ExternalId | Unset = UNSET
    name_ja: str | Unset = UNSET
    name_romaji: str | Unset = UNSET
    name_en: str | Unset = UNSET
    airing_format: MediaUpdateRequestAiringFormat | Unset = UNSET
    airing_status: MediaUpdateRequestAiringStatus | Unset = UNSET
    genres: list[str] | Unset = UNSET
    storage: MediaUpdateRequestStorage | Unset = UNSET
    start_date: datetime.date | Unset = UNSET
    end_date: datetime.date | None | Unset = UNSET
    category: Category | Unset = UNSET
    version: str | Unset = UNSET
    hash_salt: str | Unset = UNSET
    studio: None | str | Unset = UNSET
    season_name: MediaUpdateRequestSeasonName | Unset = UNSET
    season_year: int | Unset = UNSET
    storage_base_path: str | Unset = UNSET
    segment_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_ids: dict[str, Any] | Unset = UNSET
        if not isinstance(self.external_ids, Unset):
            external_ids = self.external_ids.to_dict()

        name_ja = self.name_ja

        name_romaji = self.name_romaji

        name_en = self.name_en

        airing_format: str | Unset = UNSET
        if not isinstance(self.airing_format, Unset):
            airing_format = self.airing_format

        airing_status: str | Unset = UNSET
        if not isinstance(self.airing_status, Unset):
            airing_status = self.airing_status

        genres: list[str] | Unset = UNSET
        if not isinstance(self.genres, Unset):
            genres = self.genres

        storage: str | Unset = UNSET
        if not isinstance(self.storage, Unset):
            storage = self.storage

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.date):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category

        version = self.version

        hash_salt = self.hash_salt

        studio: None | str | Unset
        if isinstance(self.studio, Unset):
            studio = UNSET
        else:
            studio = self.studio

        season_name: str | Unset = UNSET
        if not isinstance(self.season_name, Unset):
            season_name = self.season_name

        season_year = self.season_year

        storage_base_path = self.storage_base_path

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
        if storage_base_path is not UNSET:
            field_dict["storageBasePath"] = storage_base_path
        if segment_count is not UNSET:
            field_dict["segmentCount"] = segment_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.external_id import ExternalId

        _src = dict(src_dict)
        _external_ids = _src.pop("externalIds", UNSET)
        external_ids: ExternalId | Unset
        if isinstance(_external_ids, Unset):
            external_ids = UNSET
        else:
            external_ids = ExternalId.from_dict(_external_ids)

        name_ja = _src.pop("nameJa", UNSET)

        name_romaji = _src.pop("nameRomaji", UNSET)

        name_en = _src.pop("nameEn", UNSET)

        _airing_format = _src.pop("airingFormat", UNSET)
        airing_format: MediaUpdateRequestAiringFormat | Unset
        if isinstance(_airing_format, Unset):
            airing_format = UNSET
        else:
            airing_format = check_media_update_request_airing_format(_airing_format)

        _airing_status = _src.pop("airingStatus", UNSET)
        airing_status: MediaUpdateRequestAiringStatus | Unset
        if isinstance(_airing_status, Unset):
            airing_status = UNSET
        else:
            airing_status = check_media_update_request_airing_status(_airing_status)

        genres = cast(list[str], _src.pop("genres", UNSET))

        _storage = _src.pop("storage", UNSET)
        storage: MediaUpdateRequestStorage | Unset
        if isinstance(_storage, Unset):
            storage = UNSET
        else:
            storage = check_media_update_request_storage(_storage)

        _start_date = _src.pop("startDate", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = datetime.date.fromisoformat(_start_date)

        def _parse_end_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = datetime.date.fromisoformat(data)

                return end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        end_date = _parse_end_date(_src.pop("endDate", UNSET))

        _category = _src.pop("category", UNSET)
        category: Category | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = check_category(_category)

        version = _src.pop("version", UNSET)

        hash_salt = _src.pop("hashSalt", UNSET)

        def _parse_studio(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        studio = _parse_studio(_src.pop("studio", UNSET))

        _season_name = _src.pop("seasonName", UNSET)
        season_name: MediaUpdateRequestSeasonName | Unset
        if isinstance(_season_name, Unset):
            season_name = UNSET
        else:
            season_name = check_media_update_request_season_name(_season_name)

        season_year = _src.pop("seasonYear", UNSET)

        storage_base_path = _src.pop("storageBasePath", UNSET)

        segment_count = _src.pop("segmentCount", UNSET)

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
            storage_base_path=storage_base_path,
            segment_count=segment_count,
        )

        media_update_request.additional_properties = _src
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
