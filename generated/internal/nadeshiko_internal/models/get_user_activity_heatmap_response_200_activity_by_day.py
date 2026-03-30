from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.heatmap_day_counts import HeatmapDayCounts


T = TypeVar("T", bound="GetUserActivityHeatmapResponse200ActivityByDay")


@_attrs_define
class GetUserActivityHeatmapResponse200ActivityByDay:
    """Map of YYYY-MM-DD date strings to per-type activity counts"""

    additional_properties: dict[str, HeatmapDayCounts] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.heatmap_day_counts import HeatmapDayCounts

        _src = dict(src_dict)
        get_user_activity_heatmap_response_200_activity_by_day = cls()

        additional_properties = {}
        for prop_name, prop_dict in _src.items():
            additional_property = HeatmapDayCounts.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        get_user_activity_heatmap_response_200_activity_by_day.additional_properties = (
            additional_properties
        )
        return get_user_activity_heatmap_response_200_activity_by_day

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> HeatmapDayCounts:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: HeatmapDayCounts) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
