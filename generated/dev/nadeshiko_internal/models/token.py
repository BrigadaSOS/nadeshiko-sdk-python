from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Token")


@_attrs_define
class Token:
    """Morphological token from Japanese text analysis

    Attributes:
        s (str): Surface form (the text as it appears in the sentence) Example: 食べ.
        d (str): Dictionary form (base/lemma form for search) Example: 食べる.
        r (str): Reading in katakana Example: タベ.
        b (int): Begin character offset in textJa.content Example: 3.
        e (int): End character offset in textJa.content Example: 5.
        p (str): Primary part-of-speech tag Example: 動詞.
    """

    s: str
    d: str
    r: str
    b: int
    e: int
    p: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        s = self.s

        d = self.d

        r = self.r

        b = self.b

        e = self.e

        p = self.p

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "s": s,
                "d": d,
                "r": r,
                "b": b,
                "e": e,
                "p": p,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        s = d.pop("s")

        d = d.pop("d")

        r = d.pop("r")

        b = d.pop("b")

        e = d.pop("e")

        p = d.pop("p")

        token = cls(
            s=s,
            d=d,
            r=r,
            b=b,
            e=e,
            p=p,
        )

        token.additional_properties = d
        return token

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
