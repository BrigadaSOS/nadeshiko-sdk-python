from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_report_request_reason import CreateReportRequestReason
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.report_target_media import ReportTargetMedia
    from ..models.report_target_segment_input import ReportTargetSegmentInput


T = TypeVar("T", bound="CreateReportRequest")


@_attrs_define
class CreateReportRequest:
    """
    Attributes:
        target (ReportTargetMedia | ReportTargetSegmentInput):
        reason (CreateReportRequestReason): Reason for the report Example: WRONG_TRANSLATION.
        description (str | Unset): Optional description with additional details Example: The translation doesn't match
            the spoken Japanese.
    """

    target: ReportTargetMedia | ReportTargetSegmentInput
    reason: CreateReportRequestReason
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.report_target_media import ReportTargetMedia

        target: dict[str, Any]
        if isinstance(self.target, ReportTargetMedia):
            target = self.target.to_dict()
        else:
            target = self.target.to_dict()

        reason = self.reason.value

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "target": target,
                "reason": reason,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.report_target_media import ReportTargetMedia
        from ..models.report_target_segment_input import ReportTargetSegmentInput

        d = dict(src_dict)

        def _parse_target(data: object) -> ReportTargetMedia | ReportTargetSegmentInput:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_report_target_type_0 = ReportTargetMedia.from_dict(data)

                return componentsschemas_user_report_target_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_user_report_target_type_1 = ReportTargetSegmentInput.from_dict(data)

            return componentsschemas_user_report_target_type_1

        target = _parse_target(d.pop("target"))

        reason = CreateReportRequestReason(d.pop("reason"))

        description = d.pop("description", UNSET)

        create_report_request = cls(
            target=target,
            reason=reason,
            description=description,
        )

        create_report_request.additional_properties = d
        return create_report_request

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
