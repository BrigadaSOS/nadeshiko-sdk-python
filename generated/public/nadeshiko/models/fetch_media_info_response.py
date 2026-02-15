from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.media_info_data import MediaInfoData
  from ..models.media_info_stats import MediaInfoStats





T = TypeVar("T", bound="FetchMediaInfoResponse")



@_attrs_define
class FetchMediaInfoResponse:
    """ 
        Attributes:
            stats (MediaInfoStats | Unset): Statistics about media and segments in the database
            results (list[MediaInfoData] | Unset):
            cursor (int | Unset): Next cursor for pagination
            has_more_results (bool | Unset): Whether more results are available
     """

    stats: MediaInfoStats | Unset = UNSET
    results: list[MediaInfoData] | Unset = UNSET
    cursor: int | Unset = UNSET
    has_more_results: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.media_info_data import MediaInfoData
        from ..models.media_info_stats import MediaInfoStats
        stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)



        cursor = self.cursor

        has_more_results = self.has_more_results


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if stats is not UNSET:
            field_dict["stats"] = stats
        if results is not UNSET:
            field_dict["results"] = results
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if has_more_results is not UNSET:
            field_dict["hasMoreResults"] = has_more_results

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_info_data import MediaInfoData
        from ..models.media_info_stats import MediaInfoStats
        d = dict(src_dict)
        _stats = d.pop("stats", UNSET)
        stats: MediaInfoStats | Unset
        if isinstance(_stats,  Unset):
            stats = UNSET
        else:
            stats = MediaInfoStats.from_dict(_stats)




        _results = d.pop("results", UNSET)
        results: list[MediaInfoData] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = MediaInfoData.from_dict(results_item_data)



                results.append(results_item)


        cursor = d.pop("cursor", UNSET)

        has_more_results = d.pop("hasMoreResults", UNSET)

        fetch_media_info_response = cls(
            stats=stats,
            results=results,
            cursor=cursor,
            has_more_results=has_more_results,
        )


        fetch_media_info_response.additional_properties = d
        return fetch_media_info_response

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
