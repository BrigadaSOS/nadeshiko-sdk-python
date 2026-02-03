from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MediaInfoStats")


@_attrs_define
class MediaInfoStats:
    """Statistics about media and segments in the database

    Attributes:
        total_animes (int | Unset): Number of anime/media entries in the current result set Example: 15.
        total_segments (int | Unset): Number of subtitle segments in the current result set Example: 150.
        full_total_animes (int | Unset): Total number of anime/media entries in the entire database Example: 5234.
        full_total_segments (int | Unset): Total number of subtitle segments in the entire database Example: 1523847.
    """

    total_animes: int | Unset = UNSET
    total_segments: int | Unset = UNSET
    full_total_animes: int | Unset = UNSET
    full_total_segments: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_animes = self.total_animes

        total_segments = self.total_segments

        full_total_animes = self.full_total_animes

        full_total_segments = self.full_total_segments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_animes is not UNSET:
            field_dict["total_animes"] = total_animes
        if total_segments is not UNSET:
            field_dict["total_segments"] = total_segments
        if full_total_animes is not UNSET:
            field_dict["full_total_animes"] = full_total_animes
        if full_total_segments is not UNSET:
            field_dict["full_total_segments"] = full_total_segments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_animes = d.pop("total_animes", UNSET)

        total_segments = d.pop("total_segments", UNSET)

        full_total_animes = d.pop("full_total_animes", UNSET)

        full_total_segments = d.pop("full_total_segments", UNSET)

        media_info_stats = cls(
            total_animes=total_animes,
            total_segments=total_segments,
            full_total_animes=full_total_animes,
            full_total_segments=full_total_segments,
        )

        media_info_stats.additional_properties = d
        return media_info_stats

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
