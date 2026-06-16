from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.category import Category, check_category
from ..models.media_airing_format import MediaAiringFormat, check_media_airing_format
from ..models.media_airing_status import MediaAiringStatus, check_media_airing_status
from ..models.media_season_name import MediaSeasonName, check_media_season_name

if TYPE_CHECKING:
    from ..models.external_id import ExternalId


T = TypeVar("T", bound="Media")


@_attrs_define
class Media:
    """Media entry with full metadata

    Attributes:
        public_id (str): Public ID for the media (use this in public URLs) Example: V1StGXR8_Z5d.
        slug (str): URL-friendly slug for the media Example: bakuman.
        external_ids (ExternalId): External IDs for this media, keyed by source. Every source appears as a key; absent
            mappings are represented with a null value.
        name_ja (str): Original Japanese name of the media Example: バクマン。.
        name_romaji (str): Romaji transliteration of the media name Example: Bakuman..
        name_en (str): English name of the media Example: Bakuman..
        airing_format (MediaAiringFormat): Format of the media release Example: TV.
        airing_status (MediaAiringStatus): Current airing status Example: FINISHED.
        genres (list[str]): List of genres associated with the media Example: ['Comedy', 'Drama', 'Romance', 'Slice of
            Life'].
        cover_url (str): Full URL to the cover image Example: https://cdn.example.com/media/anime/bakuman/cover.webp.
        banner_url (str): Full URL to the banner image Example: https://cdn.example.com/media/anime/bakuman/banner.webp.
        start_date (datetime.date): Start date of the media (first airing/release) Example: 2010-10-02.
        end_date (datetime.date | None): End date of the media (last airing/release) Example: 2011-04-02.
        category (Category): Media category type Example: ANIME.
        segment_count (int): Total number of subtitle segments available Example: 1234.
        episode_count (int): Total number of episodes available Example: 25.
        studio (None | str): Animation studio that produced the media Example: J.C.STAFF.
        season_name (MediaSeasonName): Airing season label for the media Example: FALL.
        season_year (int): Airing year for the media Example: 2010.
    """

    public_id: str
    slug: str
    external_ids: ExternalId
    name_ja: str
    name_romaji: str
    name_en: str
    airing_format: MediaAiringFormat
    airing_status: MediaAiringStatus
    genres: list[str]
    cover_url: str
    banner_url: str
    start_date: datetime.date
    end_date: datetime.date | None
    category: Category
    segment_count: int
    episode_count: int
    studio: None | str
    season_name: MediaSeasonName
    season_year: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_id = self.public_id

        slug = self.slug

        external_ids = self.external_ids.to_dict()

        name_ja = self.name_ja

        name_romaji = self.name_romaji

        name_en = self.name_en

        airing_format: str = self.airing_format

        airing_status: str = self.airing_status

        genres = self.genres

        cover_url = self.cover_url

        banner_url = self.banner_url

        start_date = self.start_date.isoformat()

        end_date: None | str
        if isinstance(self.end_date, datetime.date):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        category: str = self.category

        segment_count = self.segment_count

        episode_count = self.episode_count

        studio: None | str
        studio = self.studio

        season_name: str = self.season_name

        season_year = self.season_year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "publicId": public_id,
                "slug": slug,
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
                "endDate": end_date,
                "category": category,
                "segmentCount": segment_count,
                "episodeCount": episode_count,
                "studio": studio,
                "seasonName": season_name,
                "seasonYear": season_year,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.external_id import ExternalId

        _src = dict(src_dict)
        public_id = _src.pop("publicId")

        slug = _src.pop("slug")

        external_ids = ExternalId.from_dict(_src.pop("externalIds"))

        name_ja = _src.pop("nameJa")

        name_romaji = _src.pop("nameRomaji")

        name_en = _src.pop("nameEn")

        airing_format = check_media_airing_format(_src.pop("airingFormat"))

        airing_status = check_media_airing_status(_src.pop("airingStatus"))

        genres = cast(list[str], _src.pop("genres"))

        cover_url = _src.pop("coverUrl")

        banner_url = _src.pop("bannerUrl")

        start_date = datetime.date.fromisoformat(_src.pop("startDate"))

        def _parse_end_date(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = datetime.date.fromisoformat(data)

                return end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        end_date = _parse_end_date(_src.pop("endDate"))

        category = check_category(_src.pop("category"))

        segment_count = _src.pop("segmentCount")

        episode_count = _src.pop("episodeCount")

        def _parse_studio(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        studio = _parse_studio(_src.pop("studio"))

        season_name = check_media_season_name(_src.pop("seasonName"))

        season_year = _src.pop("seasonYear")

        media = cls(
            public_id=public_id,
            slug=slug,
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
            end_date=end_date,
            category=category,
            segment_count=segment_count,
            episode_count=episode_count,
            studio=studio,
            season_name=season_name,
            season_year=season_year,
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
