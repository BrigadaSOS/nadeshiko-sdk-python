from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PatreonConnection")


@_attrs_define
class PatreonConnection:
    """
    Attributes:
        linked (bool):
        full_name (None | str):
        active (bool):
        patron_status (None | str):
        entitled_amount_cents (int):
        membership_checked_at (datetime.datetime):
        linked_at (datetime.datetime):
    """

    linked: bool
    full_name: None | str
    active: bool
    patron_status: None | str
    entitled_amount_cents: int
    membership_checked_at: datetime.datetime
    linked_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        linked = self.linked

        full_name: None | str
        full_name = self.full_name

        active = self.active

        patron_status: None | str
        patron_status = self.patron_status

        entitled_amount_cents = self.entitled_amount_cents

        membership_checked_at = self.membership_checked_at.isoformat()

        linked_at = self.linked_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "linked": linked,
                "fullName": full_name,
                "active": active,
                "patronStatus": patron_status,
                "entitledAmountCents": entitled_amount_cents,
                "membershipCheckedAt": membership_checked_at,
                "linkedAt": linked_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        linked = _src.pop("linked")

        def _parse_full_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        full_name = _parse_full_name(_src.pop("fullName"))

        active = _src.pop("active")

        def _parse_patron_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        patron_status = _parse_patron_status(_src.pop("patronStatus"))

        entitled_amount_cents = _src.pop("entitledAmountCents")

        membership_checked_at = datetime.datetime.fromisoformat(_src.pop("membershipCheckedAt"))

        linked_at = datetime.datetime.fromisoformat(_src.pop("linkedAt"))

        patreon_connection = cls(
            linked=linked,
            full_name=full_name,
            active=active,
            patron_status=patron_status,
            entitled_amount_cents=entitled_amount_cents,
            membership_checked_at=membership_checked_at,
            linked_at=linked_at,
        )

        patreon_connection.additional_properties = _src
        return patreon_connection

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
