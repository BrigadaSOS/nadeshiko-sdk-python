from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.character_with_media_media_appearances_item import (
        CharacterWithMediaMediaAppearancesItem,
    )
    from ..models.external_id import ExternalId
    from ..models.seiyuu import Seiyuu


T = TypeVar("T", bound="CharacterWithMedia")


@_attrs_define
class CharacterWithMedia:
    """Character with voice actor and all media appearances

    Attributes:
        id (int): Internal character ID Example: 1.
        external_ids (ExternalId): Map of external IDs keyed by source. Only sources with values are included.
        name_ja (str): Japanese name of the character Example: 真城最高.
        name_en (str): English name of the character Example: Moritaka Mashiro.
        image_url (str): Character image URL Example: https://s4.anilist.co/file/anilistcdn/character/large/b14545.jpg.
        seiyuu (Seiyuu): Japanese voice actor (seiyuu)
        media_appearances (list[CharacterWithMediaMediaAppearancesItem]): All media this character appears in
    """

    id: int
    external_ids: ExternalId
    name_ja: str
    name_en: str
    image_url: str
    seiyuu: Seiyuu
    media_appearances: list[CharacterWithMediaMediaAppearancesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        external_ids = self.external_ids.to_dict()

        name_ja = self.name_ja

        name_en = self.name_en

        image_url = self.image_url

        seiyuu = self.seiyuu.to_dict()

        media_appearances = []
        for media_appearances_item_data in self.media_appearances:
            media_appearances_item = media_appearances_item_data.to_dict()
            media_appearances.append(media_appearances_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "externalIds": external_ids,
                "nameJa": name_ja,
                "nameEn": name_en,
                "imageUrl": image_url,
                "seiyuu": seiyuu,
                "mediaAppearances": media_appearances,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.character_with_media_media_appearances_item import (
            CharacterWithMediaMediaAppearancesItem,
        )
        from ..models.external_id import ExternalId
        from ..models.seiyuu import Seiyuu

        d = dict(src_dict)
        id = d.pop("id")

        external_ids = ExternalId.from_dict(d.pop("externalIds"))

        name_ja = d.pop("nameJa")

        name_en = d.pop("nameEn")

        image_url = d.pop("imageUrl")

        seiyuu = Seiyuu.from_dict(d.pop("seiyuu"))

        media_appearances = []
        _media_appearances = d.pop("mediaAppearances")
        for media_appearances_item_data in _media_appearances:
            media_appearances_item = CharacterWithMediaMediaAppearancesItem.from_dict(
                media_appearances_item_data
            )

            media_appearances.append(media_appearances_item)

        character_with_media = cls(
            id=id,
            external_ids=external_ids,
            name_ja=name_ja,
            name_en=name_en,
            image_url=image_url,
            seiyuu=seiyuu,
            media_appearances=media_appearances,
        )

        character_with_media.additional_properties = d
        return character_with_media

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
