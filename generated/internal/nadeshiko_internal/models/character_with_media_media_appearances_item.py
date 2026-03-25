from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.character_with_media_media_appearances_item_role import (
    CharacterWithMediaMediaAppearancesItemRole,
)

if TYPE_CHECKING:
    from ..models.media import Media


T = TypeVar("T", bound="CharacterWithMediaMediaAppearancesItem")


@_attrs_define
class CharacterWithMediaMediaAppearancesItem:
    """
    Attributes:
        media (Media): Media entry with full metadata
        role (CharacterWithMediaMediaAppearancesItemRole): Character role in this media Example: MAIN.
    """

    media: Media
    role: CharacterWithMediaMediaAppearancesItemRole
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media = self.media.to_dict()

        role = self.role.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "media": media,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media import Media

        _src = dict(src_dict)
        media = Media.from_dict(_src.pop("media"))

        role = CharacterWithMediaMediaAppearancesItemRole(_src.pop("role"))

        character_with_media_media_appearances_item = cls(
            media=media,
            role=role,
        )

        character_with_media_media_appearances_item.additional_properties = _src
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
