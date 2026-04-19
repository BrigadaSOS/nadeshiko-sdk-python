from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.media_audit_target_type import MediaAuditTargetType, check_media_audit_target_type

if TYPE_CHECKING:
    from ..models.media_audit_latest_run_type_0 import MediaAuditLatestRunType0
    from ..models.media_audit_threshold import MediaAuditThreshold
    from ..models.media_audit_threshold_schema_item import MediaAuditThresholdSchemaItem


T = TypeVar("T", bound="MediaAudit")


@_attrs_define
class MediaAudit:
    """
    Attributes:
        id (int): Audit ID
        name (str): Unique audit identifier Example: lowSegmentMedia.
        label (str): Human-readable label Example: Low Segment Media.
        description (str): What this audit does
        target_type (MediaAuditTargetType): What level this audit operates on
        threshold (MediaAuditThreshold): Current threshold configuration
        enabled (bool): Whether this audit is active
        threshold_schema (list[MediaAuditThresholdSchemaItem]): Schema for threshold fields (from registry)
        latest_run (MediaAuditLatestRunType0 | None): Latest run info for this audit
        created_at (datetime.datetime | None):
        updated_at (datetime.datetime | None):
    """

    id: int
    name: str
    label: str
    description: str
    target_type: MediaAuditTargetType
    threshold: MediaAuditThreshold
    enabled: bool
    threshold_schema: list[MediaAuditThresholdSchemaItem]
    latest_run: MediaAuditLatestRunType0 | None
    created_at: datetime.datetime | None
    updated_at: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.media_audit_latest_run_type_0 import MediaAuditLatestRunType0

        id = self.id

        name = self.name

        label = self.label

        description = self.description

        target_type: str = self.target_type

        threshold = self.threshold.to_dict()

        enabled = self.enabled

        threshold_schema = []
        for threshold_schema_item_data in self.threshold_schema:
            threshold_schema_item = threshold_schema_item_data.to_dict()
            threshold_schema.append(threshold_schema_item)

        latest_run: dict[str, Any] | None
        if isinstance(self.latest_run, MediaAuditLatestRunType0):
            latest_run = self.latest_run.to_dict()
        else:
            latest_run = self.latest_run

        created_at: None | str
        if isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str
        if isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "label": label,
                "description": description,
                "targetType": target_type,
                "threshold": threshold,
                "enabled": enabled,
                "thresholdSchema": threshold_schema,
                "latestRun": latest_run,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_audit_latest_run_type_0 import MediaAuditLatestRunType0
        from ..models.media_audit_threshold import MediaAuditThreshold
        from ..models.media_audit_threshold_schema_item import MediaAuditThresholdSchemaItem

        _src = dict(src_dict)
        id = _src.pop("id")

        name = _src.pop("name")

        label = _src.pop("label")

        description = _src.pop("description")

        target_type = check_media_audit_target_type(_src.pop("targetType"))

        threshold = MediaAuditThreshold.from_dict(_src.pop("threshold"))

        enabled = _src.pop("enabled")

        threshold_schema = []
        _threshold_schema = _src.pop("thresholdSchema")
        for threshold_schema_item_data in _threshold_schema:
            threshold_schema_item = MediaAuditThresholdSchemaItem.from_dict(
                threshold_schema_item_data
            )

            threshold_schema.append(threshold_schema_item)

        def _parse_latest_run(data: object) -> MediaAuditLatestRunType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                latest_run_type_0 = MediaAuditLatestRunType0.from_dict(data)

                return latest_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MediaAuditLatestRunType0 | None, data)

        latest_run = _parse_latest_run(_src.pop("latestRun"))

        def _parse_created_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        created_at = _parse_created_at(_src.pop("createdAt"))

        def _parse_updated_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        updated_at = _parse_updated_at(_src.pop("updatedAt"))

        media_audit = cls(
            id=id,
            name=name,
            label=label,
            description=description,
            target_type=target_type,
            threshold=threshold,
            enabled=enabled,
            threshold_schema=threshold_schema,
            latest_run=latest_run,
            created_at=created_at,
            updated_at=updated_at,
        )

        media_audit.additional_properties = _src
        return media_audit

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
