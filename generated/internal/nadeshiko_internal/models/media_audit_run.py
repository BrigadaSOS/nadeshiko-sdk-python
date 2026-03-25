from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_audit_run_threshold_used import MediaAuditRunThresholdUsed


T = TypeVar("T", bound="MediaAuditRun")


@_attrs_define
class MediaAuditRun:
    """
    Attributes:
        id (int): Run ID
        audit_name (str): Name of the audit that was run Example: lowSegmentMedia.
        result_count (int): Number of reports created in this run Example: 12.
        threshold_used (MediaAuditRunThresholdUsed): Snapshot of threshold at run time
        created_at (datetime.datetime): When this run was executed
        category (None | str | Unset): Category filter used (ANIME/JDRAMA) or null for all
    """

    id: int
    audit_name: str
    result_count: int
    threshold_used: MediaAuditRunThresholdUsed
    created_at: datetime.datetime
    category: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        audit_name = self.audit_name

        result_count = self.result_count

        threshold_used = self.threshold_used.to_dict()

        created_at = self.created_at.isoformat()

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "auditName": audit_name,
                "resultCount": result_count,
                "thresholdUsed": threshold_used,
                "createdAt": created_at,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_audit_run_threshold_used import MediaAuditRunThresholdUsed

        _src = dict(src_dict)
        id = _src.pop("id")

        audit_name = _src.pop("auditName")

        result_count = _src.pop("resultCount")

        threshold_used = MediaAuditRunThresholdUsed.from_dict(_src.pop("thresholdUsed"))

        created_at = isoparse(_src.pop("createdAt"))

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(_src.pop("category", UNSET))

        media_audit_run = cls(
            id=id,
            audit_name=audit_name,
            result_count=result_count,
            threshold_used=threshold_used,
            created_at=created_at,
            category=category,
        )

        media_audit_run.additional_properties = _src
        return media_audit_run

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
