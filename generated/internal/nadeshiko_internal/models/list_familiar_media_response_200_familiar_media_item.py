from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.media_summary import MediaSummary


T = TypeVar("T", bound="ListFamiliarMediaResponse200FamiliarMediaItem")


@_attrs_define
class ListFamiliarMediaResponse200FamiliarMediaItem:
    """
    Attributes:
        media (MediaSummary): Slim media item returned by autocomplete (names + cover only)
        score (float): Weighted engagement score; ordering key, not a display value.
        anki_count (int):
        play_count (int):
        share_count (int):
    """

    media: MediaSummary
    score: float
    anki_count: int
    play_count: int
    share_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media = self.media.to_dict()

        score = self.score

        anki_count = self.anki_count

        play_count = self.play_count

        share_count = self.share_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "media": media,
                "score": score,
                "ankiCount": anki_count,
                "playCount": play_count,
                "shareCount": share_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_summary import MediaSummary

        _src = dict(src_dict)
        media = MediaSummary.from_dict(_src.pop("media"))

        score = _src.pop("score")

        anki_count = _src.pop("ankiCount")

        play_count = _src.pop("playCount")

        share_count = _src.pop("shareCount")

        list_familiar_media_response_200_familiar_media_item = cls(
            media=media,
            score=score,
            anki_count=anki_count,
            play_count=play_count,
            share_count=share_count,
        )

        list_familiar_media_response_200_familiar_media_item.additional_properties = _src
        return list_familiar_media_response_200_familiar_media_item

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
