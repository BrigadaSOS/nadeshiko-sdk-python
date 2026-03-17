from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_admin_health_response_200_status import GetAdminHealthResponse200Status

if TYPE_CHECKING:
    from ..models.get_admin_health_response_200_app import GetAdminHealthResponse200App
    from ..models.get_admin_health_response_200_database import GetAdminHealthResponse200Database
    from ..models.get_admin_health_response_200_elasticsearch import (
        GetAdminHealthResponse200Elasticsearch,
    )


T = TypeVar("T", bound="GetAdminHealthResponse200")


@_attrs_define
class GetAdminHealthResponse200:
    """
    Attributes:
        status (GetAdminHealthResponse200Status): Overall system status
        app (GetAdminHealthResponse200App):
        elasticsearch (GetAdminHealthResponse200Elasticsearch):
        database (GetAdminHealthResponse200Database):
    """

    status: GetAdminHealthResponse200Status
    app: GetAdminHealthResponse200App
    elasticsearch: GetAdminHealthResponse200Elasticsearch
    database: GetAdminHealthResponse200Database
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
        from ..models.get_admin_health_response_200_app import GetAdminHealthResponse200App
        from ..models.get_admin_health_response_200_database import (
            GetAdminHealthResponse200Database,
        )
        from ..models.get_admin_health_response_200_elasticsearch import (
            GetAdminHealthResponse200Elasticsearch,
        )

        d = dict(src_dict)
        status = GetAdminHealthResponse200Status(d.pop("status"))

        app = GetAdminHealthResponse200App.from_dict(d.pop("app"))

        elasticsearch = GetAdminHealthResponse200Elasticsearch.from_dict(d.pop("elasticsearch"))

        database = GetAdminHealthResponse200Database.from_dict(d.pop("database"))

        get_admin_health_response_200 = cls(
            status=status,
            app=app,
            elasticsearch=elasticsearch,
            database=database,
        )

        get_admin_health_response_200.additional_properties = d
        return get_admin_health_response_200

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
