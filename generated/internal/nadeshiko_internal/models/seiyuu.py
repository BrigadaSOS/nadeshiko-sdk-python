from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.external_id import ExternalId


T = TypeVar("T", bound="Seiyuu")


@_attrs_define
class Seiyuu:
    """Japanese voice actor (seiyuu)

    Attributes:
        id (int): Internal seiyuu ID Example: 1.
        public_id (str): Public identifier for the seiyuu (use this in public URLs) Example: V1StGXR8_Z5d.
        external_ids (ExternalId): Map of external IDs keyed by source. Only sources with values are included.
        name_ja (str): Japanese name of the voice actor Example: 阿部敦.
        name_en (str): English name of the voice actor Example: Atsushi Abe.
        image_url (str): Profile image URL Example: https://s4.anilist.co/file/anilistcdn/staff/large/n95991.jpg.
    """

    id: int
    public_id: str
    external_ids: ExternalId
    name_ja: str
    name_en: str
    image_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        public_id = self.public_id

        external_ids = self.external_ids.to_dict()

        name_ja = self.name_ja

        name_en = self.name_en

        image_url = self.image_url

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
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.external_id import ExternalId

        _src = dict(src_dict)
        id = _src.pop("id")

        public_id = _src.pop("publicId")

        external_ids = ExternalId.from_dict(_src.pop("externalIds"))

        name_ja = _src.pop("nameJa")

        name_en = _src.pop("nameEn")

        image_url = _src.pop("imageUrl")

        seiyuu = cls(
            id=id,
            public_id=public_id,
            external_ids=external_ids,
            name_ja=name_ja,
            name_en=name_en,
            image_url=image_url,
        )

        seiyuu.additional_properties = _src
        return seiyuu

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
