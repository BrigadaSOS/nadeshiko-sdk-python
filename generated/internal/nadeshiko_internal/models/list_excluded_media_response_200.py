from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.media_summary import MediaSummary


T = TypeVar("T", bound="ListExcludedMediaResponse200")


@_attrs_define
class ListExcludedMediaResponse200:
    """
    Attributes:
        excluded_media (list[MediaSummary]):
    """

    excluded_media: list[MediaSummary]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        excluded_media = []
        for excluded_media_item_data in self.excluded_media:
            excluded_media_item = excluded_media_item_data.to_dict()
            excluded_media.append(excluded_media_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "excludedMedia": excluded_media,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_summary import MediaSummary

        _src = dict(src_dict)
        excluded_media = []
        _excluded_media = _src.pop("excludedMedia")
        for excluded_media_item_data in _excluded_media:
            excluded_media_item = MediaSummary.from_dict(excluded_media_item_data)

            excluded_media.append(excluded_media_item)

        list_excluded_media_response_200 = cls(
            excluded_media=excluded_media,
        )

        list_excluded_media_response_200.additional_properties = _src
        return list_excluded_media_response_200

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
