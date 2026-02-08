from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.media_character_role import MediaCharacterRole
from typing import cast

if TYPE_CHECKING:
  from ..models.character import Character





T = TypeVar("T", bound="MediaCharacter")



@_attrs_define
class MediaCharacter:
    """ Character appearing in a media with their role

        Attributes:
            character (Character): Anime character
            role (MediaCharacterRole): Character's role in the media Example: MAIN.
     """

    character: Character
    role: MediaCharacterRole
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.character import Character
        character = self.character.to_dict()

        role = self.role.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "character": character,
            "role": role,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.character import Character
        d = dict(src_dict)
        character = Character.from_dict(d.pop("character"))




        role = MediaCharacterRole(d.pop("role"))




        media_character = cls(
            character=character,
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
