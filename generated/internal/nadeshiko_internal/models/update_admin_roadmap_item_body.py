from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_admin_roadmap_item_body_kind import (
    UpdateAdminRoadmapItemBodyKind,
    check_update_admin_roadmap_item_body_kind,
)
from ..models.update_admin_roadmap_item_body_status import (
    UpdateAdminRoadmapItemBodyStatus,
    check_update_admin_roadmap_item_body_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAdminRoadmapItemBody")


@_attrs_define
class UpdateAdminRoadmapItemBody:
    """
    Attributes:
        kind (UpdateAdminRoadmapItemBodyKind | Unset):
        status (UpdateAdminRoadmapItemBodyStatus | Unset):
        title (str | Unset):
        description (str | Unset):
        source_url (None | str | Unset):
        cover_url (None | str | Unset):
        target_date (datetime.date | None | Unset):
        introduced_in_version (None | str | Unset):
        sort_order (int | Unset):
        proposer_name (None | str | Unset):
    """

    kind: UpdateAdminRoadmapItemBodyKind | Unset = UNSET
    status: UpdateAdminRoadmapItemBodyStatus | Unset = UNSET
    title: str | Unset = UNSET
    description: str | Unset = UNSET
    source_url: None | str | Unset = UNSET
    cover_url: None | str | Unset = UNSET
    target_date: datetime.date | None | Unset = UNSET
    introduced_in_version: None | str | Unset = UNSET
    sort_order: int | Unset = UNSET
    proposer_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        title = self.title

        description = self.description

        source_url: None | str | Unset
        if isinstance(self.source_url, Unset):
            source_url = UNSET
        else:
            source_url = self.source_url

        cover_url: None | str | Unset
        if isinstance(self.cover_url, Unset):
            cover_url = UNSET
        else:
            cover_url = self.cover_url

        target_date: None | str | Unset
        if isinstance(self.target_date, Unset):
            target_date = UNSET
        elif isinstance(self.target_date, datetime.date):
            target_date = self.target_date.isoformat()
        else:
            target_date = self.target_date

        introduced_in_version: None | str | Unset
        if isinstance(self.introduced_in_version, Unset):
            introduced_in_version = UNSET
        else:
            introduced_in_version = self.introduced_in_version

        sort_order = self.sort_order

        proposer_name: None | str | Unset
        if isinstance(self.proposer_name, Unset):
            proposer_name = UNSET
        else:
            proposer_name = self.proposer_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if status is not UNSET:
            field_dict["status"] = status
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if source_url is not UNSET:
            field_dict["sourceUrl"] = source_url
        if cover_url is not UNSET:
            field_dict["coverUrl"] = cover_url
        if target_date is not UNSET:
            field_dict["targetDate"] = target_date
        if introduced_in_version is not UNSET:
            field_dict["introducedInVersion"] = introduced_in_version
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if proposer_name is not UNSET:
            field_dict["proposerName"] = proposer_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        _kind = _src.pop("kind", UNSET)
        kind: UpdateAdminRoadmapItemBodyKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_update_admin_roadmap_item_body_kind(_kind)

        _status = _src.pop("status", UNSET)
        status: UpdateAdminRoadmapItemBodyStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_update_admin_roadmap_item_body_status(_status)

        title = _src.pop("title", UNSET)

        description = _src.pop("description", UNSET)

        def _parse_source_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_url = _parse_source_url(_src.pop("sourceUrl", UNSET))

        def _parse_cover_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cover_url = _parse_cover_url(_src.pop("coverUrl", UNSET))

        def _parse_target_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                target_date_type_0 = datetime.date.fromisoformat(data)

                return target_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        target_date = _parse_target_date(_src.pop("targetDate", UNSET))

        def _parse_introduced_in_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        introduced_in_version = _parse_introduced_in_version(_src.pop("introducedInVersion", UNSET))

        sort_order = _src.pop("sortOrder", UNSET)

        def _parse_proposer_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        proposer_name = _parse_proposer_name(_src.pop("proposerName", UNSET))

        update_admin_roadmap_item_body = cls(
            kind=kind,
            status=status,
            title=title,
            description=description,
            source_url=source_url,
            cover_url=cover_url,
            target_date=target_date,
            introduced_in_version=introduced_in_version,
            sort_order=sort_order,
            proposer_name=proposer_name,
        )

        update_admin_roadmap_item_body.additional_properties = _src
        return update_admin_roadmap_item_body

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
