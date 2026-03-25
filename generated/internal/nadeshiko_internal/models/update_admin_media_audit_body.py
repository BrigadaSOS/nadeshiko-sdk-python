from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_admin_media_audit_body_threshold import UpdateAdminMediaAuditBodyThreshold


T = TypeVar("T", bound="UpdateAdminMediaAuditBody")


@_attrs_define
class UpdateAdminMediaAuditBody:
    """
    Attributes:
        threshold (UpdateAdminMediaAuditBodyThreshold | Unset): New threshold values
        enabled (bool | Unset): Enable or disable this audit
    """

    threshold: UpdateAdminMediaAuditBodyThreshold | Unset = UNSET
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
        from ..models.update_admin_media_audit_body_threshold import (
            UpdateAdminMediaAuditBodyThreshold,
        )

        _src = dict(src_dict)
        _threshold = _src.pop("threshold", UNSET)
        threshold: UpdateAdminMediaAuditBodyThreshold | Unset
        if isinstance(_threshold, Unset):
            threshold = UNSET
        else:
            threshold = UpdateAdminMediaAuditBodyThreshold.from_dict(_threshold)

        enabled = _src.pop("enabled", UNSET)

        update_admin_media_audit_body = cls(
            threshold=threshold,
            enabled=enabled,
        )

        update_admin_media_audit_body.additional_properties = _src
        return update_admin_media_audit_body

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
