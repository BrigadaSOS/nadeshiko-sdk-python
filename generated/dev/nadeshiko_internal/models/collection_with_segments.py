from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.collection_with_segments_visibility import CollectionWithSegmentsVisibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.collection_with_segments_includes import CollectionWithSegmentsIncludes
    from ..models.collection_with_segments_segments_item import CollectionWithSegmentsSegmentsItem
    from ..models.opaque_cursor_pagination import OpaqueCursorPagination


T = TypeVar("T", bound="CollectionWithSegments")


@_attrs_define
class CollectionWithSegments:
    """Collection with saved segments (search result format)

    Attributes:
        id (int): Collection ID Example: 123.
        name (str): Name of the collection Example: Study Favorites.
        user_id (int): User ID who owns the collection Example: 1.
        visibility (CollectionWithSegmentsVisibility): Visibility of the collection Example: PRIVATE.
        segments (list[CollectionWithSegmentsSegmentsItem]): Saved segments with their search result data
        total_count (int): Total number of segments in the collection Example: 42.
        pagination (OpaqueCursorPagination): Opaque cursor pagination metadata
        includes (CollectionWithSegmentsIncludes | Unset):
    """

    id: int
    name: str
    user_id: int
    visibility: CollectionWithSegmentsVisibility
    segments: list[CollectionWithSegmentsSegmentsItem]
    total_count: int
    pagination: OpaqueCursorPagination
    includes: CollectionWithSegmentsIncludes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        user_id = self.user_id

        visibility = self.visibility.value

        segments = []
        for segments_item_data in self.segments:
            segments_item = segments_item_data.to_dict()
            segments.append(segments_item)

        total_count = self.total_count

        pagination = self.pagination.to_dict()

        includes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.includes, Unset):
            includes = self.includes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "userId": user_id,
                "visibility": visibility,
                "segments": segments,
                "totalCount": total_count,
                "pagination": pagination,
            }
        )
        if includes is not UNSET:
            field_dict["includes"] = includes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.collection_with_segments_includes import CollectionWithSegmentsIncludes
        from ..models.collection_with_segments_segments_item import (
            CollectionWithSegmentsSegmentsItem,
        )
        from ..models.opaque_cursor_pagination import OpaqueCursorPagination

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        user_id = d.pop("userId")

        visibility = CollectionWithSegmentsVisibility(d.pop("visibility"))

        segments = []
        _segments = d.pop("segments")
        for segments_item_data in _segments:
            segments_item = CollectionWithSegmentsSegmentsItem.from_dict(segments_item_data)

            segments.append(segments_item)

        total_count = d.pop("totalCount")

        pagination = OpaqueCursorPagination.from_dict(d.pop("pagination"))

        _includes = d.pop("includes", UNSET)
        includes: CollectionWithSegmentsIncludes | Unset
        if isinstance(_includes, Unset):
            includes = UNSET
        else:
            includes = CollectionWithSegmentsIncludes.from_dict(_includes)

        collection_with_segments = cls(
            id=id,
            name=name,
            user_id=user_id,
            visibility=visibility,
            segments=segments,
            total_count=total_count,
            pagination=pagination,
            includes=includes,
        )

        collection_with_segments.additional_properties = d
        return collection_with_segments

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
