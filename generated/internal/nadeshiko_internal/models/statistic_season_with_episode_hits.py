from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.statistic_season_with_episode_hits_additional_property import StatisticSeasonWithEpisodeHitsAdditionalProperty





T = TypeVar("T", bound="StatisticSeasonWithEpisodeHits")



@_attrs_define
class StatisticSeasonWithEpisodeHits:
    """ Nested object mapping seasons to episodes with hit counts

        Example:
            {'1': {'1': 5, '2': 8, '3': 3}}

     """

    additional_properties: dict[str, StatisticSeasonWithEpisodeHitsAdditionalProperty] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.statistic_season_with_episode_hits_additional_property import StatisticSeasonWithEpisodeHitsAdditionalProperty
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.statistic_season_with_episode_hits_additional_property import StatisticSeasonWithEpisodeHitsAdditionalProperty
        d = dict(src_dict)
        statistic_season_with_episode_hits = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = StatisticSeasonWithEpisodeHitsAdditionalProperty.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        statistic_season_with_episode_hits.additional_properties = additional_properties
        return statistic_season_with_episode_hits

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> StatisticSeasonWithEpisodeHitsAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: StatisticSeasonWithEpisodeHitsAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
