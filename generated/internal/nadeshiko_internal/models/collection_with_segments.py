from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.collection_with_segments_visibility import CollectionWithSegmentsVisibility

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
        visibility (CollectionWithSegmentsVisibility): Visibility of the collection Example: PRIVATE.
        segment_count (int): Number of segments in the collection Example: 42.
        created_at (datetime.datetime): When the collection was created
        updated_at (datetime.datetime | None): When the collection was last updated
        segments (list[CollectionWithSegmentsSegmentsItem]): Saved segments with their search result data
        includes (CollectionWithSegmentsIncludes):
        total_count (int): Total number of segments in the collection Example: 42.
        pagination (OpaqueCursorPagination): Opaque cursor pagination metadata
    """

    id: int
    name: str
    visibility: CollectionWithSegmentsVisibility
    segment_count: int
    created_at: datetime.datetime
    updated_at: datetime.datetime | None
    segments: list[CollectionWithSegmentsSegmentsItem]
    includes: CollectionWithSegmentsIncludes
    total_count: int
    pagination: OpaqueCursorPagination
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        visibility = self.visibility.value

        segment_count = self.segment_count

        created_at = self.created_at.isoformat()

        updated_at: None | str
        if isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        segments = []
        for segments_item_data in self.segments:
            segments_item = segments_item_data.to_dict()
            segments.append(segments_item)

        includes = self.includes.to_dict()

        total_count = self.total_count

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "visibility": visibility,
                "segmentCount": segment_count,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "segments": segments,
                "includes": includes,
                "totalCount": total_count,
                "pagination": pagination,
            }
        )

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

        visibility = CollectionWithSegmentsVisibility(d.pop("visibility"))

        segment_count = d.pop("segmentCount")

        created_at = isoparse(d.pop("createdAt"))

        def _parse_updated_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        updated_at = _parse_updated_at(d.pop("updatedAt"))

        segments = []
        _segments = d.pop("segments")
        for segments_item_data in _segments:
            segments_item = CollectionWithSegmentsSegmentsItem.from_dict(segments_item_data)

            segments.append(segments_item)

        includes = CollectionWithSegmentsIncludes.from_dict(d.pop("includes"))

        total_count = d.pop("totalCount")

        pagination = OpaqueCursorPagination.from_dict(d.pop("pagination"))

        collection_with_segments = cls(
            id=id,
            name=name,
            visibility=visibility,
            segment_count=segment_count,
            created_at=created_at,
            updated_at=updated_at,
            segments=segments,
            includes=includes,
            total_count=total_count,
            pagination=pagination,
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
