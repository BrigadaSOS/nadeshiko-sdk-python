from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_pagination import SearchPagination
    from ..models.search_response_includes import SearchResponseIncludes
    from ..models.segment import Segment


T = TypeVar("T", bound="SearchResponse")


@_attrs_define
class SearchResponse:
    """
    Attributes:
        segments (list[Segment]):
        pagination (SearchPagination): Pagination metadata for search results
        includes (SearchResponseIncludes | Unset): Optional related resources requested via `include[]`
    """

    segments: list[Segment]
    pagination: SearchPagination
    includes: SearchResponseIncludes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        segments = []
        for segments_item_data in self.segments:
            segments_item = segments_item_data.to_dict()
            segments.append(segments_item)

        pagination = self.pagination.to_dict()

        includes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.includes, Unset):
            includes = self.includes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "segments": segments,
                "pagination": pagination,
            }
        )
        if includes is not UNSET:
            field_dict["includes"] = includes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_pagination import SearchPagination
        from ..models.search_response_includes import SearchResponseIncludes
        from ..models.segment import Segment

        _src = dict(src_dict)
        segments = []
        _segments = _src.pop("segments")
        for segments_item_data in _segments:
            segments_item = Segment.from_dict(segments_item_data)

            segments.append(segments_item)

        pagination = SearchPagination.from_dict(_src.pop("pagination"))

        _includes = _src.pop("includes", UNSET)
        includes: SearchResponseIncludes | Unset
        if isinstance(_includes, Unset):
            includes = UNSET
        else:
            includes = SearchResponseIncludes.from_dict(_includes)

        search_response = cls(
            segments=segments,
            pagination=pagination,
            includes=includes,
        )

        search_response.additional_properties = _src
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
