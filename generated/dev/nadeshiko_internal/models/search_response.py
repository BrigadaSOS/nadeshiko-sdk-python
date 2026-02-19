from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pagination_info import PaginationInfo
    from ..models.search_response_includes import SearchResponseIncludes
    from ..models.segment import Segment


T = TypeVar("T", bound="SearchResponse")


@_attrs_define
class SearchResponse:
    """
    Attributes:
        segments (list[Segment] | Unset):
        includes (SearchResponseIncludes | Unset):
        pagination (PaginationInfo | Unset): Pagination metadata for search results
    """

    segments: list[Segment] | Unset = UNSET
    includes: SearchResponseIncludes | Unset = UNSET
    pagination: PaginationInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        segments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.segments, Unset):
            segments = []
            for segments_item_data in self.segments:
                segments_item = segments_item_data.to_dict()
                segments.append(segments_item)

        includes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.includes, Unset):
            includes = self.includes.to_dict()

        pagination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if segments is not UNSET:
            field_dict["segments"] = segments
        if includes is not UNSET:
            field_dict["includes"] = includes
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination_info import PaginationInfo
        from ..models.search_response_includes import SearchResponseIncludes
        from ..models.segment import Segment

        d = dict(src_dict)
        _segments = d.pop("segments", UNSET)
        segments: list[Segment] | Unset = UNSET
        if _segments is not UNSET:
            segments = []
            for segments_item_data in _segments:
                segments_item = Segment.from_dict(segments_item_data)

                segments.append(segments_item)

        _includes = d.pop("includes", UNSET)
        includes: SearchResponseIncludes | Unset
        if isinstance(_includes, Unset):
            includes = UNSET
        else:
            includes = SearchResponseIncludes.from_dict(_includes)

        _pagination = d.pop("pagination", UNSET)
        pagination: PaginationInfo | Unset
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = PaginationInfo.from_dict(_pagination)

        search_response = cls(
            segments=segments,
            includes=includes,
            pagination=pagination,
        )

        search_response.additional_properties = d
        return search_response

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
