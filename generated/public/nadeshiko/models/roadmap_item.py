from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.roadmap_item_kind import RoadmapItemKind, check_roadmap_item_kind
from ..models.roadmap_item_status import RoadmapItemStatus, check_roadmap_item_status
from ..types import UNSET, Unset

T = TypeVar("T", bound="RoadmapItem")


@_attrs_define
class RoadmapItem:
    """
    Attributes:
        id (UUID):
        kind (RoadmapItemKind):
        status (RoadmapItemStatus):
        title (str):
        description (str):
        source_url (None | str):
        cover_url (None | str):
        target_date (datetime.date | None):
        introduced_in_version (None | str): Nadeshiko version that introduced this feature.
        sort_order (int):
        created_at (datetime.datetime):
        proposer_name (None | str): Optional public credit chosen by the proposer or an admin.
        requester_user_id (int | None | Unset): Present on admin responses only.
    """

    id: UUID
    kind: RoadmapItemKind
    status: RoadmapItemStatus
    title: str
    description: str
    source_url: None | str
    cover_url: None | str
    target_date: datetime.date | None
    introduced_in_version: None | str
    sort_order: int
    created_at: datetime.datetime
    proposer_name: None | str
    requester_user_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        kind: str = self.kind

        status: str = self.status

        title = self.title

        description = self.description

        source_url: None | str
        source_url = self.source_url

        cover_url: None | str
        cover_url = self.cover_url

        target_date: None | str
        if isinstance(self.target_date, datetime.date):
            target_date = self.target_date.isoformat()
        else:
            target_date = self.target_date

        introduced_in_version: None | str
        introduced_in_version = self.introduced_in_version

        sort_order = self.sort_order

        created_at = self.created_at.isoformat()

        proposer_name: None | str
        proposer_name = self.proposer_name

        requester_user_id: int | None | Unset
        if isinstance(self.requester_user_id, Unset):
            requester_user_id = UNSET
        else:
            requester_user_id = self.requester_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "kind": kind,
                "status": status,
                "title": title,
                "description": description,
                "sourceUrl": source_url,
                "coverUrl": cover_url,
                "targetDate": target_date,
                "introducedInVersion": introduced_in_version,
                "sortOrder": sort_order,
                "createdAt": created_at,
                "proposerName": proposer_name,
            }
        )
        if requester_user_id is not UNSET:
            field_dict["requesterUserId"] = requester_user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        id = UUID(_src.pop("id"))

        kind = check_roadmap_item_kind(_src.pop("kind"))

        status = check_roadmap_item_status(_src.pop("status"))

        title = _src.pop("title")

        description = _src.pop("description")

        def _parse_source_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        source_url = _parse_source_url(_src.pop("sourceUrl"))

        def _parse_cover_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cover_url = _parse_cover_url(_src.pop("coverUrl"))

        def _parse_target_date(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                target_date_type_0 = datetime.date.fromisoformat(data)

                return target_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        target_date = _parse_target_date(_src.pop("targetDate"))

        def _parse_introduced_in_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        introduced_in_version = _parse_introduced_in_version(_src.pop("introducedInVersion"))

        sort_order = _src.pop("sortOrder")

        created_at = datetime.datetime.fromisoformat(_src.pop("createdAt"))

        def _parse_proposer_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        proposer_name = _parse_proposer_name(_src.pop("proposerName"))

        def _parse_requester_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        requester_user_id = _parse_requester_user_id(_src.pop("requesterUserId", UNSET))

        roadmap_item = cls(
            id=id,
            kind=kind,
            status=status,
            title=title,
            description=description,
            source_url=source_url,
            cover_url=cover_url,
            target_date=target_date,
            introduced_in_version=introduced_in_version,
            sort_order=sort_order,
            created_at=created_at,
            proposer_name=proposer_name,
            requester_user_id=requester_user_id,
        )

        roadmap_item.additional_properties = _src
        return roadmap_item

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
