from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalId")


@_attrs_define
class ExternalId:
    """Map of external IDs keyed by source. Only sources with values are included.

    Attributes:
        anilist (str | Unset): AniList ID Example: 21459.
        imdb (str | Unset): IMDB ID Example: tt1234567.
        tvdb (str | Unset): TVDB ID Example: 12345.
    """

    anilist: str | Unset = UNSET
    imdb: str | Unset = UNSET
    tvdb: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        anilist = self.anilist

        imdb = self.imdb

        tvdb = self.tvdb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if anilist is not UNSET:
            field_dict["anilist"] = anilist
        if imdb is not UNSET:
            field_dict["imdb"] = imdb
        if tvdb is not UNSET:
            field_dict["tvdb"] = tvdb

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        anilist = d.pop("anilist", UNSET)

        imdb = d.pop("imdb", UNSET)

        tvdb = d.pop("tvdb", UNSET)

        external_id = cls(
            anilist=anilist,
            imdb=imdb,
            tvdb=tvdb,
        )

        external_id.additional_properties = d
        return external_id

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
