from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExternalId")


@_attrs_define
class ExternalId:
    """External IDs for this media, keyed by source. Every source appears as a key; absent mappings are represented with a
    null value.

        Attributes:
            anilist (None | str): AniList ID Example: 21459.
            imdb (None | str): IMDB ID Example: tt1234567.
            tvdb (None | str): TVDB ID Example: 12345.
            tmdb (None | str): TMDB ID Example: 90955.
    """

    anilist: None | str
    imdb: None | str
    tvdb: None | str
    tmdb: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        anilist: None | str
        anilist = self.anilist

        imdb: None | str
        imdb = self.imdb

        tvdb: None | str
        tvdb = self.tvdb

        tmdb: None | str
        tmdb = self.tmdb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "anilist": anilist,
                "imdb": imdb,
                "tvdb": tvdb,
                "tmdb": tmdb,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)

        def _parse_anilist(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        anilist = _parse_anilist(_src.pop("anilist"))

        def _parse_imdb(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        imdb = _parse_imdb(_src.pop("imdb"))

        def _parse_tvdb(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tvdb = _parse_tvdb(_src.pop("tvdb"))

        def _parse_tmdb(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tmdb = _parse_tmdb(_src.pop("tmdb"))

        external_id = cls(
            anilist=anilist,
            imdb=imdb,
            tvdb=tvdb,
            tmdb=tmdb,
        )

        external_id.additional_properties = _src
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
