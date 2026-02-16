from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.admin_morpheme_backfill_create_response_200_stats import (
        AdminMorphemeBackfillCreateResponse200Stats,
    )


T = TypeVar("T", bound="AdminMorphemeBackfillCreateResponse200")


@_attrs_define
class AdminMorphemeBackfillCreateResponse200:
    """
    Attributes:
        success (bool):
        message (str):
        stats (AdminMorphemeBackfillCreateResponse200Stats):
    """

    success: bool
    message: str
    stats: AdminMorphemeBackfillCreateResponse200Stats
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        message = self.message

        stats = self.stats.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "message": message,
                "stats": stats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admin_morpheme_backfill_create_response_200_stats import (
            AdminMorphemeBackfillCreateResponse200Stats,
        )

        d = dict(src_dict)
        success = d.pop("success")

        message = d.pop("message")

        stats = AdminMorphemeBackfillCreateResponse200Stats.from_dict(d.pop("stats"))

        admin_morpheme_backfill_create_response_200 = cls(
            success=success,
            message=message,
            stats=stats,
        )

        admin_morpheme_backfill_create_response_200.additional_properties = d
        return admin_morpheme_backfill_create_response_200

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
