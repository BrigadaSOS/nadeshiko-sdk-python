from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.patreon_connection import PatreonConnection


T = TypeVar("T", bound="GetPatreonConnectionResponse200")


@_attrs_define
class GetPatreonConnectionResponse200:
    """
    Attributes:
        connection (None | PatreonConnection):
        patreon_url (str):
    """

    connection: None | PatreonConnection
    patreon_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.patreon_connection import PatreonConnection  # noqa: PLC0415

        connection: dict[str, Any] | None
        if isinstance(self.connection, PatreonConnection):
            connection = self.connection.to_dict()
        else:
            connection = self.connection

        patreon_url = self.patreon_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connection": connection,
                "patreonUrl": patreon_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patreon_connection import PatreonConnection  # noqa: PLC0415

        _src = dict(src_dict)

        def _parse_connection(data: object) -> None | PatreonConnection:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                connection_type_0 = PatreonConnection.from_dict(data)

                return connection_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatreonConnection, data)

        connection = _parse_connection(_src.pop("connection"))

        patreon_url = _src.pop("patreonUrl")

        get_patreon_connection_response_200 = cls(
            connection=connection,
            patreon_url=patreon_url,
        )

        get_patreon_connection_response_200.additional_properties = _src
        return get_patreon_connection_response_200

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
