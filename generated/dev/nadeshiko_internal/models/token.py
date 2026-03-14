from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

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
        p1 (str | Unset): POS subtype 1 (UniDic pos[1]) Example: 固有名詞.
        p2 (str | Unset): POS subtype 2 (UniDic pos[2]) Example: 人名.
        p4 (str | Unset): Conjugation type (UniDic pos[4]) Example: 五段-カ行.
        cf (str | Unset): Conjugation form (UniDic pos[5]) Example: 連用形-一般.
    """

    s: str
    d: str
    r: str
    b: int
    e: int
    p: str
    p1: str | Unset = UNSET
    p2: str | Unset = UNSET
    p4: str | Unset = UNSET
    cf: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        s = self.s

        d = self.d

        r = self.r

        b = self.b

        e = self.e

        p = self.p

        p1 = self.p1

        p2 = self.p2

        p4 = self.p4

        cf = self.cf

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
        if p1 is not UNSET:
            field_dict["p1"] = p1
        if p2 is not UNSET:
            field_dict["p2"] = p2
        if p4 is not UNSET:
            field_dict["p4"] = p4
        if cf is not UNSET:
            field_dict["cf"] = cf

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

        p1 = d.pop("p1", UNSET)

        p2 = d.pop("p2", UNSET)

        p4 = d.pop("p4", UNSET)

        cf = d.pop("cf", UNSET)

        token = cls(
            s=s,
            d=d,
            r=r,
            b=b,
            e=e,
            p=p,
            p1=p1,
            p2=p2,
            p4=p4,
            cf=cf,
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
