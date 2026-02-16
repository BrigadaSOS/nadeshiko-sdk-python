from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.character_with_media_media_appearances_item_role import (
    CharacterWithMediaMediaAppearancesItemRole,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media import Media


T = TypeVar("T", bound="CharacterWithMediaMediaAppearancesItem")


@_attrs_define
class CharacterWithMediaMediaAppearancesItem:
    """
    Attributes:
        media (Media | Unset): Media entry with full metadata
        role (CharacterWithMediaMediaAppearancesItemRole | Unset): Character role in this media Example: MAIN.
    """

    media: Media | Unset = UNSET
    role: CharacterWithMediaMediaAppearancesItemRole | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media: dict[str, Any] | Unset = UNSET
        if not isinstance(self.media, Unset):
            media = self.media.to_dict()

        role: str | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if media is not UNSET:
            field_dict["media"] = media
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media import Media

        d = dict(src_dict)
        _media = d.pop("media", UNSET)
        media: Media | Unset
        if isinstance(_media, Unset):
            media = UNSET
        else:
            media = Media.from_dict(_media)

        _role = d.pop("role", UNSET)
        role: CharacterWithMediaMediaAppearancesItemRole | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = CharacterWithMediaMediaAppearancesItemRole(_role)

        character_with_media_media_appearances_item = cls(
            media=media,
            role=role,
        )

        character_with_media_media_appearances_item.additional_properties = d
        return character_with_media_media_appearances_item

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
