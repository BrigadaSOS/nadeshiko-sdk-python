from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.character_input_character_role import CharacterInputCharacterRole

T = TypeVar("T", bound="CharacterInput")


@_attrs_define
class CharacterInput:
    """Character data for creating/updating media

    Attributes:
        character_id (int): AniList character ID Example: 14545.
        character_name_japanese (str): Japanese name of the character Example: 真城最高.
        character_name_english (str): English name of the character Example: Moritaka Mashiro.
        character_image_url (str): Character image URL Example:
            https://s4.anilist.co/file/anilistcdn/character/large/b14545.jpg.
        character_role (CharacterInputCharacterRole): Character's role in the media Example: MAIN.
        seiyuu_id (int): AniList staff ID for the Japanese voice actor Example: 95991.
        seiyuu_name_japanese (str): Japanese name of the voice actor Example: 阿部敦.
        seiyuu_name_english (str): English name of the voice actor Example: Atsushi Abe.
        seiyuu_image_url (str): Voice actor profile image URL Example:
            https://s4.anilist.co/file/anilistcdn/staff/large/n95991.jpg.
    """

    character_id: int
    character_name_japanese: str
    character_name_english: str
    character_image_url: str
    character_role: CharacterInputCharacterRole
    seiyuu_id: int
    seiyuu_name_japanese: str
    seiyuu_name_english: str
    seiyuu_image_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        character_id = self.character_id

        character_name_japanese = self.character_name_japanese

        character_name_english = self.character_name_english

        character_image_url = self.character_image_url

        character_role = self.character_role.value

        seiyuu_id = self.seiyuu_id

        seiyuu_name_japanese = self.seiyuu_name_japanese

        seiyuu_name_english = self.seiyuu_name_english

        seiyuu_image_url = self.seiyuu_image_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "characterId": character_id,
                "characterNameJapanese": character_name_japanese,
                "characterNameEnglish": character_name_english,
                "characterImageUrl": character_image_url,
                "characterRole": character_role,
                "seiyuuId": seiyuu_id,
                "seiyuuNameJapanese": seiyuu_name_japanese,
                "seiyuuNameEnglish": seiyuu_name_english,
                "seiyuuImageUrl": seiyuu_image_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        character_id = d.pop("characterId")

        character_name_japanese = d.pop("characterNameJapanese")

        character_name_english = d.pop("characterNameEnglish")

        character_image_url = d.pop("characterImageUrl")

        character_role = CharacterInputCharacterRole(d.pop("characterRole"))

        seiyuu_id = d.pop("seiyuuId")

        seiyuu_name_japanese = d.pop("seiyuuNameJapanese")

        seiyuu_name_english = d.pop("seiyuuNameEnglish")

        seiyuu_image_url = d.pop("seiyuuImageUrl")

        character_input = cls(
            character_id=character_id,
            character_name_japanese=character_name_japanese,
            character_name_english=character_name_english,
            character_image_url=character_image_url,
            character_role=character_role,
            seiyuu_id=seiyuu_id,
            seiyuu_name_japanese=seiyuu_name_japanese,
            seiyuu_name_english=seiyuu_name_english,
            seiyuu_image_url=seiyuu_image_url,
        )

        character_input.additional_properties = d
        return character_input

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
