from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.review_check_threshold_schema_item_type import ReviewCheckThresholdSchemaItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReviewCheckThresholdSchemaItem")


@_attrs_define
class ReviewCheckThresholdSchemaItem:
    """
    Attributes:
        key (str | Unset):
        label (str | Unset):
        type_ (ReviewCheckThresholdSchemaItemType | Unset):
        default (bool | float | Unset):
        min_ (float | Unset):
        max_ (float | Unset):
    """

    key: str | Unset = UNSET
    label: str | Unset = UNSET
    type_: ReviewCheckThresholdSchemaItemType | Unset = UNSET
    default: bool | float | Unset = UNSET
    min_: float | Unset = UNSET
    max_: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        label = self.label

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        default: bool | float | Unset
        if isinstance(self.default, Unset):
            default = UNSET
        else:
            default = self.default

        min_ = self.min_

        max_ = self.max_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if label is not UNSET:
            field_dict["label"] = label
        if type_ is not UNSET:
            field_dict["type"] = type_
        if default is not UNSET:
            field_dict["default"] = default
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key", UNSET)

        label = d.pop("label", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: ReviewCheckThresholdSchemaItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ReviewCheckThresholdSchemaItemType(_type_)

        def _parse_default(data: object) -> bool | float | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | float | Unset, data)

        default = _parse_default(d.pop("default", UNSET))

        min_ = d.pop("min", UNSET)

        max_ = d.pop("max", UNSET)

        review_check_threshold_schema_item = cls(
            key=key,
            label=label,
            type_=type_,
            default=default,
            min_=min_,
            max_=max_,
        )

        review_check_threshold_schema_item.additional_properties = d
        return review_check_threshold_schema_item

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
