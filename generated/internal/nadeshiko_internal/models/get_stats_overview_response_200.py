from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.get_stats_overview_response_200_translations import (
        GetStatsOverviewResponse200Translations,
    )
    from ..models.word_coverage_tier import WordCoverageTier


T = TypeVar("T", bound="GetStatsOverviewResponse200")


@_attrs_define
class GetStatsOverviewResponse200:
    """
    Attributes:
        total_segments (int): Total number of active segments in the corpus Example: 1200000.
        total_episodes (int): Total number of episodes Example: 8500.
        total_media (int): Total number of media entries Example: 350.
        total_frequency_words (int): Total number of words in the frequency list Example: 215900.
        dialogue_hours (float): Total hours of Japanese dialogue (subtitle coverage time) Example: 2450.5.
        tiers (list[WordCoverageTier]):
        last_updated (datetime.datetime | None): When the word coverage data was last updated
        translations (GetStatsOverviewResponse200Translations):
    """

    total_segments: int
    total_episodes: int
    total_media: int
    total_frequency_words: int
    dialogue_hours: float
    tiers: list[WordCoverageTier]
    last_updated: datetime.datetime | None
    translations: GetStatsOverviewResponse200Translations
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_segments = self.total_segments

        total_episodes = self.total_episodes

        total_media = self.total_media

        total_frequency_words = self.total_frequency_words

        dialogue_hours = self.dialogue_hours

        tiers = []
        for tiers_item_data in self.tiers:
            tiers_item = tiers_item_data.to_dict()
            tiers.append(tiers_item)

        last_updated: None | str
        if isinstance(self.last_updated, datetime.datetime):
            last_updated = self.last_updated.isoformat()
        else:
            last_updated = self.last_updated

        translations = self.translations.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalSegments": total_segments,
                "totalEpisodes": total_episodes,
                "totalMedia": total_media,
                "totalFrequencyWords": total_frequency_words,
                "dialogueHours": dialogue_hours,
                "tiers": tiers,
                "lastUpdated": last_updated,
                "translations": translations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_stats_overview_response_200_translations import (
            GetStatsOverviewResponse200Translations,
        )
        from ..models.word_coverage_tier import WordCoverageTier

        _src = dict(src_dict)
        total_segments = _src.pop("totalSegments")

        total_episodes = _src.pop("totalEpisodes")

        total_media = _src.pop("totalMedia")

        total_frequency_words = _src.pop("totalFrequencyWords")

        dialogue_hours = _src.pop("dialogueHours")

        tiers = []
        _tiers = _src.pop("tiers")
        for tiers_item_data in _tiers:
            tiers_item = WordCoverageTier.from_dict(tiers_item_data)

            tiers.append(tiers_item)

        def _parse_last_updated(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_updated_type_0 = isoparse(data)

                return last_updated_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_updated = _parse_last_updated(_src.pop("lastUpdated"))

        translations = GetStatsOverviewResponse200Translations.from_dict(_src.pop("translations"))

        get_stats_overview_response_200 = cls(
            total_segments=total_segments,
            total_episodes=total_episodes,
            total_media=total_media,
            total_frequency_words=total_frequency_words,
            dialogue_hours=dialogue_hours,
            tiers=tiers,
            last_updated=last_updated,
            translations=translations,
        )

        get_stats_overview_response_200.additional_properties = _src
        return get_stats_overview_response_200

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
