from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.collection import Collection
    from ..models.cursor_pagination import CursorPagination


T = TypeVar("T", bound="CollectionListResponse")


@_attrs_define
class CollectionListResponse:
    """Paginated collection list response

    Attributes:
        collections (list[Collection]):
        pagination (CursorPagination): Cursor pagination metadata
    """

    collections: list[Collection]
    pagination: CursorPagination
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collections = []
        for collections_item_data in self.collections:
            collections_item = collections_item_data.to_dict()
            collections.append(collections_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collections": collections,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.collection import Collection
        from ..models.cursor_pagination import CursorPagination

        d = dict(src_dict)
        collections = []
        _collections = d.pop("collections")
        for collections_item_data in _collections:
            collections_item = Collection.from_dict(collections_item_data)

            collections.append(collections_item)

        pagination = CursorPagination.from_dict(d.pop("pagination"))

        collection_list_response = cls(
            collections=collections,
            pagination=pagination,
        )

        collection_list_response.additional_properties = d
        return collection_list_response

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
