from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.patreon_connection import PatreonConnection


T = TypeVar("T", bound="CompletePatreonLinkResponse200")


@_attrs_define
class CompletePatreonLinkResponse200:
    """
    Attributes:
        connection (PatreonConnection):
    """

    connection: PatreonConnection
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection = self.connection.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connection": connection,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patreon_connection import PatreonConnection  # noqa: PLC0415

        _src = dict(src_dict)
        connection = PatreonConnection.from_dict(_src.pop("connection"))

        complete_patreon_link_response_200 = cls(
            connection=connection,
        )

        complete_patreon_link_response_200.additional_properties = _src
        return complete_patreon_link_response_200

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
