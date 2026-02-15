from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.episode import Episode





T = TypeVar("T", bound="EpisodeListResponse")



@_attrs_define
class EpisodeListResponse:
    """ 
        Attributes:
            data (list[Episode]): Array of episode objects
            has_more_results (bool): Whether more results are available Example: True.
            cursor (int | Unset): Cursor for pagination (last episode number in current page) Example: 12.
     """

    data: list[Episode]
    has_more_results: bool
    cursor: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.episode import Episode
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)



        has_more_results = self.has_more_results

        cursor = self.cursor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "data": data,
            "hasMoreResults": has_more_results,
        })
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.episode import Episode
        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in (_data):
            data_item = Episode.from_dict(data_item_data)



            data.append(data_item)


        has_more_results = d.pop("hasMoreResults")

        cursor = d.pop("cursor", UNSET)

        episode_list_response = cls(
            data=data,
            has_more_results=has_more_results,
            cursor=cursor,
        )


        episode_list_response.additional_properties = d
        return episode_list_response

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
