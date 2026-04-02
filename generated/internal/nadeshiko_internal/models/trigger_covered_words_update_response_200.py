from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TriggerCoveredWordsUpdateResponse200")


@_attrs_define
class TriggerCoveredWordsUpdateResponse200:
    """
    Attributes:
        words_checked (int):
        newly_covered (int):
        total_covered (int):
        percentage (float):
    """

    words_checked: int
    newly_covered: int
    total_covered: int
    percentage: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        words_checked = self.words_checked

        newly_covered = self.newly_covered

        total_covered = self.total_covered

        percentage = self.percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "wordsChecked": words_checked,
                "newlyCovered": newly_covered,
                "totalCovered": total_covered,
                "percentage": percentage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        words_checked = _src.pop("wordsChecked")

        newly_covered = _src.pop("newlyCovered")

        total_covered = _src.pop("totalCovered")

        percentage = _src.pop("percentage")

        trigger_covered_words_update_response_200 = cls(
            words_checked=words_checked,
            newly_covered=newly_covered,
            total_covered=total_covered,
            percentage=percentage,
        )

        trigger_covered_words_update_response_200.additional_properties = _src
        return trigger_covered_words_update_response_200

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
