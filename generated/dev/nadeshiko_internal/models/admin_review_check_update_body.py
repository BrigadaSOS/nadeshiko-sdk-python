from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.admin_review_check_update_body_threshold import (
        AdminReviewCheckUpdateBodyThreshold,
    )


T = TypeVar("T", bound="AdminReviewCheckUpdateBody")


@_attrs_define
class AdminReviewCheckUpdateBody:
    """
    Attributes:
        threshold (AdminReviewCheckUpdateBodyThreshold | Unset): New threshold values
        enabled (bool | Unset): Enable or disable this check
    """

    threshold: AdminReviewCheckUpdateBodyThreshold | Unset = UNSET
    enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        threshold: dict[str, Any] | Unset = UNSET
        if not isinstance(self.threshold, Unset):
            threshold = self.threshold.to_dict()

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if threshold is not UNSET:
            field_dict["threshold"] = threshold
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admin_review_check_update_body_threshold import (
            AdminReviewCheckUpdateBodyThreshold,
        )

        d = dict(src_dict)
        _threshold = d.pop("threshold", UNSET)
        threshold: AdminReviewCheckUpdateBodyThreshold | Unset
        if isinstance(_threshold, Unset):
            threshold = UNSET
        else:
            threshold = AdminReviewCheckUpdateBodyThreshold.from_dict(_threshold)

        enabled = d.pop("enabled", UNSET)

        admin_review_check_update_body = cls(
            threshold=threshold,
            enabled=enabled,
        )

        admin_review_check_update_body.additional_properties = d
        return admin_review_check_update_body

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
