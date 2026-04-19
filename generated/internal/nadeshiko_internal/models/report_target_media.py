from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.report_target_media_type import ReportTargetMediaType, check_report_target_media_type

T = TypeVar("T", bound="ReportTargetMedia")


@_attrs_define
class ReportTargetMedia:
    """
    Attributes:
        type_ (ReportTargetMediaType): Report target type Example: MEDIA.
        media_public_id (str): publicId of the media this report targets Example: V1StGXR8_Z5d.
    """

    type_: ReportTargetMediaType
    media_public_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        media_public_id = self.media_public_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "mediaPublicId": media_public_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        type_ = check_report_target_media_type(_src.pop("type"))

        media_public_id = _src.pop("mediaPublicId")

        report_target_media = cls(
            type_=type_,
            media_public_id=media_public_id,
        )

        report_target_media.additional_properties = _src
        return report_target_media

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
