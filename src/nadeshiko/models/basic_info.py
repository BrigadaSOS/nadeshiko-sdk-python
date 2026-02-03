from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BasicInfo")


@_attrs_define
class BasicInfo:
    """Basic anime/media information included in search results

    Attributes:
        id_anime (int): Unique identifier for the anime/media Example: 110316.
        name_anime_romaji (str): Romaji transliteration of the anime name Example: Steins;Gate.
        episode (int): Episode number where the segment appears Example: 1.
        season (int): Season number where the segment appears Example: 1.
        category (int): Media category (1=Anime, 2=Unknown, 3=J-Drama, 4=Audiobook) Example: 1.
        name_anime_en (str | Unset): English translation of the anime name Example: Steins;Gate.
        name_anime_jp (str | Unset): Original Japanese name of the anime Example: シュタインズ・ゲート.
        cover (str | Unset): URL to the cover image Example: https://example.com/media/anime/steins-gate/cover.jpg.
        banner (str | Unset): URL to the banner image Example: https://example.com/media/anime/steins-gate/banner.jpg.
    """

    id_anime: int
    name_anime_romaji: str
    episode: int
    season: int
    category: int
    name_anime_en: str | Unset = UNSET
    name_anime_jp: str | Unset = UNSET
    cover: str | Unset = UNSET
    banner: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id_anime = self.id_anime

        name_anime_romaji = self.name_anime_romaji

        episode = self.episode

        season = self.season

        category = self.category

        name_anime_en = self.name_anime_en

        name_anime_jp = self.name_anime_jp

        cover = self.cover

        banner = self.banner

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id_anime": id_anime,
                "name_anime_romaji": name_anime_romaji,
                "episode": episode,
                "season": season,
                "category": category,
            }
        )
        if name_anime_en is not UNSET:
            field_dict["name_anime_en"] = name_anime_en
        if name_anime_jp is not UNSET:
            field_dict["name_anime_jp"] = name_anime_jp
        if cover is not UNSET:
            field_dict["cover"] = cover
        if banner is not UNSET:
            field_dict["banner"] = banner

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id_anime = d.pop("id_anime")

        name_anime_romaji = d.pop("name_anime_romaji")

        episode = d.pop("episode")

        season = d.pop("season")

        category = d.pop("category")

        name_anime_en = d.pop("name_anime_en", UNSET)

        name_anime_jp = d.pop("name_anime_jp", UNSET)

        cover = d.pop("cover", UNSET)

        banner = d.pop("banner", UNSET)

        basic_info = cls(
            id_anime=id_anime,
            name_anime_romaji=name_anime_romaji,
            episode=episode,
            season=season,
            category=category,
            name_anime_en=name_anime_en,
            name_anime_jp=name_anime_jp,
            cover=cover,
            banner=banner,
        )

        basic_info.additional_properties = d
        return basic_info

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
