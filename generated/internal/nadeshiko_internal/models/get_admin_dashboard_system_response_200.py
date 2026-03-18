from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_admin_dashboard_system_response_200_status import (
    GetAdminDashboardSystemResponse200Status,
)

if TYPE_CHECKING:
    from ..models.get_admin_dashboard_system_response_200_app import (
        GetAdminDashboardSystemResponse200App,
    )
    from ..models.get_admin_dashboard_system_response_200_database import (
        GetAdminDashboardSystemResponse200Database,
    )
    from ..models.get_admin_dashboard_system_response_200_elasticsearch import (
        GetAdminDashboardSystemResponse200Elasticsearch,
    )
    from ..models.get_admin_dashboard_system_response_200_queues_item import (
        GetAdminDashboardSystemResponse200QueuesItem,
    )


T = TypeVar("T", bound="GetAdminDashboardSystemResponse200")


@_attrs_define
class GetAdminDashboardSystemResponse200:
    """
    Attributes:
        status (GetAdminDashboardSystemResponse200Status):
        app (GetAdminDashboardSystemResponse200App):
        elasticsearch (GetAdminDashboardSystemResponse200Elasticsearch):
        database (GetAdminDashboardSystemResponse200Database):
        queues (list[GetAdminDashboardSystemResponse200QueuesItem]):
    """

    status: GetAdminDashboardSystemResponse200Status
    app: GetAdminDashboardSystemResponse200App
    elasticsearch: GetAdminDashboardSystemResponse200Elasticsearch
    database: GetAdminDashboardSystemResponse200Database
    queues: list[GetAdminDashboardSystemResponse200QueuesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        app = self.app.to_dict()

        elasticsearch = self.elasticsearch.to_dict()

        database = self.database.to_dict()

        queues = []
        for queues_item_data in self.queues:
            queues_item = queues_item_data.to_dict()
            queues.append(queues_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "app": app,
                "elasticsearch": elasticsearch,
                "database": database,
                "queues": queues,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_admin_dashboard_system_response_200_app import (
            GetAdminDashboardSystemResponse200App,
        )
        from ..models.get_admin_dashboard_system_response_200_database import (
            GetAdminDashboardSystemResponse200Database,
        )
        from ..models.get_admin_dashboard_system_response_200_elasticsearch import (
            GetAdminDashboardSystemResponse200Elasticsearch,
        )
        from ..models.get_admin_dashboard_system_response_200_queues_item import (
            GetAdminDashboardSystemResponse200QueuesItem,
        )

        d = dict(src_dict)
        status = GetAdminDashboardSystemResponse200Status(d.pop("status"))

        app = GetAdminDashboardSystemResponse200App.from_dict(d.pop("app"))

        elasticsearch = GetAdminDashboardSystemResponse200Elasticsearch.from_dict(
            d.pop("elasticsearch")
        )

        database = GetAdminDashboardSystemResponse200Database.from_dict(d.pop("database"))

        queues = []
        _queues = d.pop("queues")
        for queues_item_data in _queues:
            queues_item = GetAdminDashboardSystemResponse200QueuesItem.from_dict(queues_item_data)

            queues.append(queues_item)

        get_admin_dashboard_system_response_200 = cls(
            status=status,
            app=app,
            elasticsearch=elasticsearch,
            database=database,
            queues=queues,
        )

        get_admin_dashboard_system_response_200.additional_properties = d
        return get_admin_dashboard_system_response_200

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
