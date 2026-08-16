from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_familiar_media_response_200_familiar_media_item import (
        ListFamiliarMediaResponse200FamiliarMediaItem,
    )


T = TypeVar("T", bound="ListFamiliarMediaResponse200")


@_attrs_define
class ListFamiliarMediaResponse200:
    """
    Attributes:
        familiar_media (list[ListFamiliarMediaResponse200FamiliarMediaItem]):
    """

    familiar_media: list[ListFamiliarMediaResponse200FamiliarMediaItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        familiar_media = []
        for familiar_media_item_data in self.familiar_media:
            familiar_media_item = familiar_media_item_data.to_dict()
            familiar_media.append(familiar_media_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "familiarMedia": familiar_media,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_familiar_media_response_200_familiar_media_item import (
            ListFamiliarMediaResponse200FamiliarMediaItem,
        )

        _src = dict(src_dict)
        familiar_media = []
        _familiar_media = _src.pop("familiarMedia")
        for familiar_media_item_data in _familiar_media:
            familiar_media_item = ListFamiliarMediaResponse200FamiliarMediaItem.from_dict(
                familiar_media_item_data
            )

            familiar_media.append(familiar_media_item)

        list_familiar_media_response_200 = cls(
            familiar_media=familiar_media,
        )

        list_familiar_media_response_200.additional_properties = _src
        return list_familiar_media_response_200

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
