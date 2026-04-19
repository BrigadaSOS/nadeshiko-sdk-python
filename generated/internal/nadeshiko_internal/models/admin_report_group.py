from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.report_status import ReportStatus, check_report_status

if TYPE_CHECKING:
    from ..models.admin_report_group_item import AdminReportGroupItem
    from ..models.report_target_episode import ReportTargetEpisode
    from ..models.report_target_media import ReportTargetMedia
    from ..models.report_target_segment import ReportTargetSegment


T = TypeVar("T", bound="AdminReportGroup")


@_attrs_define
class AdminReportGroup:
    """
    Attributes:
        target (ReportTargetEpisode | ReportTargetMedia | ReportTargetSegment):
        media_name (str): Display name of the target media (romaji) Example: Bocchi the Rock!.
        status (ReportStatus): Current status of a report Example: OPEN.
        report_count (int): Total number of individual reports in this group Example: 3.
        reporter_count (int): Number of distinct users who reported this target Example: 2.
        first_reported_at (datetime.datetime): When the earliest report in this group was created
        last_status_change (datetime.datetime | None): When the most recent status change occurred in this group
        reports (list[AdminReportGroupItem]): Individual reports within this group
    """

    target: ReportTargetEpisode | ReportTargetMedia | ReportTargetSegment
    media_name: str
    status: ReportStatus
    report_count: int
    reporter_count: int
    first_reported_at: datetime.datetime
    last_status_change: datetime.datetime | None
    reports: list[AdminReportGroupItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.report_target_episode import ReportTargetEpisode
        from ..models.report_target_media import ReportTargetMedia

        target: dict[str, Any]
        if isinstance(self.target, ReportTargetMedia) or isinstance(
            self.target, ReportTargetEpisode
        ):
            target = self.target.to_dict()
        else:
            target = self.target.to_dict()

        media_name = self.media_name

        status: str = self.status

        report_count = self.report_count

        reporter_count = self.reporter_count

        first_reported_at = self.first_reported_at.isoformat()

        last_status_change: None | str
        if isinstance(self.last_status_change, datetime.datetime):
            last_status_change = self.last_status_change.isoformat()
        else:
            last_status_change = self.last_status_change

        reports = []
        for reports_item_data in self.reports:
            reports_item = reports_item_data.to_dict()
            reports.append(reports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "target": target,
                "mediaName": media_name,
                "status": status,
                "reportCount": report_count,
                "reporterCount": reporter_count,
                "firstReportedAt": first_reported_at,
                "lastStatusChange": last_status_change,
                "reports": reports,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admin_report_group_item import AdminReportGroupItem
        from ..models.report_target_episode import ReportTargetEpisode
        from ..models.report_target_media import ReportTargetMedia
        from ..models.report_target_segment import ReportTargetSegment

        _src = dict(src_dict)

        def _parse_target(
            data: object,
        ) -> ReportTargetEpisode | ReportTargetMedia | ReportTargetSegment:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_report_target_type_0 = ReportTargetMedia.from_dict(data)

                return componentsschemas_report_target_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_report_target_type_1 = ReportTargetEpisode.from_dict(data)

                return componentsschemas_report_target_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_report_target_type_2 = ReportTargetSegment.from_dict(data)

            return componentsschemas_report_target_type_2

        target = _parse_target(_src.pop("target"))

        media_name = _src.pop("mediaName")

        status = check_report_status(_src.pop("status"))

        report_count = _src.pop("reportCount")

        reporter_count = _src.pop("reporterCount")

        first_reported_at = isoparse(_src.pop("firstReportedAt"))

        def _parse_last_status_change(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_status_change_type_0 = isoparse(data)

                return last_status_change_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_status_change = _parse_last_status_change(_src.pop("lastStatusChange"))

        reports = []
        _reports = _src.pop("reports")
        for reports_item_data in _reports:
            reports_item = AdminReportGroupItem.from_dict(reports_item_data)

            reports.append(reports_item)

        admin_report_group = cls(
            target=target,
            media_name=media_name,
            status=status,
            report_count=report_count,
            reporter_count=reporter_count,
            first_reported_at=first_reported_at,
            last_status_change=last_status_change,
            reports=reports,
        )

        admin_report_group.additional_properties = _src
        return admin_report_group

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
