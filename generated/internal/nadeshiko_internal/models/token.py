from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

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
        p1 (None | str): POS subtype 1 (UniDic pos[1]) Example: 固有名詞.
        p2 (None | str): POS subtype 2 (UniDic pos[2]) Example: 人名.
        p4 (None | str): Conjugation type (UniDic pos[4]) Example: 五段-カ行.
        cf (None | str): Conjugation form (UniDic pos[5]) Example: 連用形-一般.
    """

    s: str
    d: str
    r: str
    b: int
    e: int
    p: str
    p1: None | str
    p2: None | str
    p4: None | str
    cf: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        s = self.s

        d = self.d

        r = self.r

        b = self.b

        e = self.e

        p = self.p

        p1: None | str
        p1 = self.p1

        p2: None | str
        p2 = self.p2

        p4: None | str
        p4 = self.p4

        cf: None | str
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
                "p1": p1,
                "p2": p2,
                "p4": p4,
                "cf": cf,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        s = _src.pop("s")

        d = _src.pop("d")

        r = _src.pop("r")

        b = _src.pop("b")

        e = _src.pop("e")

        p = _src.pop("p")

        def _parse_p1(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        p1 = _parse_p1(_src.pop("p1"))

        def _parse_p2(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        p2 = _parse_p2(_src.pop("p2"))

        def _parse_p4(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        p4 = _parse_p4(_src.pop("p4"))

        def _parse_cf(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cf = _parse_cf(_src.pop("cf"))

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

        token.additional_properties = _src
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
