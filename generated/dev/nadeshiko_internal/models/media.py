from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.category import Category
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_id import ExternalId
    from ..models.list_ import List
    from ..models.media_character import MediaCharacter


T = TypeVar("T", bound="Media")


@_attrs_define
class Media:
    """Media entry with full metadata

    Attributes:
        id (int): Unique identifier for the media Example: 7674.
        name_ja (str): Original Japanese name of the media Example: バクマン。.
        name_romaji (str): Romaji transliteration of the media name Example: Bakuman..
        name_en (str): English name of the media Example: Bakuman..
        airing_format (str): Format of the media release (e.g., TV, OVA, Movie) Example: TV.
        airing_status (str): Current airing status (FINISHED, RELEASING, NOT_YET_RELEASED, CANCELLED) Example: FINISHED.
        genres (list[str]): List of genres associated with the media Example: ['Comedy', 'Drama', 'Romance', 'Slice of
            Life'].
        cover_url (str): Full URL to the cover image Example: https://cdn.example.com/media/anime/bakuman/cover.webp.
        banner_url (str): Full URL to the banner image Example: https://cdn.example.com/media/anime/bakuman/banner.webp.
        start_date (datetime.date): Start date of the media (first airing/release) Example: 2010-10-02.
        category (Category): Media category type Example: ANIME.
        version (str): Version identifier for the media entry Example: 6.
        studio (str): Animation studio that produced the media Example: J.C.STAFF.
        season_name (str): Airing season label for the media Example: FALL.
        season_year (int): Airing year for the media Example: 2010.
        external_ids (ExternalId | Unset): Map of external IDs keyed by source. Only sources with values are included.
        end_date (datetime.date | None | Unset): End date of the media (last airing/release) Example: 2011-04-02.
        segment_count (int | Unset): Total number of subtitle segments available
        episode_count (int | Unset): Total number of episodes available Example: 25.
        storage_base_path (None | str | Unset): Base path for R2/CDN storage (e.g. "media/21459") Example: media/21459.
        characters (list[MediaCharacter] | Unset): Characters appearing in the media with their voice actors
        lists (list[List] | Unset): Lists that contain this media
    """

    id: int
    name_ja: str
    name_romaji: str
    name_en: str
    airing_format: str
    airing_status: str
    genres: list[str]
    cover_url: str
    banner_url: str
    start_date: datetime.date
    category: Category
    version: str
    studio: str
    season_name: str
    season_year: int
    external_ids: ExternalId | Unset = UNSET
    end_date: datetime.date | None | Unset = UNSET
    segment_count: int | Unset = UNSET
    episode_count: int | Unset = UNSET
    storage_base_path: None | str | Unset = UNSET
    characters: list[MediaCharacter] | Unset = UNSET
    lists: list[List] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name_ja = self.name_ja

        name_romaji = self.name_romaji

        name_en = self.name_en

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

        external_ids: dict[str, Any] | Unset = UNSET
        if not isinstance(self.external_ids, Unset):
            external_ids = self.external_ids.to_dict()

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.date):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        segment_count = self.segment_count

        episode_count = self.episode_count

        storage_base_path: None | str | Unset
        if isinstance(self.storage_base_path, Unset):
            storage_base_path = UNSET
        else:
            storage_base_path = self.storage_base_path

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
                "nameJa": name_ja,
                "nameRomaji": name_romaji,
                "nameEn": name_en,
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
        if external_ids is not UNSET:
            field_dict["externalIds"] = external_ids
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if segment_count is not UNSET:
            field_dict["segmentCount"] = segment_count
        if episode_count is not UNSET:
            field_dict["episodeCount"] = episode_count
        if storage_base_path is not UNSET:
            field_dict["storageBasePath"] = storage_base_path
        if characters is not UNSET:
            field_dict["characters"] = characters
        if lists is not UNSET:
            field_dict["lists"] = lists

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.external_id import ExternalId
        from ..models.list_ import List
        from ..models.media_character import MediaCharacter

        d = dict(src_dict)
        id = d.pop("id")

        name_ja = d.pop("nameJa")

        name_romaji = d.pop("nameRomaji")

        name_en = d.pop("nameEn")

        airing_format = d.pop("airingFormat")

        airing_status = d.pop("airingStatus")

        genres = cast(list[str], d.pop("genres"))

        cover_url = d.pop("coverUrl")

        banner_url = d.pop("bannerUrl")

        start_date = isoparse(d.pop("startDate")).date()

        category = Category(d.pop("category"))

        version = d.pop("version")

        studio = d.pop("studio")

        season_name = d.pop("seasonName")

        season_year = d.pop("seasonYear")

        _external_ids = d.pop("externalIds", UNSET)
        external_ids: ExternalId | Unset
        if isinstance(_external_ids, Unset):
            external_ids = UNSET
        else:
            external_ids = ExternalId.from_dict(_external_ids)

        def _parse_end_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data).date()

                return end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        end_date = _parse_end_date(d.pop("endDate", UNSET))

        segment_count = d.pop("segmentCount", UNSET)

        episode_count = d.pop("episodeCount", UNSET)

        def _parse_storage_base_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_base_path = _parse_storage_base_path(d.pop("storageBasePath", UNSET))

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
            name_ja=name_ja,
            name_romaji=name_romaji,
            name_en=name_en,
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
            external_ids=external_ids,
            end_date=end_date,
            segment_count=segment_count,
            episode_count=episode_count,
            storage_base_path=storage_base_path,
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
