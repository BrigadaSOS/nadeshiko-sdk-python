from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.statistic_season_with_episode_hits import StatisticSeasonWithEpisodeHits


T = TypeVar("T", bound="Statistic")


@_attrs_define
class Statistic:
    """Search result statistics grouped by anime/media

    Attributes:
        anime_id (int | Unset): Unique identifier for the anime/media Example: 110316.
        category (int | Unset): Media category (1=Anime, 2=Unknown, 3=J-Drama, 4=Audiobook) Example: 1.
        name_anime_romaji (str | Unset): Romaji transliteration of the anime name Example: Steins;Gate.
        name_anime_en (str | Unset): English translation of the anime name Example: Steins;Gate.
        name_anime_jp (str | Unset): Original Japanese name of the anime Example: シュタインズ・ゲート.
        amount_sentences_found (int | Unset): Total number of sentences found for this anime Example: 42.
        season_with_episode_hits (StatisticSeasonWithEpisodeHits | Unset): Nested object mapping seasons to episodes
            with hit counts Example: {'1': {'1': 5, '2': 8, '3': 3}}.
    """

    anime_id: int | Unset = UNSET
    category: int | Unset = UNSET
    name_anime_romaji: str | Unset = UNSET
    name_anime_en: str | Unset = UNSET
    name_anime_jp: str | Unset = UNSET
    amount_sentences_found: int | Unset = UNSET
    season_with_episode_hits: StatisticSeasonWithEpisodeHits | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        anime_id = self.anime_id

        category = self.category

        name_anime_romaji = self.name_anime_romaji

        name_anime_en = self.name_anime_en

        name_anime_jp = self.name_anime_jp

        amount_sentences_found = self.amount_sentences_found

        season_with_episode_hits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.season_with_episode_hits, Unset):
            season_with_episode_hits = self.season_with_episode_hits.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if anime_id is not UNSET:
            field_dict["anime_id"] = anime_id
        if category is not UNSET:
            field_dict["category"] = category
        if name_anime_romaji is not UNSET:
            field_dict["name_anime_romaji"] = name_anime_romaji
        if name_anime_en is not UNSET:
            field_dict["name_anime_en"] = name_anime_en
        if name_anime_jp is not UNSET:
            field_dict["name_anime_jp"] = name_anime_jp
        if amount_sentences_found is not UNSET:
            field_dict["amount_sentences_found"] = amount_sentences_found
        if season_with_episode_hits is not UNSET:
            field_dict["season_with_episode_hits"] = season_with_episode_hits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.statistic_season_with_episode_hits import StatisticSeasonWithEpisodeHits

        d = dict(src_dict)
        anime_id = d.pop("anime_id", UNSET)

        category = d.pop("category", UNSET)

        name_anime_romaji = d.pop("name_anime_romaji", UNSET)

        name_anime_en = d.pop("name_anime_en", UNSET)

        name_anime_jp = d.pop("name_anime_jp", UNSET)

        amount_sentences_found = d.pop("amount_sentences_found", UNSET)

        _season_with_episode_hits = d.pop("season_with_episode_hits", UNSET)
        season_with_episode_hits: StatisticSeasonWithEpisodeHits | Unset
        if isinstance(_season_with_episode_hits, Unset):
            season_with_episode_hits = UNSET
        else:
            season_with_episode_hits = StatisticSeasonWithEpisodeHits.from_dict(
                _season_with_episode_hits
            )

        statistic = cls(
            anime_id=anime_id,
            category=category,
            name_anime_romaji=name_anime_romaji,
            name_anime_en=name_anime_en,
            name_anime_jp=name_anime_jp,
            amount_sentences_found=amount_sentences_found,
            season_with_episode_hits=season_with_episode_hits,
        )

        statistic.additional_properties = d
        return statistic

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
