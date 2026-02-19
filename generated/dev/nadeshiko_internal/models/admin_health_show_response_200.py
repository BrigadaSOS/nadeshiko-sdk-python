from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.admin_health_show_response_200_status import AdminHealthShowResponse200Status

if TYPE_CHECKING:
    from ..models.admin_health_show_response_200_app import AdminHealthShowResponse200App
    from ..models.admin_health_show_response_200_database import AdminHealthShowResponse200Database
    from ..models.admin_health_show_response_200_elasticsearch import (
        AdminHealthShowResponse200Elasticsearch,
    )


T = TypeVar("T", bound="AdminHealthShowResponse200")


@_attrs_define
class AdminHealthShowResponse200:
    """
    Attributes:
        status (AdminHealthShowResponse200Status): Overall system status
        app (AdminHealthShowResponse200App):
        elasticsearch (AdminHealthShowResponse200Elasticsearch):
        database (AdminHealthShowResponse200Database):
    """

    status: AdminHealthShowResponse200Status
    app: AdminHealthShowResponse200App
    elasticsearch: AdminHealthShowResponse200Elasticsearch
    database: AdminHealthShowResponse200Database
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        app = self.app.to_dict()

        elasticsearch = self.elasticsearch.to_dict()

        database = self.database.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "app": app,
                "elasticsearch": elasticsearch,
                "database": database,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admin_health_show_response_200_app import AdminHealthShowResponse200App
        from ..models.admin_health_show_response_200_database import (
            AdminHealthShowResponse200Database,
        )
        from ..models.admin_health_show_response_200_elasticsearch import (
            AdminHealthShowResponse200Elasticsearch,
        )

        d = dict(src_dict)
        status = AdminHealthShowResponse200Status(d.pop("status"))

        app = AdminHealthShowResponse200App.from_dict(d.pop("app"))

        elasticsearch = AdminHealthShowResponse200Elasticsearch.from_dict(d.pop("elasticsearch"))

        database = AdminHealthShowResponse200Database.from_dict(d.pop("database"))

        admin_health_show_response_200 = cls(
            status=status,
            app=app,
            elasticsearch=elasticsearch,
            database=database,
        )

        admin_health_show_response_200.additional_properties = d
        return admin_health_show_response_200

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
