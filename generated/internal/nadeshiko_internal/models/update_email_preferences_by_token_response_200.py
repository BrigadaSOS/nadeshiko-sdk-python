from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.update_email_preferences_by_token_response_200_categories import (
        UpdateEmailPreferencesByTokenResponse200Categories,
    )


T = TypeVar("T", bound="UpdateEmailPreferencesByTokenResponse200")


@_attrs_define
class UpdateEmailPreferencesByTokenResponse200:
    """
    Attributes:
        enabled (bool):
        categories (UpdateEmailPreferencesByTokenResponse200Categories):
    """

    enabled: bool
    categories: UpdateEmailPreferencesByTokenResponse200Categories
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        categories = self.categories.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "categories": categories,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_email_preferences_by_token_response_200_categories import (
            UpdateEmailPreferencesByTokenResponse200Categories,
        )

        _src = dict(src_dict)
        enabled = _src.pop("enabled")

        categories = UpdateEmailPreferencesByTokenResponse200Categories.from_dict(
            _src.pop("categories")
        )

        update_email_preferences_by_token_response_200 = cls(
            enabled=enabled,
            categories=categories,
        )

        update_email_preferences_by_token_response_200.additional_properties = _src
        return update_email_preferences_by_token_response_200

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
