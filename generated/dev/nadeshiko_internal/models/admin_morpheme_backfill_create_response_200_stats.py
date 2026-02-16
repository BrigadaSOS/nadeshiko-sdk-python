from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AdminMorphemeBackfillCreateResponse200Stats")


@_attrs_define
class AdminMorphemeBackfillCreateResponse200Stats:
    """
    Attributes:
        total_segments (int):
        successful_analyses (int):
        failed_analyses (int):
    """

    total_segments: int
    successful_analyses: int
    failed_analyses: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_segments = self.total_segments

        successful_analyses = self.successful_analyses

        failed_analyses = self.failed_analyses

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalSegments": total_segments,
                "successfulAnalyses": successful_analyses,
                "failedAnalyses": failed_analyses,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_segments = d.pop("totalSegments")

        successful_analyses = d.pop("successfulAnalyses")

        failed_analyses = d.pop("failedAnalyses")

        admin_morpheme_backfill_create_response_200_stats = cls(
            total_segments=total_segments,
            successful_analyses=successful_analyses,
            failed_analyses=failed_analyses,
        )

        admin_morpheme_backfill_create_response_200_stats.additional_properties = d
        return admin_morpheme_backfill_create_response_200_stats

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
