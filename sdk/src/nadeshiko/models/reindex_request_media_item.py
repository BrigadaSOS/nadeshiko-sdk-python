from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ReindexRequestMediaItem")



@_attrs_define
class ReindexRequestMediaItem:
    """ 
        Attributes:
            media_id (int): The ID of the media Example: 5.
            episodes (list[int] | Unset): Optional array of episode numbers to reindex.
                If not provided, all episodes for this media will be reindexed. Example: [1, 3, 5].
     """

    media_id: int
    episodes: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        media_id = self.media_id

        episodes: list[int] | Unset = UNSET
        if not isinstance(self.episodes, Unset):
            episodes = self.episodes




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "mediaId": media_id,
        })
        if episodes is not UNSET:
            field_dict["episodes"] = episodes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        media_id = d.pop("mediaId")

        episodes = cast(list[int], d.pop("episodes", UNSET))


        reindex_request_media_item = cls(
            media_id=media_id,
            episodes=episodes,
        )


        reindex_request_media_item.additional_properties = d
        return reindex_request_media_item

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
