from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetEmailPreferencesByTokenResponse200Categories")


@_attrs_define
class GetEmailPreferencesByTokenResponse200Categories:
    """Each category the reader can hold separately. Absent from
    storage means "follow the master", which is resolved here so
    the page never has to reason about it.

        Attributes:
            recap (bool):
            checkins (bool):
            updates (bool):
    """

    recap: bool
    checkins: bool
    updates: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        recap = self.recap

        checkins = self.checkins

        updates = self.updates

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "recap": recap,
                "checkins": checkins,
                "updates": updates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        recap = _src.pop("recap")

        checkins = _src.pop("checkins")

        updates = _src.pop("updates")

        get_email_preferences_by_token_response_200_categories = cls(
            recap=recap,
            checkins=checkins,
            updates=updates,
        )

        get_email_preferences_by_token_response_200_categories.additional_properties = _src
        return get_email_preferences_by_token_response_200_categories

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
