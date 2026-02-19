from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CursorPagination")


@_attrs_define
class CursorPagination:
    """Cursor pagination metadata

    Attributes:
        has_more (bool): Whether more results are available Example: True.
        cursor (int | None): Cursor for the next page (`null` when `hasMore` is `false`) Example: 42.
    """

    has_more: bool
    cursor: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        has_more = self.has_more

        cursor: int | None
        cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hasMore": has_more,
                "cursor": cursor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        has_more = d.pop("hasMore")

        def _parse_cursor(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        cursor = _parse_cursor(d.pop("cursor"))

        cursor_pagination = cls(
            has_more=has_more,
            cursor=cursor,
        )

        cursor_pagination.additional_properties = d
        return cursor_pagination

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
