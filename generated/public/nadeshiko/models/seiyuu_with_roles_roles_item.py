from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.seiyuu_with_roles_roles_item_role import SeiyuuWithRolesRolesItemRole
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.character import Character
  from ..models.media import Media





T = TypeVar("T", bound="SeiyuuWithRolesRolesItem")



@_attrs_define
class SeiyuuWithRolesRolesItem:
    """ 
        Attributes:
            character (Character | Unset): Anime character
            media (Media | Unset): Media entry with full metadata
            role (SeiyuuWithRolesRolesItemRole | Unset): Character role in this media Example: MAIN.
     """

    character: Character | Unset = UNSET
    media: Media | Unset = UNSET
    role: SeiyuuWithRolesRolesItemRole | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.media import Media
        from ..models.character import Character
        character: dict[str, Any] | Unset = UNSET
        if not isinstance(self.character, Unset):
            character = self.character.to_dict()

        media: dict[str, Any] | Unset = UNSET
        if not isinstance(self.media, Unset):
            media = self.media.to_dict()

        role: str | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if character is not UNSET:
            field_dict["character"] = character
        if media is not UNSET:
            field_dict["media"] = media
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.character import Character
        from ..models.media import Media
        d = dict(src_dict)
        _character = d.pop("character", UNSET)
        character: Character | Unset
        if isinstance(_character,  Unset):
            character = UNSET
        else:
            character = Character.from_dict(_character)




        _media = d.pop("media", UNSET)
        media: Media | Unset
        if isinstance(_media,  Unset):
            media = UNSET
        else:
            media = Media.from_dict(_media)




        _role = d.pop("role", UNSET)
        role: SeiyuuWithRolesRolesItemRole | Unset
        if isinstance(_role,  Unset):
            role = UNSET
        else:
            role = SeiyuuWithRolesRolesItemRole(_role)




        seiyuu_with_roles_roles_item = cls(
            character=character,
            media=media,
            role=role,
        )


        seiyuu_with_roles_roles_item.additional_properties = d
        return seiyuu_with_roles_roles_item

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
