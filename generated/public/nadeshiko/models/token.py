from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.token_kind import TokenKind, check_token_kind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.token_f_item import TokenFItem
    from ..models.token_inflection import TokenInflection
    from ..models.token_parts_item import TokenPartsItem


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
        pos_label (str | Unset): The part of speech in words, so a client needs no UniDic table. Example: Verb.
        pt (str | Unset): The short part-of-speech tag the dictionary lookup ranks by (`verb`, `prt`, `exp`), where `p`
            is UniDic's Japanese category and `posLabel` is the printable wording. A client resolving a word should send
            this rather than mapping `p` itself: the mapping is the parser's to make, and a category it grows that a hand-
            written table lacks would otherwise silently resolve to no tag at all. Empty for punctuation, symbols and
            whitespace, which are nothing to look up. Absent on anything parsed before it was stored.
             Example: verb.
        kind (TokenKind | Unset): How this token was grouped: a plain word, a compound, an inflected form, a counter, a
            function word, a merged grammatical expression, or a symbol.
             Example: inflected.
        f (list[TokenFItem] | Unset): Ruby, aligned to this surface: 食べました is 食(た) + べました, over the kanji and not the
            okurigana. Absent when there is none to show.
        inflection (TokenInflection | Unset): What this surface does to its dictionary form, outermost step first.
            Japanese stacks, so it is a chain rather than one name, and a step that is genuinely ambiguous says so
            ("potential / passive") instead of picking a side. Absent for anything that is not an inflected verb or
            adjective.
        parts (list[TokenPartsItem] | Unset): The finer morphemes inside a grouped token, positioned like their parent.
            Elasticsearch highlights with its own analyzer, so a match can land inside one of these tokens; these are the
            boundaries that let it render as a partial highlight. Absent when the token is already atomic.
    """

    s: str
    d: str
    r: str
    b: int
    e: int
    p: str
    pos_label: str | Unset = UNSET
    pt: str | Unset = UNSET
    kind: TokenKind | Unset = UNSET
    f: list[TokenFItem] | Unset = UNSET
    inflection: TokenInflection | Unset = UNSET
    parts: list[TokenPartsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        s = self.s

        d = self.d

        r = self.r

        b = self.b

        e = self.e

        p = self.p

        pos_label = self.pos_label

        pt = self.pt

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        f: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.f, Unset):
            f = []
            for f_item_data in self.f:
                f_item = f_item_data.to_dict()
                f.append(f_item)

        inflection: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inflection, Unset):
            inflection = self.inflection.to_dict()

        parts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parts, Unset):
            parts = []
            for parts_item_data in self.parts:
                parts_item = parts_item_data.to_dict()
                parts.append(parts_item)

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
        if pos_label is not UNSET:
            field_dict["posLabel"] = pos_label
        if pt is not UNSET:
            field_dict["pt"] = pt
        if kind is not UNSET:
            field_dict["kind"] = kind
        if f is not UNSET:
            field_dict["f"] = f
        if inflection is not UNSET:
            field_dict["inflection"] = inflection
        if parts is not UNSET:
            field_dict["parts"] = parts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.token_f_item import TokenFItem
        from ..models.token_inflection import TokenInflection
        from ..models.token_parts_item import TokenPartsItem

        _src = dict(src_dict)
        s = _src.pop("s")

        d = _src.pop("d")

        r = _src.pop("r")

        b = _src.pop("b")

        e = _src.pop("e")

        p = _src.pop("p")

        pos_label = _src.pop("posLabel", UNSET)

        pt = _src.pop("pt", UNSET)

        _kind = _src.pop("kind", UNSET)
        kind: TokenKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_token_kind(_kind)

        _f = _src.pop("f", UNSET)
        f: list[TokenFItem] | Unset = UNSET
        if _f is not UNSET:
            f = []
            for f_item_data in _f:
                f_item = TokenFItem.from_dict(f_item_data)

                f.append(f_item)

        _inflection = _src.pop("inflection", UNSET)
        inflection: TokenInflection | Unset
        if isinstance(_inflection, Unset):
            inflection = UNSET
        else:
            inflection = TokenInflection.from_dict(_inflection)

        _parts = _src.pop("parts", UNSET)
        parts: list[TokenPartsItem] | Unset = UNSET
        if _parts is not UNSET:
            parts = []
            for parts_item_data in _parts:
                parts_item = TokenPartsItem.from_dict(parts_item_data)

                parts.append(parts_item)

        token = cls(
            s=s,
            d=d,
            r=r,
            b=b,
            e=e,
            p=p,
            pos_label=pos_label,
            pt=pt,
            kind=kind,
            f=f,
            inflection=inflection,
            parts=parts,
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
