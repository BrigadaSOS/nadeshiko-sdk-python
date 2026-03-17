from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.media_autocomplete_item import MediaAutocompleteItem


T = TypeVar("T", bound="MediaAutocompleteResponse")


@_attrs_define
class MediaAutocompleteResponse:
    """
    Attributes:
        media (list[MediaAutocompleteItem]):
    """

    media: list[MediaAutocompleteItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media = []
        for media_item_data in self.media:
            media_item = media_item_data.to_dict()
            media.append(media_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "media": media,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_autocomplete_item import MediaAutocompleteItem

        d = dict(src_dict)
        media = []
        _media = d.pop("media")
        for media_item_data in _media:
            media_item = MediaAutocompleteItem.from_dict(media_item_data)

            media.append(media_item)

        media_autocomplete_response = cls(
            media=media,
        )

        media_autocomplete_response.additional_properties = d
        return media_autocomplete_response

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
