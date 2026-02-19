from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.admin_dashboard_show_response_200_system_database_status import (
    AdminDashboardShowResponse200SystemDatabaseStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminDashboardShowResponse200SystemDatabase")


@_attrs_define
class AdminDashboardShowResponse200SystemDatabase:
    """
    Attributes:
        status (AdminDashboardShowResponse200SystemDatabaseStatus):
        version (None | str | Unset):
    """

    status: AdminDashboardShowResponse200SystemDatabaseStatus
    version: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = AdminDashboardShowResponse200SystemDatabaseStatus(d.pop("status"))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        admin_dashboard_show_response_200_system_database = cls(
            status=status,
            version=version,
        )

        admin_dashboard_show_response_200_system_database.additional_properties = d
        return admin_dashboard_show_response_200_system_database

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
