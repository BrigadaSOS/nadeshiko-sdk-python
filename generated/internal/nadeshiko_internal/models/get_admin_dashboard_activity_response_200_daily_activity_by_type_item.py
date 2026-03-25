from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetAdminDashboardActivityResponse200DailyActivityByTypeItem")


@_attrs_define
class GetAdminDashboardActivityResponse200DailyActivityByTypeItem:
    """
    Attributes:
        date (str):
        search (int):
        anki_export (int):
        segment_play (int):
        share (int):
    """

    date: str
    search: int
    anki_export: int
    segment_play: int
    share: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        search = self.search

        anki_export = self.anki_export

        segment_play = self.segment_play

        share = self.share

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "search": search,
                "ankiExport": anki_export,
                "segmentPlay": segment_play,
                "share": share,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        date = _src.pop("date")

        search = _src.pop("search")

        anki_export = _src.pop("ankiExport")

        segment_play = _src.pop("segmentPlay")

        share = _src.pop("share")

        get_admin_dashboard_activity_response_200_daily_activity_by_type_item = cls(
            date=date,
            search=search,
            anki_export=anki_export,
            segment_play=segment_play,
            share=share,
        )

        get_admin_dashboard_activity_response_200_daily_activity_by_type_item.additional_properties = _src
        return get_admin_dashboard_activity_response_200_daily_activity_by_type_item

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
