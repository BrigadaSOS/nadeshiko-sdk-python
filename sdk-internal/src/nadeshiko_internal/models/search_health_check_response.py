from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.category_statistic import CategoryStatistic
  from ..models.sentence import Sentence
  from ..models.statistic import Statistic





T = TypeVar("T", bound="SearchHealthCheckResponse")



@_attrs_define
class SearchHealthCheckResponse:
    """ 
        Attributes:
            statistics (list[Statistic] | Unset):
            category_statistics (list[CategoryStatistic] | Unset):
            sentences (list[Sentence] | Unset):
            cursor (list[float] | Unset): Cursor for pagination
     """

    statistics: list[Statistic] | Unset = UNSET
    category_statistics: list[CategoryStatistic] | Unset = UNSET
    sentences: list[Sentence] | Unset = UNSET
    cursor: list[float] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sentence import Sentence
        from ..models.category_statistic import CategoryStatistic
        from ..models.statistic import Statistic
        statistics: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = []
            for statistics_item_data in self.statistics:
                statistics_item = statistics_item_data.to_dict()
                statistics.append(statistics_item)



        category_statistics: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.category_statistics, Unset):
            category_statistics = []
            for category_statistics_item_data in self.category_statistics:
                category_statistics_item = category_statistics_item_data.to_dict()
                category_statistics.append(category_statistics_item)



        sentences: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sentences, Unset):
            sentences = []
            for sentences_item_data in self.sentences:
                sentences_item = sentences_item_data.to_dict()
                sentences.append(sentences_item)



        cursor: list[float] | Unset = UNSET
        if not isinstance(self.cursor, Unset):
            cursor = self.cursor




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if category_statistics is not UNSET:
            field_dict["categoryStatistics"] = category_statistics
        if sentences is not UNSET:
            field_dict["sentences"] = sentences
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.category_statistic import CategoryStatistic
        from ..models.sentence import Sentence
        from ..models.statistic import Statistic
        d = dict(src_dict)
        _statistics = d.pop("statistics", UNSET)
        statistics: list[Statistic] | Unset = UNSET
        if _statistics is not UNSET:
            statistics = []
            for statistics_item_data in _statistics:
                statistics_item = Statistic.from_dict(statistics_item_data)



                statistics.append(statistics_item)


        _category_statistics = d.pop("categoryStatistics", UNSET)
        category_statistics: list[CategoryStatistic] | Unset = UNSET
        if _category_statistics is not UNSET:
            category_statistics = []
            for category_statistics_item_data in _category_statistics:
                category_statistics_item = CategoryStatistic.from_dict(category_statistics_item_data)



                category_statistics.append(category_statistics_item)


        _sentences = d.pop("sentences", UNSET)
        sentences: list[Sentence] | Unset = UNSET
        if _sentences is not UNSET:
            sentences = []
            for sentences_item_data in _sentences:
                sentences_item = Sentence.from_dict(sentences_item_data)



                sentences.append(sentences_item)


        cursor = cast(list[float], d.pop("cursor", UNSET))


        search_health_check_response = cls(
            statistics=statistics,
            category_statistics=category_statistics,
            sentences=sentences,
            cursor=cursor,
        )


        search_health_check_response.additional_properties = d
        return search_health_check_response

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
