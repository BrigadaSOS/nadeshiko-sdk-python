from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TokenInflection")


@_attrs_define
class TokenInflection:
    """What this surface does to its dictionary form, outermost step first. Japanese stacks, so it is a chain rather than
    one name, and a step that is genuinely ambiguous says so ("potential / passive") instead of picking a side. Absent
    for anything that is not an inflected verb or adjective.

        Attributes:
            labels (list[str]):  Example: ['past', 'polite'].
            base (str):  Example: 食べる.
    """

    labels: list[str]
    base: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        labels = self.labels

        base = self.base

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "labels": labels,
                "base": base,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        labels = cast(list[str], _src.pop("labels"))

        base = _src.pop("base")

        token_inflection = cls(
            labels=labels,
            base=base,
        )

        token_inflection.additional_properties = _src
        return token_inflection

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
