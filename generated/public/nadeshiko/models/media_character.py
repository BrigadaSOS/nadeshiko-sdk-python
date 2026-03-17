from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.media_character_role import MediaCharacterRole

if TYPE_CHECKING:
    from ..models.seiyuu import Seiyuu


T = TypeVar("T", bound="MediaCharacter")


@_attrs_define
class MediaCharacter:
    """Character appearing in a media with their voice actor and role

    Attributes:
        id (int): AniList character ID Example: 14545.
        name_ja (str): Japanese name of the character Example: 真城最高.
        name_en (str): English name of the character Example: Moritaka Mashiro.
        image_url (str): Character image URL Example: https://s4.anilist.co/file/anilistcdn/character/large/b14545.jpg.
        seiyuu (Seiyuu): Japanese voice actor (seiyuu)
        role (MediaCharacterRole): Character's role in the media Example: MAIN.
    """

    id: int
    name_ja: str
    name_en: str
    image_url: str
    seiyuu: Seiyuu
    role: MediaCharacterRole
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name_ja = self.name_ja

        name_en = self.name_en

        image_url = self.image_url

        seiyuu = self.seiyuu.to_dict()

        role = self.role.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "nameJa": name_ja,
                "nameEn": name_en,
                "imageUrl": image_url,
                "seiyuu": seiyuu,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.seiyuu import Seiyuu

        d = dict(src_dict)
        id = d.pop("id")

        name_ja = d.pop("nameJa")

        name_en = d.pop("nameEn")

        image_url = d.pop("imageUrl")

        seiyuu = Seiyuu.from_dict(d.pop("seiyuu"))

        role = MediaCharacterRole(d.pop("role"))

        media_character = cls(
            id=id,
            name_ja=name_ja,
            name_en=name_en,
            image_url=image_url,
            seiyuu=seiyuu,
            role=role,
        )

        media_character.additional_properties = d
        return media_character

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
