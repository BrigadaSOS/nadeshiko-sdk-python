from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetStatsOverviewResponse200Translations")


@_attrs_define
class GetStatsOverviewResponse200Translations:
    """
    Attributes:
        total (int): Total active segments Example: 1200000.
        en_human (int): Segments with human English translations Example: 800000.
        en_machine (int): Segments with machine English translations Example: 350000.
        es_human (int): Segments with human Spanish translations Example: 200000.
        es_machine (int): Segments with machine Spanish translations Example: 400000.
    """

    total: int
    en_human: int
    en_machine: int
    es_human: int
    es_machine: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        en_human = self.en_human

        en_machine = self.en_machine

        es_human = self.es_human

        es_machine = self.es_machine

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "enHuman": en_human,
                "enMachine": en_machine,
                "esHuman": es_human,
                "esMachine": es_machine,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        total = _src.pop("total")

        en_human = _src.pop("enHuman")

        en_machine = _src.pop("enMachine")

        es_human = _src.pop("esHuman")

        es_machine = _src.pop("esMachine")

        get_stats_overview_response_200_translations = cls(
            total=total,
            en_human=en_human,
            en_machine=en_machine,
            es_human=es_human,
            es_machine=es_machine,
        )

        get_stats_overview_response_200_translations.additional_properties = _src
        return get_stats_overview_response_200_translations

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
