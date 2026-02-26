from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.media import Media


T = TypeVar("T", bound="SeriesWithMediaMediaItem")


@_attrs_define
class SeriesWithMediaMediaItem:
    """
    Attributes:
        position (int): Position in the series (1-indexed) Example: 1.
        media (Media): Media entry with full metadata
    """

    position: int
    media: Media
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        position = self.position

        media = self.media.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position": position,
                "media": media,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media import Media

        d = dict(src_dict)
        position = d.pop("position")

        media = Media.from_dict(d.pop("media"))

        series_with_media_media_item = cls(
            position=position,
            media=media,
        )

        series_with_media_media_item.additional_properties = d
        return series_with_media_media_item

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
