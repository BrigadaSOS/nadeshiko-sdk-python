from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.admin_dashboard_show_response_200_system_status import (
    AdminDashboardShowResponse200SystemStatus,
)

if TYPE_CHECKING:
    from ..models.admin_dashboard_show_response_200_system_app import (
        AdminDashboardShowResponse200SystemApp,
    )
    from ..models.admin_dashboard_show_response_200_system_database import (
        AdminDashboardShowResponse200SystemDatabase,
    )
    from ..models.admin_dashboard_show_response_200_system_elasticsearch import (
        AdminDashboardShowResponse200SystemElasticsearch,
    )
    from ..models.admin_dashboard_show_response_200_system_queues_item import (
        AdminDashboardShowResponse200SystemQueuesItem,
    )


T = TypeVar("T", bound="AdminDashboardShowResponse200System")


@_attrs_define
class AdminDashboardShowResponse200System:
    """
    Attributes:
        status (AdminDashboardShowResponse200SystemStatus):
        app (AdminDashboardShowResponse200SystemApp):
        elasticsearch (AdminDashboardShowResponse200SystemElasticsearch):
        database (AdminDashboardShowResponse200SystemDatabase):
        queues (list[AdminDashboardShowResponse200SystemQueuesItem]):
    """

    status: AdminDashboardShowResponse200SystemStatus
    app: AdminDashboardShowResponse200SystemApp
    elasticsearch: AdminDashboardShowResponse200SystemElasticsearch
    database: AdminDashboardShowResponse200SystemDatabase
    queues: list[AdminDashboardShowResponse200SystemQueuesItem]
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
        from ..models.admin_dashboard_show_response_200_system_app import (
            AdminDashboardShowResponse200SystemApp,
        )
        from ..models.admin_dashboard_show_response_200_system_database import (
            AdminDashboardShowResponse200SystemDatabase,
        )
        from ..models.admin_dashboard_show_response_200_system_elasticsearch import (
            AdminDashboardShowResponse200SystemElasticsearch,
        )
        from ..models.admin_dashboard_show_response_200_system_queues_item import (
            AdminDashboardShowResponse200SystemQueuesItem,
        )

        d = dict(src_dict)
        status = AdminDashboardShowResponse200SystemStatus(d.pop("status"))

        app = AdminDashboardShowResponse200SystemApp.from_dict(d.pop("app"))

        elasticsearch = AdminDashboardShowResponse200SystemElasticsearch.from_dict(
            d.pop("elasticsearch")
        )

        database = AdminDashboardShowResponse200SystemDatabase.from_dict(d.pop("database"))

        queues = []
        _queues = d.pop("queues")
        for queues_item_data in _queues:
            queues_item = AdminDashboardShowResponse200SystemQueuesItem.from_dict(queues_item_data)

            queues.append(queues_item)

        admin_dashboard_show_response_200_system = cls(
            status=status,
            app=app,
            elasticsearch=elasticsearch,
            database=database,
            queues=queues,
        )

        admin_dashboard_show_response_200_system.additional_properties = d
        return admin_dashboard_show_response_200_system

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
