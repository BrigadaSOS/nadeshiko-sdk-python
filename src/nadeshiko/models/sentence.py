from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.basic_info import BasicInfo
    from ..models.media_info_path import MediaInfoPath
    from ..models.segment_info import SegmentInfo


T = TypeVar("T", bound="Sentence")


@_attrs_define
class Sentence:
    """A complete sentence result combining basic info, segment details, and media paths

    Attributes:
        basic_info (BasicInfo): Basic anime/media information included in search results
        segment_info (SegmentInfo): Detailed information about a subtitle segment
        media_info (MediaInfoPath): URLs to media resources for a segment
    """

    basic_info: BasicInfo
    segment_info: SegmentInfo
    media_info: MediaInfoPath
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        basic_info = self.basic_info.to_dict()

        segment_info = self.segment_info.to_dict()

        media_info = self.media_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "basic_info": basic_info,
                "segment_info": segment_info,
                "media_info": media_info,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.basic_info import BasicInfo
        from ..models.media_info_path import MediaInfoPath
        from ..models.segment_info import SegmentInfo

        d = dict(src_dict)
        basic_info = BasicInfo.from_dict(d.pop("basic_info"))

        segment_info = SegmentInfo.from_dict(d.pop("segment_info"))

        media_info = MediaInfoPath.from_dict(d.pop("media_info"))

        sentence = cls(
            basic_info=basic_info,
            segment_info=segment_info,
            media_info=media_info,
        )

        sentence.additional_properties = d
        return sentence

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
