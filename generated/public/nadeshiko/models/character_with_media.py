from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.character_with_media_media_appearances_item import CharacterWithMediaMediaAppearancesItem
  from ..models.seiyuu import Seiyuu





T = TypeVar("T", bound="CharacterWithMedia")



@_attrs_define
class CharacterWithMedia:
    """ Character with all media appearances

        Attributes:
            id (int): AniList character ID Example: 14545.
            name_japanese (str): Japanese name of the character Example: 真城最高.
            name_english (str): English name of the character Example: Moritaka Mashiro.
            image_url (str): Character image URL Example: https://s4.anilist.co/file/anilistcdn/character/large/b14545.jpg.
            seiyuu (Seiyuu): Japanese voice actor (seiyuu)
            media_appearances (list[CharacterWithMediaMediaAppearancesItem]): All media this character appears in
     """

    id: int
    name_japanese: str
    name_english: str
    image_url: str
    seiyuu: Seiyuu
    media_appearances: list[CharacterWithMediaMediaAppearancesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.seiyuu import Seiyuu
        from ..models.character_with_media_media_appearances_item import CharacterWithMediaMediaAppearancesItem
        id = self.id

        name_japanese = self.name_japanese

        name_english = self.name_english

        image_url = self.image_url

        seiyuu = self.seiyuu.to_dict()

        media_appearances = []
        for media_appearances_item_data in self.media_appearances:
            media_appearances_item = media_appearances_item_data.to_dict()
            media_appearances.append(media_appearances_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "nameJapanese": name_japanese,
            "nameEnglish": name_english,
            "imageUrl": image_url,
            "seiyuu": seiyuu,
            "mediaAppearances": media_appearances,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.character_with_media_media_appearances_item import CharacterWithMediaMediaAppearancesItem
        from ..models.seiyuu import Seiyuu
        d = dict(src_dict)
        id = d.pop("id")

        name_japanese = d.pop("nameJapanese")

        name_english = d.pop("nameEnglish")

        image_url = d.pop("imageUrl")

        seiyuu = Seiyuu.from_dict(d.pop("seiyuu"))




        media_appearances = []
        _media_appearances = d.pop("mediaAppearances")
        for media_appearances_item_data in (_media_appearances):
            media_appearances_item = CharacterWithMediaMediaAppearancesItem.from_dict(media_appearances_item_data)



            media_appearances.append(media_appearances_item)


        character_with_media = cls(
            id=id,
            name_japanese=name_japanese,
            name_english=name_english,
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
