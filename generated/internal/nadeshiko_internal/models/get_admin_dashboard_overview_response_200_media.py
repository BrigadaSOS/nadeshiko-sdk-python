from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetAdminDashboardOverviewResponse200Media")


@_attrs_define
class GetAdminDashboardOverviewResponse200Media:
    """
    Attributes:
        total_media (int):
        total_episodes (int):
        total_segments (int):
        total_characters (int):
        total_seiyuu (int):
    """

    total_media: int
    total_episodes: int
    total_segments: int
    total_characters: int
    total_seiyuu: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_media = self.total_media

        total_episodes = self.total_episodes

        total_segments = self.total_segments

        total_characters = self.total_characters

        total_seiyuu = self.total_seiyuu

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalMedia": total_media,
                "totalEpisodes": total_episodes,
                "totalSegments": total_segments,
                "totalCharacters": total_characters,
                "totalSeiyuu": total_seiyuu,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        total_media = _src.pop("totalMedia")

        total_episodes = _src.pop("totalEpisodes")

        total_segments = _src.pop("totalSegments")

        total_characters = _src.pop("totalCharacters")

        total_seiyuu = _src.pop("totalSeiyuu")

        get_admin_dashboard_overview_response_200_media = cls(
            total_media=total_media,
            total_episodes=total_episodes,
            total_segments=total_segments,
            total_characters=total_characters,
            total_seiyuu=total_seiyuu,
        )

        get_admin_dashboard_overview_response_200_media.additional_properties = _src
        return get_admin_dashboard_overview_response_200_media

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
