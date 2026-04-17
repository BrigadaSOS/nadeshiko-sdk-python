from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.category import Category
from ..models.media_create_request_airing_format import MediaCreateRequestAiringFormat
from ..models.media_create_request_airing_status import MediaCreateRequestAiringStatus
from ..models.media_create_request_season_name import MediaCreateRequestSeasonName
from ..models.media_create_request_storage import MediaCreateRequestStorage
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_id import ExternalId


T = TypeVar("T", bound="MediaCreateRequest")


@_attrs_define
class MediaCreateRequest:
    """Request body for creating a new media entry

    Attributes:
        name_ja (str): Original Japanese name of the media Example: バクマン。.
        name_romaji (str): Romaji transliteration of the media name Example: Bakuman..
        name_en (str): English name of the media Example: Bakuman..
        airing_format (MediaCreateRequestAiringFormat): Format of the media release Example: TV.
        airing_status (MediaCreateRequestAiringStatus): Current airing status Example: FINISHED.
        genres (list[str]): List of genres associated with the media Example: ['Comedy', 'Drama', 'Romance', 'Slice of
            Life'].
        storage (MediaCreateRequestStorage): Storage backend for media assets Default: MediaCreateRequestStorage.R2.
            Example: R2.
        start_date (datetime.date): Start date of the media (first airing/release) Example: 2010-10-02.
        category (Category): Media category type Example: ANIME.
        version (str): Version of the media-sub-splitter used Example: 6.
        hash_salt (str): Hash salt used when generating the hash for the related media assets Example:
            ba0cbe173ed310528f16130273662a60.
        season_name (MediaCreateRequestSeasonName): Airing season label for the media Example: FALL.
        season_year (int): Airing year for the media Example: 2010.
        external_ids (ExternalId | Unset): External IDs for this media, keyed by source. Every source appears as a key;
            absent mappings are represented with a null value.
        end_date (datetime.date | Unset): End date of the media (last airing/release) Example: 2011-04-02.
        studio (None | str | Unset): Animation studio that produced the media. Pass `null` to explicitly mark as
            unknown. Example: J.C.STAFF.
        storage_base_path (str | Unset): Base path for R2/CDN storage (e.g. "media/21459") Example: media/21459.
    """

    name_ja: str
    name_romaji: str
    name_en: str
    airing_format: MediaCreateRequestAiringFormat
    airing_status: MediaCreateRequestAiringStatus
    genres: list[str]
    start_date: datetime.date
    category: Category
    version: str
    hash_salt: str
    season_name: MediaCreateRequestSeasonName
    season_year: int
    storage: MediaCreateRequestStorage = MediaCreateRequestStorage.R2
    external_ids: ExternalId | Unset = UNSET
    end_date: datetime.date | Unset = UNSET
    studio: None | str | Unset = UNSET
    storage_base_path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name_ja = self.name_ja

        name_romaji = self.name_romaji

        name_en = self.name_en

        airing_format = self.airing_format.value

        airing_status = self.airing_status.value

        genres = self.genres

        storage = self.storage.value

        start_date = self.start_date.isoformat()

        category = self.category.value

        version = self.version

        hash_salt = self.hash_salt

        season_name = self.season_name.value

        season_year = self.season_year

        external_ids: dict[str, Any] | Unset = UNSET
        if not isinstance(self.external_ids, Unset):
            external_ids = self.external_ids.to_dict()

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        studio: None | str | Unset
        if isinstance(self.studio, Unset):
            studio = UNSET
        else:
            studio = self.studio

        storage_base_path = self.storage_base_path

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.external_id import ExternalId

        _src = dict(src_dict)
        name_ja = _src.pop("nameJa")

        name_romaji = _src.pop("nameRomaji")

        name_en = _src.pop("nameEn")

        airing_format = MediaCreateRequestAiringFormat(_src.pop("airingFormat"))

        airing_status = MediaCreateRequestAiringStatus(_src.pop("airingStatus"))

        genres = cast(list[str], _src.pop("genres"))

        storage = MediaCreateRequestStorage(_src.pop("storage"))

        start_date = isoparse(_src.pop("startDate")).date()

        category = Category(_src.pop("category"))

        version = _src.pop("version")

        hash_salt = _src.pop("hashSalt")

        season_name = MediaCreateRequestSeasonName(_src.pop("seasonName"))

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

        def _parse_studio(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        studio = _parse_studio(_src.pop("studio", UNSET))

        storage_base_path = _src.pop("storageBasePath", UNSET)

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
