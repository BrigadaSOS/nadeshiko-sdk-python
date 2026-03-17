from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reindex_request_media_item import ReindexRequestMediaItem


T = TypeVar("T", bound="ReindexRequest")


@_attrs_define
class ReindexRequest:
    """Request to reindex segments from the database into Elasticsearch

    Attributes:
        media (list[ReindexRequestMediaItem] | Unset): Array of media to reindex. If not provided, all media will be
            reindexed.
            Each media can optionally specify which episodes to reindex.
            If episodes are not specified for a media, all episodes will be reindexed. Example: [{'mediaId': 5, 'episodes':
            [1, 3]}, {'mediaId': 10}].
    """

    media: list[ReindexRequestMediaItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.media, Unset):
            media = []
            for media_item_data in self.media:
                media_item = media_item_data.to_dict()
                media.append(media_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if media is not UNSET:
            field_dict["media"] = media

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reindex_request_media_item import ReindexRequestMediaItem

        d = dict(src_dict)
        _media = d.pop("media", UNSET)
        media: list[ReindexRequestMediaItem] | Unset = UNSET
        if _media is not UNSET:
            media = []
            for media_item_data in _media:
                media_item = ReindexRequestMediaItem.from_dict(media_item_data)

                media.append(media_item)

        reindex_request = cls(
            media=media,
        )

        reindex_request.additional_properties = d
        return reindex_request

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
