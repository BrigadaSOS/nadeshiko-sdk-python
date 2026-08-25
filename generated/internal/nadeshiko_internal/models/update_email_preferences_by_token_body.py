from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateEmailPreferencesByTokenBody")


@_attrs_define
class UpdateEmailPreferencesByTokenBody:
    """
    Attributes:
        token (str): The same token the link carries. In the BODY rather than the
            query for this one, unlike the GET: a write does not need to be
            reachable from a URL, and keeping it out of the path keeps it out
            of proxy access logs and browser history.
        enabled (bool | Unset):
        recap (bool | Unset):
        checkins (bool | Unset):
        updates (bool | Unset):
    """

    token: str
    enabled: bool | Unset = UNSET
    recap: bool | Unset = UNSET
    checkins: bool | Unset = UNSET
    updates: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        enabled = self.enabled

        recap = self.recap

        checkins = self.checkins

        updates = self.updates

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if recap is not UNSET:
            field_dict["recap"] = recap
        if checkins is not UNSET:
            field_dict["checkins"] = checkins
        if updates is not UNSET:
            field_dict["updates"] = updates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        token = _src.pop("token")

        enabled = _src.pop("enabled", UNSET)

        recap = _src.pop("recap", UNSET)

        checkins = _src.pop("checkins", UNSET)

        updates = _src.pop("updates", UNSET)

        update_email_preferences_by_token_body = cls(
            token=token,
            enabled=enabled,
            recap=recap,
            checkins=checkins,
            updates=updates,
        )

        update_email_preferences_by_token_body.additional_properties = _src
        return update_email_preferences_by_token_body

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
