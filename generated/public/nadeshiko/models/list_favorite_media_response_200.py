from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.media_summary import MediaSummary


T = TypeVar("T", bound="ListFavoriteMediaResponse200")


@_attrs_define
class ListFavoriteMediaResponse200:
    """
    Attributes:
        favorite_media (list[MediaSummary]):
    """

    favorite_media: list[MediaSummary]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        favorite_media = []
        for favorite_media_item_data in self.favorite_media:
            favorite_media_item = favorite_media_item_data.to_dict()
            favorite_media.append(favorite_media_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "favoriteMedia": favorite_media,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_summary import MediaSummary

        _src = dict(src_dict)
        favorite_media = []
        _favorite_media = _src.pop("favoriteMedia")
        for favorite_media_item_data in _favorite_media:
            favorite_media_item = MediaSummary.from_dict(favorite_media_item_data)

            favorite_media.append(favorite_media_item)

        list_favorite_media_response_200 = cls(
            favorite_media=favorite_media,
        )

        list_favorite_media_response_200.additional_properties = _src
        return list_favorite_media_response_200

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
