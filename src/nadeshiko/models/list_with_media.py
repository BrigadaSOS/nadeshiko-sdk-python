from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_with_media_type import ListWithMediaType
from ..models.list_with_media_visibility import ListWithMediaVisibility

if TYPE_CHECKING:
    from ..models.list_with_media_media_item import ListWithMediaMediaItem


T = TypeVar("T", bound="ListWithMedia")


@_attrs_define
class ListWithMedia:
    """List with all media in order

    Attributes:
        id (int): List ID Example: 123.
        name (str): Name of the list Example: Bakuman Series.
        type_ (ListWithMediaType): Type of list Example: SERIES.
        user_id (int): User ID who owns the list (1 = admin) Example: 1.
        visibility (ListWithMediaVisibility): Visibility of the list Example: PUBLIC.
        media (list[ListWithMediaMediaItem]): All media in the list, sorted by position
    """

    id: int
    name: str
    type_: ListWithMediaType
    user_id: int
    visibility: ListWithMediaVisibility
    media: list[ListWithMediaMediaItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_ = self.type_.value

        user_id = self.user_id

        visibility = self.visibility.value

        media = []
        for media_item_data in self.media:
            media_item = media_item_data.to_dict()
            media.append(media_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type_,
                "userId": user_id,
                "visibility": visibility,
                "media": media,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_with_media_media_item import ListWithMediaMediaItem

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        type_ = ListWithMediaType(d.pop("type"))

        user_id = d.pop("userId")

        visibility = ListWithMediaVisibility(d.pop("visibility"))

        media = []
        _media = d.pop("media")
        for media_item_data in _media:
            media_item = ListWithMediaMediaItem.from_dict(media_item_data)

            media.append(media_item)

        list_with_media = cls(
            id=id,
            name=name,
            type_=type_,
            user_id=user_id,
            visibility=visibility,
            media=media,
        )

        list_with_media.additional_properties = d
        return list_with_media

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
