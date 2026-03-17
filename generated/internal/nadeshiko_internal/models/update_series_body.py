from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateSeriesBody")


@_attrs_define
class UpdateSeriesBody:
    """
    Attributes:
        name_ja (str | Unset): Updated Japanese name Example: 更新バクマン。シリーズ.
        name_romaji (str | Unset): Updated Romaji name Example: Updated Bakuman. Series.
        name_en (str | Unset): Updated English name Example: Updated Bakuman Series.
    """

    name_ja: str | Unset = UNSET
    name_romaji: str | Unset = UNSET
    name_en: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name_ja = self.name_ja

        name_romaji = self.name_romaji

        name_en = self.name_en

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name_ja is not UNSET:
            field_dict["nameJa"] = name_ja
        if name_romaji is not UNSET:
            field_dict["nameRomaji"] = name_romaji
        if name_en is not UNSET:
            field_dict["nameEn"] = name_en

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name_ja = d.pop("nameJa", UNSET)

        name_romaji = d.pop("nameRomaji", UNSET)

        name_en = d.pop("nameEn", UNSET)

        update_series_body = cls(
            name_ja=name_ja,
            name_romaji=name_romaji,
            name_en=name_en,
        )

        update_series_body.additional_properties = d
        return update_series_body

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
