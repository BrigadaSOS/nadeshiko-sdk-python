from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.search_multiple_response_includes_media import SearchMultipleResponseIncludesMedia


T = TypeVar("T", bound="SearchMultipleResponseIncludes")


@_attrs_define
class SearchMultipleResponseIncludes:
    """
    Attributes:
        media (SearchMultipleResponseIncludesMedia): Media objects keyed by mediaId
    """

    media: SearchMultipleResponseIncludesMedia
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media = self.media.to_dict()

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
        from ..models.search_multiple_response_includes_media import (
            SearchMultipleResponseIncludesMedia,
        )

        _src = dict(src_dict)
        media = SearchMultipleResponseIncludesMedia.from_dict(_src.pop("media"))

        search_multiple_response_includes = cls(
            media=media,
        )

        search_multiple_response_includes.additional_properties = _src
        return search_multiple_response_includes

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
