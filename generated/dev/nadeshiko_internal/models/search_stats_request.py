from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.category import Category
from ..models.search_stats_request_status_item import SearchStatsRequestStatusItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchStatsRequest")


@_attrs_define
class SearchStatsRequest:
    """
    Attributes:
        query (str | Unset): Text or sentence to search Example: 彼女.
        category (list[Category] | Unset): Media category filter
        exact_match (bool | Unset): Whether to use exact phrase matching Default: False.
        min_length (int | Unset): Minimum content length Example: 10.
        max_length (int | Unset): Maximum content length Example: 50.
        excluded_media_ids (list[int] | Unset): Media IDs to exclude from results
        media_ids (list[int] | Unset): Restrict stats to these media IDs (for list-scoped stats)
        status (list[SearchStatsRequestStatusItem] | Unset): Segment status filter
    """

    query: str | Unset = UNSET
    category: list[Category] | Unset = UNSET
    exact_match: bool | Unset = False
    min_length: int | Unset = UNSET
    max_length: int | Unset = UNSET
    excluded_media_ids: list[int] | Unset = UNSET
    media_ids: list[int] | Unset = UNSET
    status: list[SearchStatsRequestStatusItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        category: list[str] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = []
            for category_item_data in self.category:
                category_item = category_item_data.value
                category.append(category_item)

        exact_match = self.exact_match

        min_length = self.min_length

        max_length = self.max_length

        excluded_media_ids: list[int] | Unset = UNSET
        if not isinstance(self.excluded_media_ids, Unset):
            excluded_media_ids = self.excluded_media_ids

        media_ids: list[int] | Unset = UNSET
        if not isinstance(self.media_ids, Unset):
            media_ids = self.media_ids

        status: list[str] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = []
            for status_item_data in self.status:
                status_item = status_item_data.value
                status.append(status_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query is not UNSET:
            field_dict["query"] = query
        if category is not UNSET:
            field_dict["category"] = category
        if exact_match is not UNSET:
            field_dict["exactMatch"] = exact_match
        if min_length is not UNSET:
            field_dict["minLength"] = min_length
        if max_length is not UNSET:
            field_dict["maxLength"] = max_length
        if excluded_media_ids is not UNSET:
            field_dict["excludedMediaIds"] = excluded_media_ids
        if media_ids is not UNSET:
            field_dict["mediaIds"] = media_ids
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query", UNSET)

        _category = d.pop("category", UNSET)
        category: list[Category] | Unset = UNSET
        if _category is not UNSET:
            category = []
            for category_item_data in _category:
                category_item = Category(category_item_data)

                category.append(category_item)

        exact_match = d.pop("exactMatch", UNSET)

        min_length = d.pop("minLength", UNSET)

        max_length = d.pop("maxLength", UNSET)

        excluded_media_ids = cast(list[int], d.pop("excludedMediaIds", UNSET))

        media_ids = cast(list[int], d.pop("mediaIds", UNSET))

        _status = d.pop("status", UNSET)
        status: list[SearchStatsRequestStatusItem] | Unset = UNSET
        if _status is not UNSET:
            status = []
            for status_item_data in _status:
                status_item = SearchStatsRequestStatusItem(status_item_data)

                status.append(status_item)

        search_stats_request = cls(
            query=query,
            category=category,
            exact_match=exact_match,
            min_length=min_length,
            max_length=max_length,
            excluded_media_ids=excluded_media_ids,
            media_ids=media_ids,
            status=status,
        )

        search_stats_request.additional_properties = d
        return search_stats_request

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
