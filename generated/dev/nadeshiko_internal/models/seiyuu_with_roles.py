from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.seiyuu_with_roles_characters_item import SeiyuuWithRolesCharactersItem


T = TypeVar("T", bound="SeiyuuWithRoles")


@_attrs_define
class SeiyuuWithRoles:
    """Seiyuu details with optional character appearances

    Attributes:
        id (int): AniList staff ID Example: 95991.
        name_ja (str): Japanese name of the voice actor Example: 阿部敦.
        name_en (str): English name of the voice actor Example: Atsushi Abe.
        image_url (str): Profile image URL Example: https://s4.anilist.co/file/anilistcdn/staff/large/n95991.jpg.
        characters (list[SeiyuuWithRolesCharactersItem]): Characters voiced by this seiyuu with their media appearances
    """

    id: int
    name_ja: str
    name_en: str
    image_url: str
    characters: list[SeiyuuWithRolesCharactersItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name_ja = self.name_ja

        name_en = self.name_en

        image_url = self.image_url

        characters = []
        for characters_item_data in self.characters:
            characters_item = characters_item_data.to_dict()
            characters.append(characters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "nameJa": name_ja,
                "nameEn": name_en,
                "imageUrl": image_url,
                "characters": characters,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.seiyuu_with_roles_characters_item import SeiyuuWithRolesCharactersItem

        d = dict(src_dict)
        id = d.pop("id")

        name_ja = d.pop("nameJa")

        name_en = d.pop("nameEn")

        image_url = d.pop("imageUrl")

        characters = []
        _characters = d.pop("characters")
        for characters_item_data in _characters:
            characters_item = SeiyuuWithRolesCharactersItem.from_dict(characters_item_data)

            characters.append(characters_item)

        seiyuu_with_roles = cls(
            id=id,
            name_ja=name_ja,
            name_en=name_en,
            image_url=image_url,
            characters=characters,
        )

        seiyuu_with_roles.additional_properties = d
        return seiyuu_with_roles

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
