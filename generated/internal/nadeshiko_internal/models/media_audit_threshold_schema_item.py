from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.media_audit_threshold_schema_item_type import (
    MediaAuditThresholdSchemaItemType,
    check_media_audit_threshold_schema_item_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="MediaAuditThresholdSchemaItem")


@_attrs_define
class MediaAuditThresholdSchemaItem:
    """
    Attributes:
        key (str):
        label (str):
        type_ (MediaAuditThresholdSchemaItemType):
        default (bool | float):
        min_ (float | Unset):
        max_ (float | Unset):
    """

    key: str
    label: str
    type_: MediaAuditThresholdSchemaItemType
    default: bool | float
    min_: float | Unset = UNSET
    max_: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        label = self.label

        type_: str = self.type_

        default: bool | float
        default = self.default

        min_ = self.min_

        max_ = self.max_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "label": label,
                "type": type_,
                "default": default,
            }
        )
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        key = _src.pop("key")

        label = _src.pop("label")

        type_ = check_media_audit_threshold_schema_item_type(_src.pop("type"))

        def _parse_default(data: object) -> bool | float:
            return cast(bool | float, data)

        default = _parse_default(_src.pop("default"))

        min_ = _src.pop("min", UNSET)

        max_ = _src.pop("max", UNSET)

        media_audit_threshold_schema_item = cls(
            key=key,
            label=label,
            type_=type_,
            default=default,
            min_=min_,
            max_=max_,
        )

        media_audit_threshold_schema_item.additional_properties = _src
        return media_audit_threshold_schema_item

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
