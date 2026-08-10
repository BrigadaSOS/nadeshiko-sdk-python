from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserExportResponseTruncated")


@_attrs_define
class UserExportResponseTruncated:
    """Which sections were cut short. The export is assembled and returned as a single JSON
    body, so each section has a ceiling: 50000 activity entries, 5000 reports, 1000
    collections, and 50000 collection segment references in total. A `true` here means more
    data exists than the response carries.

        Attributes:
            activity (bool):
            collections (bool):
            collection_segments (bool):
            reports (bool):
    """

    activity: bool
    collections: bool
    collection_segments: bool
    reports: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity = self.activity

        collections = self.collections

        collection_segments = self.collection_segments

        reports = self.reports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "activity": activity,
                "collections": collections,
                "collectionSegments": collection_segments,
                "reports": reports,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        activity = _src.pop("activity")

        collections = _src.pop("collections")

        collection_segments = _src.pop("collectionSegments")

        reports = _src.pop("reports")

        user_export_response_truncated = cls(
            activity=activity,
            collections=collections,
            collection_segments=collection_segments,
            reports=reports,
        )

        user_export_response_truncated.additional_properties = _src
        return user_export_response_truncated

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
