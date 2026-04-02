from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WordCoverageTier")


@_attrs_define
class WordCoverageTier:
    """Coverage statistics for a frequency tier

    Attributes:
        tier (int): The frequency tier (e.g. 1000 means top 1000 words) Example: 5000.
        covered (int): Number of words with at least one match in the corpus Example: 4823.
        total (int): Total number of words in this tier Example: 5000.
        percentage (float): Coverage percentage Example: 96.5.
    """

    tier: int
    covered: int
    total: int
    percentage: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tier = self.tier

        covered = self.covered

        total = self.total

        percentage = self.percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tier": tier,
                "covered": covered,
                "total": total,
                "percentage": percentage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        tier = _src.pop("tier")

        covered = _src.pop("covered")

        total = _src.pop("total")

        percentage = _src.pop("percentage")

        word_coverage_tier = cls(
            tier=tier,
            covered=covered,
            total=total,
            percentage=percentage,
        )

        word_coverage_tier.additional_properties = _src
        return word_coverage_tier

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
