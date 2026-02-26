from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.media import Media
    from ..models.opaque_cursor_pagination import OpaqueCursorPagination


T = TypeVar("T", bound="MediaListResponse")


@_attrs_define
class MediaListResponse:
    """
    Attributes:
        media (list[Media]):
        pagination (OpaqueCursorPagination): Opaque cursor pagination metadata
    """

    media: list[Media]
    pagination: OpaqueCursorPagination
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media = []
        for media_item_data in self.media:
            media_item = media_item_data.to_dict()
            media.append(media_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "media": media,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media import Media
        from ..models.opaque_cursor_pagination import OpaqueCursorPagination

        d = dict(src_dict)
        media = []
        _media = d.pop("media")
        for media_item_data in _media:
            media_item = Media.from_dict(media_item_data)

            media.append(media_item)

        pagination = OpaqueCursorPagination.from_dict(d.pop("pagination"))

        media_list_response = cls(
            media=media,
            pagination=pagination,
        )

        media_list_response.additional_properties = d
        return media_list_response

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
