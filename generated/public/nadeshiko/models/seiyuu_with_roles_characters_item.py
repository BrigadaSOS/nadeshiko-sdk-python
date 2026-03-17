from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.seiyuu_with_roles_characters_item_role import SeiyuuWithRolesCharactersItemRole

if TYPE_CHECKING:
    from ..models.external_id import ExternalId
    from ..models.media import Media


T = TypeVar("T", bound="SeiyuuWithRolesCharactersItem")


@_attrs_define
class SeiyuuWithRolesCharactersItem:
    """
    Attributes:
        id (int): Internal character ID Example: 1.
        public_id (str): Public identifier for the character (use this in public URLs) Example: V1StGXR8_Z5d.
        external_ids (ExternalId): Map of external IDs keyed by source. Only sources with values are included.
        name_ja (str): Japanese name of the character Example: 真城最高.
        name_en (str): English name of the character Example: Moritaka Mashiro.
        image_url (str): Character image URL Example: https://s4.anilist.co/file/anilistcdn/character/large/b14545.jpg.
        media (Media): Media entry with full metadata
        role (SeiyuuWithRolesCharactersItemRole): Character role in this media Example: MAIN.
    """

    id: int
    public_id: str
    external_ids: ExternalId
    name_ja: str
    name_en: str
    image_url: str
    media: Media
    role: SeiyuuWithRolesCharactersItemRole
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        public_id = self.public_id

        external_ids = self.external_ids.to_dict()

        name_ja = self.name_ja

        name_en = self.name_en

        image_url = self.image_url

        media = self.media.to_dict()

        role = self.role.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "publicId": public_id,
                "externalIds": external_ids,
                "nameJa": name_ja,
                "nameEn": name_en,
                "imageUrl": image_url,
                "media": media,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.external_id import ExternalId
        from ..models.media import Media

        d = dict(src_dict)
        id = d.pop("id")

        public_id = d.pop("publicId")

        external_ids = ExternalId.from_dict(d.pop("externalIds"))

        name_ja = d.pop("nameJa")

        name_en = d.pop("nameEn")

        image_url = d.pop("imageUrl")

        media = Media.from_dict(d.pop("media"))

        role = SeiyuuWithRolesCharactersItemRole(d.pop("role"))

        seiyuu_with_roles_characters_item = cls(
            id=id,
            public_id=public_id,
            external_ids=external_ids,
            name_ja=name_ja,
            name_en=name_en,
            image_url=image_url,
            media=media,
            role=role,
        )

        seiyuu_with_roles_characters_item.additional_properties = d
        return seiyuu_with_roles_characters_item

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
