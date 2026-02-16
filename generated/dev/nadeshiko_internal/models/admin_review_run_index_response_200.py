from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.review_check_run import ReviewCheckRun


T = TypeVar("T", bound="AdminReviewRunIndexResponse200")


@_attrs_define
class AdminReviewRunIndexResponse200:
    """
    Attributes:
        data (list[ReviewCheckRun]):
        has_more (bool):
        cursor (int | None | Unset):
    """

    data: list[ReviewCheckRun]
    has_more: bool
    cursor: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        has_more = self.has_more

        cursor: int | None | Unset
        if isinstance(self.cursor, Unset):
            cursor = UNSET
        else:
            cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "hasMore": has_more,
            }
        )
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.review_check_run import ReviewCheckRun

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = ReviewCheckRun.from_dict(data_item_data)

            data.append(data_item)

        has_more = d.pop("hasMore")

        def _parse_cursor(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cursor = _parse_cursor(d.pop("cursor", UNSET))

        admin_review_run_index_response_200 = cls(
            data=data,
            has_more=has_more,
            cursor=cursor,
        )

        admin_review_run_index_response_200.additional_properties = d
        return admin_review_run_index_response_200

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
