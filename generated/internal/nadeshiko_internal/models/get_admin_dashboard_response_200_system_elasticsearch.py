from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_admin_dashboard_response_200_system_elasticsearch_status import (
    GetAdminDashboardResponse200SystemElasticsearchStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAdminDashboardResponse200SystemElasticsearch")


@_attrs_define
class GetAdminDashboardResponse200SystemElasticsearch:
    """
    Attributes:
        status (GetAdminDashboardResponse200SystemElasticsearchStatus):
        version (None | str | Unset):
        cluster_name (None | str | Unset):
        cluster_status (None | str | Unset):
        index_name (None | str | Unset):
        document_count (int | None | Unset):
    """

    status: GetAdminDashboardResponse200SystemElasticsearchStatus
    version: None | str | Unset = UNSET
    cluster_name: None | str | Unset = UNSET
    cluster_status: None | str | Unset = UNSET
    index_name: None | str | Unset = UNSET
    document_count: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        cluster_name: None | str | Unset
        if isinstance(self.cluster_name, Unset):
            cluster_name = UNSET
        else:
            cluster_name = self.cluster_name

        cluster_status: None | str | Unset
        if isinstance(self.cluster_status, Unset):
            cluster_status = UNSET
        else:
            cluster_status = self.cluster_status

        index_name: None | str | Unset
        if isinstance(self.index_name, Unset):
            index_name = UNSET
        else:
            index_name = self.index_name

        document_count: int | None | Unset
        if isinstance(self.document_count, Unset):
            document_count = UNSET
        else:
            document_count = self.document_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if version is not UNSET:
            field_dict["version"] = version
        if cluster_name is not UNSET:
            field_dict["clusterName"] = cluster_name
        if cluster_status is not UNSET:
            field_dict["clusterStatus"] = cluster_status
        if index_name is not UNSET:
            field_dict["indexName"] = index_name
        if document_count is not UNSET:
            field_dict["documentCount"] = document_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        status = GetAdminDashboardResponse200SystemElasticsearchStatus(_src.pop("status"))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(_src.pop("version", UNSET))

        def _parse_cluster_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cluster_name = _parse_cluster_name(_src.pop("clusterName", UNSET))

        def _parse_cluster_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cluster_status = _parse_cluster_status(_src.pop("clusterStatus", UNSET))

        def _parse_index_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        index_name = _parse_index_name(_src.pop("indexName", UNSET))

        def _parse_document_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        document_count = _parse_document_count(_src.pop("documentCount", UNSET))

        get_admin_dashboard_response_200_system_elasticsearch = cls(
            status=status,
            version=version,
            cluster_name=cluster_name,
            cluster_status=cluster_status,
            index_name=index_name,
            document_count=document_count,
        )

        get_admin_dashboard_response_200_system_elasticsearch.additional_properties = _src
        return get_admin_dashboard_response_200_system_elasticsearch

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
