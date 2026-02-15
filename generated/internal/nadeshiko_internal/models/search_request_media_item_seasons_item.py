from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="SearchRequestMediaItemSeasonsItem")



@_attrs_define
class SearchRequestMediaItemSeasonsItem:
    """ 
        Attributes:
            season (float):  Example: 1.
            episodes (list[float]):  Example: [1, 2].
     """

    season: float
    episodes: list[float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        season = self.season

        episodes = self.episodes




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "season": season,
            "episodes": episodes,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        season = d.pop("season")

        episodes = cast(list[float], d.pop("episodes"))


        search_request_media_item_seasons_item = cls(
            season=season,
            episodes=episodes,
        )


        search_request_media_item_seasons_item.additional_properties = d
        return search_request_media_item_seasons_item

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
