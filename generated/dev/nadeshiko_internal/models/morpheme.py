from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Morpheme")


@_attrs_define
class Morpheme:
    """Morphological analysis token

    Attributes:
        surface (str): Surface form of the token as it appears in the text Example: 食べ.
        reading (str): Reading in katakana Example: タベ.
        baseform (str): Dictionary/base form of the word Example: 食べる.
        pronunciation (str): Pronunciation in katakana Example: タベル.
        pos (list[str]): Full part-of-speech tag array Example: ['動詞', '一般', '*', '*'].
        pos_short (str): Short part-of-speech label (first element of pos array) Example: 動詞.
        begin (int): Character offset where the token begins in the original text
        end (int): Character offset where the token ends in the original text Example: 2.
        pitch_accent_type (list[int] | None): Pitch accent type — mora position(s) where the pitch drops. 0 = heiban
            (flat), 1 = atamadaka, 2+ = nakadaka/odaka. Comma-separated in UniDic feature[24]. Null if not available.
             Example: [0].
        pitch_compound_rule (None | str): Compound accent connection rule from UniDic feature[25]. Values like C1-C5,
            F1-F6, P1-P13. Null if not available.
             Example: C2.
        pitch_modification_rule (None | str): Accent modification rule from UniDic feature[26]. Values like M1, M2, M4.
            Null if not available.
    """

    surface: str
    reading: str
    baseform: str
    pronunciation: str
    pos: list[str]
    pos_short: str
    begin: int
    end: int
    pitch_accent_type: list[int] | None
    pitch_compound_rule: None | str
    pitch_modification_rule: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        surface = self.surface

        reading = self.reading

        baseform = self.baseform

        pronunciation = self.pronunciation

        pos = self.pos

        pos_short = self.pos_short

        begin = self.begin

        end = self.end

        pitch_accent_type: list[int] | None
        if isinstance(self.pitch_accent_type, list):
            pitch_accent_type = self.pitch_accent_type

        else:
            pitch_accent_type = self.pitch_accent_type

        pitch_compound_rule: None | str
        pitch_compound_rule = self.pitch_compound_rule

        pitch_modification_rule: None | str
        pitch_modification_rule = self.pitch_modification_rule

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "surface": surface,
                "reading": reading,
                "baseform": baseform,
                "pronunciation": pronunciation,
                "pos": pos,
                "posShort": pos_short,
                "begin": begin,
                "end": end,
                "pitchAccentType": pitch_accent_type,
                "pitchCompoundRule": pitch_compound_rule,
                "pitchModificationRule": pitch_modification_rule,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        surface = d.pop("surface")

        reading = d.pop("reading")

        baseform = d.pop("baseform")

        pronunciation = d.pop("pronunciation")

        pos = cast(list[str], d.pop("pos"))

        pos_short = d.pop("posShort")

        begin = d.pop("begin")

        end = d.pop("end")

        def _parse_pitch_accent_type(data: object) -> list[int] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                pitch_accent_type_type_0 = cast(list[int], data)

                return pitch_accent_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None, data)

        pitch_accent_type = _parse_pitch_accent_type(d.pop("pitchAccentType"))

        def _parse_pitch_compound_rule(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        pitch_compound_rule = _parse_pitch_compound_rule(d.pop("pitchCompoundRule"))

        def _parse_pitch_modification_rule(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        pitch_modification_rule = _parse_pitch_modification_rule(d.pop("pitchModificationRule"))

        morpheme = cls(
            surface=surface,
            reading=reading,
            baseform=baseform,
            pronunciation=pronunciation,
            pos=pos,
            pos_short=pos_short,
            begin=begin,
            end=end,
            pitch_accent_type=pitch_accent_type,
            pitch_compound_rule=pitch_compound_rule,
            pitch_modification_rule=pitch_modification_rule,
        )

        morpheme.additional_properties = d
        return morpheme

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
