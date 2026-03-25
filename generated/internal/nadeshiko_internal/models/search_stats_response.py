from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.category_count import CategoryCount
    from ..models.media_search_stats import MediaSearchStats
    from ..models.search_stats_response_includes import SearchStatsResponseIncludes


T = TypeVar("T", bound="SearchStatsResponse")


@_attrs_define
class SearchStatsResponse:
    """
    Attributes:
        media (list[MediaSearchStats]):
        categories (list[CategoryCount]):
        includes (SearchStatsResponseIncludes):
    """

    media: list[MediaSearchStats]
    categories: list[CategoryCount]
    includes: SearchStatsResponseIncludes
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media = []
        for media_item_data in self.media:
            media_item = media_item_data.to_dict()
            media.append(media_item)

        categories = []
        for categories_item_data in self.categories:
            categories_item = categories_item_data.to_dict()
            categories.append(categories_item)

        includes = self.includes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "media": media,
                "categories": categories,
                "includes": includes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.category_count import CategoryCount
        from ..models.media_search_stats import MediaSearchStats
        from ..models.search_stats_response_includes import SearchStatsResponseIncludes

        _src = dict(src_dict)
        media = []
        _media = _src.pop("media")
        for media_item_data in _media:
            media_item = MediaSearchStats.from_dict(media_item_data)

            media.append(media_item)

        categories = []
        _categories = _src.pop("categories")
        for categories_item_data in _categories:
            categories_item = CategoryCount.from_dict(categories_item_data)

            categories.append(categories_item)

        includes = SearchStatsResponseIncludes.from_dict(_src.pop("includes"))

        search_stats_response = cls(
            media=media,
            categories=categories,
            includes=includes,
        )

        search_stats_response.additional_properties = _src
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
