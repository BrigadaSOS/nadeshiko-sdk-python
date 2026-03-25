from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReindexResponseStats")


@_attrs_define
class ReindexResponseStats:
    """Statistics about the reindex operation

    Attributes:
        total_segments (int): Total number of segments processed
        successful_indexes (int): Number of segments successfully indexed
        failed_indexes (int): Number of segments that failed to index
        media_processed (int): Number of media items processed
    """

    total_segments: int
    successful_indexes: int
    failed_indexes: int
    media_processed: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_segments = self.total_segments

        successful_indexes = self.successful_indexes

        failed_indexes = self.failed_indexes

        media_processed = self.media_processed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalSegments": total_segments,
                "successfulIndexes": successful_indexes,
                "failedIndexes": failed_indexes,
                "mediaProcessed": media_processed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        total_segments = _src.pop("totalSegments")

        successful_indexes = _src.pop("successfulIndexes")

        failed_indexes = _src.pop("failedIndexes")

        media_processed = _src.pop("mediaProcessed")

        reindex_response_stats = cls(
            total_segments=total_segments,
            successful_indexes=successful_indexes,
            failed_indexes=failed_indexes,
            media_processed=media_processed,
        )

        reindex_response_stats.additional_properties = _src
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
