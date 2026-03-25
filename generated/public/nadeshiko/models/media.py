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
    from ..models.media_character import MediaCharacter


T = TypeVar("T", bound="Media")


@_attrs_define
class Media:
    """Media entry with full metadata

    Attributes:
        id (int): Internal unique identifier for the media Example: 7674.
        public_id (str): Public identifier for the media (use this in public URLs) Example: V1StGXR8_Z5d.
        external_ids (ExternalId): Map of external IDs keyed by source. Only sources with values are included.
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
        segment_count (int): Total number of subtitle segments available
        episode_count (int): Total number of episodes available Example: 25.
        season_name (str): Airing season label for the media Example: FALL.
        season_year (int): Airing year for the media Example: 2010.
        end_date (datetime.date | None | Unset): End date of the media (last airing/release) Example: 2011-04-02.
        studio (None | str | Unset): Animation studio that produced the media Example: J.C.STAFF.
        characters (list[MediaCharacter] | Unset): Characters appearing in the media with their voice actors
    """

    id: int
    public_id: str
    external_ids: ExternalId
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
    segment_count: int
    episode_count: int
    season_name: str
    season_year: int
    end_date: datetime.date | None | Unset = UNSET
    studio: None | str | Unset = UNSET
    characters: list[MediaCharacter] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        public_id = self.public_id

        external_ids = self.external_ids.to_dict()

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

        segment_count = self.segment_count

        episode_count = self.episode_count

        season_name = self.season_name

        season_year = self.season_year

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.date):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        studio: None | str | Unset
        if isinstance(self.studio, Unset):
            studio = UNSET
        else:
            studio = self.studio

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
                "id": id,
                "publicId": public_id,
                "externalIds": external_ids,
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
                "segmentCount": segment_count,
                "episodeCount": episode_count,
                "seasonName": season_name,
                "seasonYear": season_year,
            }
        )
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if studio is not UNSET:
            field_dict["studio"] = studio
        if characters is not UNSET:
            field_dict["characters"] = characters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.external_id import ExternalId
        from ..models.media_character import MediaCharacter

        _src = dict(src_dict)
        id = _src.pop("id")

        public_id = _src.pop("publicId")

        external_ids = ExternalId.from_dict(_src.pop("externalIds"))

        name_ja = _src.pop("nameJa")

        name_romaji = _src.pop("nameRomaji")

        name_en = _src.pop("nameEn")

        airing_format = _src.pop("airingFormat")

        airing_status = _src.pop("airingStatus")

        genres = cast(list[str], _src.pop("genres"))

        cover_url = _src.pop("coverUrl")

        banner_url = _src.pop("bannerUrl")

        start_date = isoparse(_src.pop("startDate")).date()

        category = Category(_src.pop("category"))

        segment_count = _src.pop("segmentCount")

        episode_count = _src.pop("episodeCount")

        season_name = _src.pop("seasonName")

        season_year = _src.pop("seasonYear")

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

        end_date = _parse_end_date(_src.pop("endDate", UNSET))

        def _parse_studio(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        studio = _parse_studio(_src.pop("studio", UNSET))

        _characters = _src.pop("characters", UNSET)
        characters: list[MediaCharacter] | Unset = UNSET
        if _characters is not UNSET:
            characters = []
            for characters_item_data in _characters:
                characters_item = MediaCharacter.from_dict(characters_item_data)

                characters.append(characters_item)

        media = cls(
            id=id,
            public_id=public_id,
            external_ids=external_ids,
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
            segment_count=segment_count,
            episode_count=episode_count,
            season_name=season_name,
            season_year=season_year,
            end_date=end_date,
            studio=studio,
            characters=characters,
        )

        media.additional_properties = _src
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
