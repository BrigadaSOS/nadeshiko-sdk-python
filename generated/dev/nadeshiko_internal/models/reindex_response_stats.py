from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReindexResponseStats")


@_attrs_define
class ReindexResponseStats:
    """Statistics about the reindex operation

    Attributes:
        total_segments (int | Unset): Total number of segments processed
        successful_indexes (int | Unset): Number of segments successfully indexed
        failed_indexes (int | Unset): Number of segments that failed to index
        media_processed (int | Unset): Number of media items processed
    """

    total_segments: int | Unset = UNSET
    successful_indexes: int | Unset = UNSET
    failed_indexes: int | Unset = UNSET
    media_processed: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_segments = self.total_segments

        successful_indexes = self.successful_indexes

        failed_indexes = self.failed_indexes

        media_processed = self.media_processed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_segments is not UNSET:
            field_dict["totalSegments"] = total_segments
        if successful_indexes is not UNSET:
            field_dict["successfulIndexes"] = successful_indexes
        if failed_indexes is not UNSET:
            field_dict["failedIndexes"] = failed_indexes
        if media_processed is not UNSET:
            field_dict["mediaProcessed"] = media_processed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_segments = d.pop("totalSegments", UNSET)

        successful_indexes = d.pop("successfulIndexes", UNSET)

        failed_indexes = d.pop("failedIndexes", UNSET)

        media_processed = d.pop("mediaProcessed", UNSET)

        reindex_response_stats = cls(
            total_segments=total_segments,
            successful_indexes=successful_indexes,
            failed_indexes=failed_indexes,
            media_processed=media_processed,
        )

        reindex_response_stats.additional_properties = d
        return reindex_response_stats

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
