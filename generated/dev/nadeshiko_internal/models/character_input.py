from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.character_input_role import CharacterInputRole

T = TypeVar("T", bound="CharacterInput")


@_attrs_define
class CharacterInput:
    """Character data for creating/updating media

    Attributes:
        id (int): AniList character ID Example: 14545.
        name_ja (str): Japanese name of the character Example: 真城最高.
        name_en (str): English name of the character Example: Moritaka Mashiro.
        image_url (str): Character image URL Example: https://s4.anilist.co/file/anilistcdn/character/large/b14545.jpg.
        role (CharacterInputRole): Character's role in the media Example: MAIN.
        seiyuu_id (int): AniList staff ID for the Japanese voice actor Example: 95991.
        seiyuu_name_ja (str): Japanese name of the voice actor Example: 阿部敦.
        seiyuu_name_en (str): English name of the voice actor Example: Atsushi Abe.
        seiyuu_image_url (str): Voice actor profile image URL Example:
            https://s4.anilist.co/file/anilistcdn/staff/large/n95991.jpg.
    """

    id: int
    name_ja: str
    name_en: str
    image_url: str
    role: CharacterInputRole
    seiyuu_id: int
    seiyuu_name_ja: str
    seiyuu_name_en: str
    seiyuu_image_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name_ja = self.name_ja

        name_en = self.name_en

        image_url = self.image_url

        role = self.role.value

        seiyuu_id = self.seiyuu_id

        seiyuu_name_ja = self.seiyuu_name_ja

        seiyuu_name_en = self.seiyuu_name_en

        seiyuu_image_url = self.seiyuu_image_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "nameJa": name_ja,
                "nameEn": name_en,
                "imageUrl": image_url,
                "role": role,
                "seiyuuId": seiyuu_id,
                "seiyuuNameJa": seiyuu_name_ja,
                "seiyuuNameEn": seiyuu_name_en,
                "seiyuuImageUrl": seiyuu_image_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name_ja = d.pop("nameJa")

        name_en = d.pop("nameEn")

        image_url = d.pop("imageUrl")

        role = CharacterInputRole(d.pop("role"))

        seiyuu_id = d.pop("seiyuuId")

        seiyuu_name_ja = d.pop("seiyuuNameJa")

        seiyuu_name_en = d.pop("seiyuuNameEn")

        seiyuu_image_url = d.pop("seiyuuImageUrl")

        character_input = cls(
            id=id,
            name_ja=name_ja,
            name_en=name_en,
            image_url=image_url,
            role=role,
            seiyuu_id=seiyuu_id,
            seiyuu_name_ja=seiyuu_name_ja,
            seiyuu_name_en=seiyuu_name_en,
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
