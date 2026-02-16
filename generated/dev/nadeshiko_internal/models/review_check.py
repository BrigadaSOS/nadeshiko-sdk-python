from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.review_check_target_type import ReviewCheckTargetType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.review_check_latest_run_type_0 import ReviewCheckLatestRunType0
    from ..models.review_check_threshold import ReviewCheckThreshold
    from ..models.review_check_threshold_schema_item import ReviewCheckThresholdSchemaItem


T = TypeVar("T", bound="ReviewCheck")


@_attrs_define
class ReviewCheck:
    """
    Attributes:
        id (int): Check ID
        name (str): Unique check identifier Example: lowSegmentMedia.
        label (str): Human-readable label Example: Low Segment Media.
        description (str): What this check does
        target_type (ReviewCheckTargetType): What level this check operates on
        threshold (ReviewCheckThreshold): Current threshold configuration
        enabled (bool): Whether this check is active
        threshold_schema (list[ReviewCheckThresholdSchemaItem] | Unset): Schema for threshold fields (from registry)
        latest_run (None | ReviewCheckLatestRunType0 | Unset): Latest run info for this check
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | None | Unset):
    """

    id: int
    name: str
    label: str
    description: str
    target_type: ReviewCheckTargetType
    threshold: ReviewCheckThreshold
    enabled: bool
    threshold_schema: list[ReviewCheckThresholdSchemaItem] | Unset = UNSET
    latest_run: None | ReviewCheckLatestRunType0 | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.review_check_latest_run_type_0 import ReviewCheckLatestRunType0

        id = self.id

        name = self.name

        label = self.label

        description = self.description

        target_type = self.target_type.value

        threshold = self.threshold.to_dict()

        enabled = self.enabled

        threshold_schema: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.threshold_schema, Unset):
            threshold_schema = []
            for threshold_schema_item_data in self.threshold_schema:
                threshold_schema_item = threshold_schema_item_data.to_dict()
                threshold_schema.append(threshold_schema_item)

        latest_run: dict[str, Any] | None | Unset
        if isinstance(self.latest_run, Unset):
            latest_run = UNSET
        elif isinstance(self.latest_run, ReviewCheckLatestRunType0):
            latest_run = self.latest_run.to_dict()
        else:
            latest_run = self.latest_run

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
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
            }
        )
        if threshold_schema is not UNSET:
            field_dict["thresholdSchema"] = threshold_schema
        if latest_run is not UNSET:
            field_dict["latestRun"] = latest_run
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.review_check_latest_run_type_0 import ReviewCheckLatestRunType0
        from ..models.review_check_threshold import ReviewCheckThreshold
        from ..models.review_check_threshold_schema_item import ReviewCheckThresholdSchemaItem

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        label = d.pop("label")

        description = d.pop("description")

        target_type = ReviewCheckTargetType(d.pop("targetType"))

        threshold = ReviewCheckThreshold.from_dict(d.pop("threshold"))

        enabled = d.pop("enabled")

        _threshold_schema = d.pop("thresholdSchema", UNSET)
        threshold_schema: list[ReviewCheckThresholdSchemaItem] | Unset = UNSET
        if _threshold_schema is not UNSET:
            threshold_schema = []
            for threshold_schema_item_data in _threshold_schema:
                threshold_schema_item = ReviewCheckThresholdSchemaItem.from_dict(
                    threshold_schema_item_data
                )

                threshold_schema.append(threshold_schema_item)

        def _parse_latest_run(data: object) -> None | ReviewCheckLatestRunType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                latest_run_type_0 = ReviewCheckLatestRunType0.from_dict(data)

                return latest_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReviewCheckLatestRunType0 | Unset, data)

        latest_run = _parse_latest_run(d.pop("latestRun", UNSET))

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))

        review_check = cls(
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

        review_check.additional_properties = d
        return review_check

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
