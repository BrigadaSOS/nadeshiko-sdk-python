from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MediaFilterItem")


@_attrs_define
class MediaFilterItem:
    """A media filter entry with optional episode restriction

    Attributes:
        media_id (int): Media ID to filter Example: 123.
        episodes (list[int] | Unset): Specific episodes (omit for all episodes) Example: [1, 2].
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
        field_dict.update(
            {
                "mediaId": media_id,
            }
        )
        if episodes is not UNSET:
            field_dict["episodes"] = episodes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        media_id = d.pop("mediaId")

        episodes = cast(list[int], d.pop("episodes", UNSET))

        media_filter_item = cls(
            media_id=media_id,
            episodes=episodes,
        )

        media_filter_item.additional_properties = d
        return media_filter_item

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
