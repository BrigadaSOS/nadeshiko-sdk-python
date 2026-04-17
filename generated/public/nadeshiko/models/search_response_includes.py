from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_response_includes_media import SearchResponseIncludesMedia


T = TypeVar("T", bound="SearchResponseIncludes")


@_attrs_define
class SearchResponseIncludes:
    """Optional related resources requested via `include[]`

    Attributes:
        media (SearchResponseIncludesMedia | Unset): Media objects keyed by mediaPublicId. Present only when
            `include[]=media` is requested.
    """

    media: SearchResponseIncludesMedia | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media: dict[str, Any] | Unset = UNSET
        if not isinstance(self.media, Unset):
            media = self.media.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if media is not UNSET:
            field_dict["media"] = media

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_response_includes_media import SearchResponseIncludesMedia

        _src = dict(src_dict)
        _media = _src.pop("media", UNSET)
        media: SearchResponseIncludesMedia | Unset
        if isinstance(_media, Unset):
            media = UNSET
        else:
            media = SearchResponseIncludesMedia.from_dict(_media)

        search_response_includes = cls(
            media=media,
        )

        search_response_includes.additional_properties = _src
        return search_response_includes

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
