from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cursor_pagination import CursorPagination
    from ..models.user_activity import UserActivity


T = TypeVar("T", bound="ListUserActivityResponse200")


@_attrs_define
class ListUserActivityResponse200:
    """
    Attributes:
        activities (list[UserActivity]):
        pagination (CursorPagination): Opaque cursor pagination metadata
    """

    activities: list[UserActivity]
    pagination: CursorPagination
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activities = []
        for activities_item_data in self.activities:
            activities_item = activities_item_data.to_dict()
            activities.append(activities_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "activities": activities,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cursor_pagination import CursorPagination
        from ..models.user_activity import UserActivity

        _src = dict(src_dict)
        activities = []
        _activities = _src.pop("activities")
        for activities_item_data in _activities:
            activities_item = UserActivity.from_dict(activities_item_data)

            activities.append(activities_item)

        pagination = CursorPagination.from_dict(_src.pop("pagination"))

        list_user_activity_response_200 = cls(
            activities=activities,
            pagination=pagination,
        )

        list_user_activity_response_200.additional_properties = _src
        return list_user_activity_response_200

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
