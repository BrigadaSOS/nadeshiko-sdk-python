from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.report import Report
    from ..models.review_check_run import ReviewCheckRun


T = TypeVar("T", bound="GetAdminReviewRunResponse200")


@_attrs_define
class GetAdminReviewRunResponse200:
    """
    Attributes:
        run (ReviewCheckRun):
        reports (list[Report]):
    """

    run: ReviewCheckRun
    reports: list[Report]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run = self.run.to_dict()

        reports = []
        for reports_item_data in self.reports:
            reports_item = reports_item_data.to_dict()
            reports.append(reports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "run": run,
                "reports": reports,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.report import Report
        from ..models.review_check_run import ReviewCheckRun

        d = dict(src_dict)
        run = ReviewCheckRun.from_dict(d.pop("run"))

        reports = []
        _reports = d.pop("reports")
        for reports_item_data in _reports:
            reports_item = Report.from_dict(reports_item_data)

            reports.append(reports_item)

        get_admin_review_run_response_200 = cls(
            run=run,
            reports=reports,
        )

        get_admin_review_run_response_200.additional_properties = d
        return get_admin_review_run_response_200

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
