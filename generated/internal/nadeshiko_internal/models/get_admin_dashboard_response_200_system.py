from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_admin_dashboard_response_200_system_status import (
    GetAdminDashboardResponse200SystemStatus,
)

if TYPE_CHECKING:
    from ..models.get_admin_dashboard_response_200_system_app import (
        GetAdminDashboardResponse200SystemApp,
    )
    from ..models.get_admin_dashboard_response_200_system_database import (
        GetAdminDashboardResponse200SystemDatabase,
    )
    from ..models.get_admin_dashboard_response_200_system_elasticsearch import (
        GetAdminDashboardResponse200SystemElasticsearch,
    )
    from ..models.get_admin_dashboard_response_200_system_queues_item import (
        GetAdminDashboardResponse200SystemQueuesItem,
    )


T = TypeVar("T", bound="GetAdminDashboardResponse200System")


@_attrs_define
class GetAdminDashboardResponse200System:
    """
    Attributes:
        status (GetAdminDashboardResponse200SystemStatus):
        app (GetAdminDashboardResponse200SystemApp):
        elasticsearch (GetAdminDashboardResponse200SystemElasticsearch):
        database (GetAdminDashboardResponse200SystemDatabase):
        queues (list[GetAdminDashboardResponse200SystemQueuesItem]):
    """

    status: GetAdminDashboardResponse200SystemStatus
    app: GetAdminDashboardResponse200SystemApp
    elasticsearch: GetAdminDashboardResponse200SystemElasticsearch
    database: GetAdminDashboardResponse200SystemDatabase
    queues: list[GetAdminDashboardResponse200SystemQueuesItem]
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
        from ..models.get_admin_dashboard_response_200_system_app import (
            GetAdminDashboardResponse200SystemApp,
        )
        from ..models.get_admin_dashboard_response_200_system_database import (
            GetAdminDashboardResponse200SystemDatabase,
        )
        from ..models.get_admin_dashboard_response_200_system_elasticsearch import (
            GetAdminDashboardResponse200SystemElasticsearch,
        )
        from ..models.get_admin_dashboard_response_200_system_queues_item import (
            GetAdminDashboardResponse200SystemQueuesItem,
        )

        _src = dict(src_dict)
        status = GetAdminDashboardResponse200SystemStatus(_src.pop("status"))

        app = GetAdminDashboardResponse200SystemApp.from_dict(_src.pop("app"))

        elasticsearch = GetAdminDashboardResponse200SystemElasticsearch.from_dict(
            _src.pop("elasticsearch")
        )

        database = GetAdminDashboardResponse200SystemDatabase.from_dict(_src.pop("database"))

        queues = []
        _queues = _src.pop("queues")
        for queues_item_data in _queues:
            queues_item = GetAdminDashboardResponse200SystemQueuesItem.from_dict(queues_item_data)

            queues.append(queues_item)

        get_admin_dashboard_response_200_system = cls(
            status=status,
            app=app,
            elasticsearch=elasticsearch,
            database=database,
            queues=queues,
        )

        get_admin_dashboard_response_200_system.additional_properties = _src
        return get_admin_dashboard_response_200_system

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
