from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category_count import CategoryCount
    from ..models.media_search_stats import MediaSearchStats
    from ..models.search_stats_response_includes import SearchStatsResponseIncludes


T = TypeVar("T", bound="SearchStatsResponse")


@_attrs_define
class SearchStatsResponse:
    """
    Attributes:
        media (list[MediaSearchStats] | Unset):
        categories (list[CategoryCount] | Unset):
        includes (SearchStatsResponseIncludes | Unset):
    """

    media: list[MediaSearchStats] | Unset = UNSET
    categories: list[CategoryCount] | Unset = UNSET
    includes: SearchStatsResponseIncludes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.media, Unset):
            media = []
            for media_item_data in self.media:
                media_item = media_item_data.to_dict()
                media.append(media_item)

        categories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()
                categories.append(categories_item)

        includes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.includes, Unset):
            includes = self.includes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if media is not UNSET:
            field_dict["media"] = media
        if categories is not UNSET:
            field_dict["categories"] = categories
        if includes is not UNSET:
            field_dict["includes"] = includes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.category_count import CategoryCount
        from ..models.media_search_stats import MediaSearchStats
        from ..models.search_stats_response_includes import SearchStatsResponseIncludes

        d = dict(src_dict)
        _media = d.pop("media", UNSET)
        media: list[MediaSearchStats] | Unset = UNSET
        if _media is not UNSET:
            media = []
            for media_item_data in _media:
                media_item = MediaSearchStats.from_dict(media_item_data)

                media.append(media_item)

        _categories = d.pop("categories", UNSET)
        categories: list[CategoryCount] | Unset = UNSET
        if _categories is not UNSET:
            categories = []
            for categories_item_data in _categories:
                categories_item = CategoryCount.from_dict(categories_item_data)

                categories.append(categories_item)

        _includes = d.pop("includes", UNSET)
        includes: SearchStatsResponseIncludes | Unset
        if isinstance(_includes, Unset):
            includes = UNSET
        else:
            includes = SearchStatsResponseIncludes.from_dict(_includes)

        search_stats_response = cls(
            media=media,
            categories=categories,
            includes=includes,
        )

        search_stats_response.additional_properties = d
        return search_stats_response

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
