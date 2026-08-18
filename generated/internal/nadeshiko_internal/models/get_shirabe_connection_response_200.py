from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.shirabe_connection import ShirabeConnection


T = TypeVar("T", bound="GetShirabeConnectionResponse200")


@_attrs_define
class GetShirabeConnectionResponse200:
    """
    Attributes:
        connection (None | ShirabeConnection):
    """

    connection: None | ShirabeConnection
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.shirabe_connection import ShirabeConnection

        connection: dict[str, Any] | None
        if isinstance(self.connection, ShirabeConnection):
            connection = self.connection.to_dict()
        else:
            connection = self.connection

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
        from ..models.shirabe_connection import ShirabeConnection

        _src = dict(src_dict)

        def _parse_connection(data: object) -> None | ShirabeConnection:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                connection_type_1 = ShirabeConnection.from_dict(data)

                return connection_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ShirabeConnection, data)

        connection = _parse_connection(_src.pop("connection"))

        get_shirabe_connection_response_200 = cls(
            connection=connection,
        )

        get_shirabe_connection_response_200.additional_properties = _src
        return get_shirabe_connection_response_200

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
