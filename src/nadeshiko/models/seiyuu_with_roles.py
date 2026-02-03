from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.seiyuu_with_roles_roles_item import SeiyuuWithRolesRolesItem


T = TypeVar("T", bound="SeiyuuWithRoles")


@_attrs_define
class SeiyuuWithRoles:
    """Seiyuu with all voice acting roles

    Attributes:
        id (int): AniList staff ID Example: 95991.
        name_japanese (str): Japanese name of the voice actor Example: 阿部敦.
        name_english (str): English name of the voice actor Example: Atsushi Abe.
        image_url (str): Profile image URL Example: https://s4.anilist.co/file/anilistcdn/staff/large/n95991.jpg.
        roles (list[SeiyuuWithRolesRolesItem]): All characters voiced by this seiyuu with their media appearances
    """

    id: int
    name_japanese: str
    name_english: str
    image_url: str
    roles: list[SeiyuuWithRolesRolesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name_japanese = self.name_japanese

        name_english = self.name_english

        image_url = self.image_url

        roles = []
        for roles_item_data in self.roles:
            roles_item = roles_item_data.to_dict()
            roles.append(roles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "nameJapanese": name_japanese,
                "nameEnglish": name_english,
                "imageUrl": image_url,
                "roles": roles,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.seiyuu_with_roles_roles_item import SeiyuuWithRolesRolesItem

        d = dict(src_dict)
        id = d.pop("id")

        name_japanese = d.pop("nameJapanese")

        name_english = d.pop("nameEnglish")

        image_url = d.pop("imageUrl")

        roles = []
        _roles = d.pop("roles")
        for roles_item_data in _roles:
            roles_item = SeiyuuWithRolesRolesItem.from_dict(roles_item_data)

            roles.append(roles_item)

        seiyuu_with_roles = cls(
            id=id,
            name_japanese=name_japanese,
            name_english=name_english,
            image_url=image_url,
            roles=roles,
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
