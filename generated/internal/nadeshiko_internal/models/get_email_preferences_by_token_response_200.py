from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_email_preferences_by_token_response_200_category import (
    GetEmailPreferencesByTokenResponse200Category,
    check_get_email_preferences_by_token_response_200_category,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_email_preferences_by_token_response_200_categories import (
        GetEmailPreferencesByTokenResponse200Categories,
    )


T = TypeVar("T", bound="GetEmailPreferencesByTokenResponse200")


@_attrs_define
class GetEmailPreferencesByTokenResponse200:
    """
    Attributes:
        enabled (bool): The master switch. False means nothing below is sent.
        categories (GetEmailPreferencesByTokenResponse200Categories): Each category the reader can hold separately.
            Absent from
            storage means "follow the master", which is resolved here so
            the page never has to reason about it.
        category (GetEmailPreferencesByTokenResponse200Category | Unset): Which category the email carrying this token
            belonged to, when
            it named one. The page highlights it, because that is the one
            the reader clicked about.
    """

    enabled: bool
    categories: GetEmailPreferencesByTokenResponse200Categories
    category: GetEmailPreferencesByTokenResponse200Category | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        categories = self.categories.to_dict()

        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "categories": categories,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_email_preferences_by_token_response_200_categories import (
            GetEmailPreferencesByTokenResponse200Categories,
        )

        _src = dict(src_dict)
        enabled = _src.pop("enabled")

        categories = GetEmailPreferencesByTokenResponse200Categories.from_dict(
            _src.pop("categories")
        )

        _category = _src.pop("category", UNSET)
        category: GetEmailPreferencesByTokenResponse200Category | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = check_get_email_preferences_by_token_response_200_category(_category)

        get_email_preferences_by_token_response_200 = cls(
            enabled=enabled,
            categories=categories,
            category=category,
        )

        get_email_preferences_by_token_response_200.additional_properties = _src
        return get_email_preferences_by_token_response_200

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
