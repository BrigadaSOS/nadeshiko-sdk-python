from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserExportResponseMediaAffinityItem")


@_attrs_define
class UserExportResponseMediaAffinityItem:
    """
    Attributes:
        media_public_id (str):
        period_yyyymm (int): Year and month of the tally, as YYYYMM in UTC.
        anki_count (int):
        play_count (int):
        share_count (int):
    """

    media_public_id: str
    period_yyyymm: int
    anki_count: int
    play_count: int
    share_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media_public_id = self.media_public_id

        period_yyyymm = self.period_yyyymm

        anki_count = self.anki_count

        play_count = self.play_count

        share_count = self.share_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mediaPublicId": media_public_id,
                "periodYyyymm": period_yyyymm,
                "ankiCount": anki_count,
                "playCount": play_count,
                "shareCount": share_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        media_public_id = _src.pop("mediaPublicId")

        period_yyyymm = _src.pop("periodYyyymm")

        anki_count = _src.pop("ankiCount")

        play_count = _src.pop("playCount")

        share_count = _src.pop("shareCount")

        user_export_response_media_affinity_item = cls(
            media_public_id=media_public_id,
            period_yyyymm=period_yyyymm,
            anki_count=anki_count,
            play_count=play_count,
            share_count=share_count,
        )

        user_export_response_media_affinity_item.additional_properties = _src
        return user_export_response_media_affinity_item

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
