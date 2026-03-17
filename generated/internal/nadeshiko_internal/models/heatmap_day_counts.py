from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HeatmapDayCounts")


@_attrs_define
class HeatmapDayCounts:
    """Activity counts for a single day, broken down by type. Only types with at least 1 event are present.

    Attributes:
        search (int | Unset):
        segment_play (int | Unset):
        anki_export (int | Unset):
        share (int | Unset):
    """

    search: int | Unset = UNSET
    segment_play: int | Unset = UNSET
    anki_export: int | Unset = UNSET
    share: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        search = self.search

        segment_play = self.segment_play

        anki_export = self.anki_export

        share = self.share

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if search is not UNSET:
            field_dict["SEARCH"] = search
        if segment_play is not UNSET:
            field_dict["SEGMENT_PLAY"] = segment_play
        if anki_export is not UNSET:
            field_dict["ANKI_EXPORT"] = anki_export
        if share is not UNSET:
            field_dict["SHARE"] = share

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        search = d.pop("SEARCH", UNSET)

        segment_play = d.pop("SEGMENT_PLAY", UNSET)

        anki_export = d.pop("ANKI_EXPORT", UNSET)

        share = d.pop("SHARE", UNSET)

        heatmap_day_counts = cls(
            search=search,
            segment_play=segment_play,
            anki_export=anki_export,
            share=share,
        )

        heatmap_day_counts.additional_properties = d
        return heatmap_day_counts

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
