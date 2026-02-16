from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.segment_create_request_status import SegmentCreateRequestStatus
from ..models.segment_create_request_storage import SegmentCreateRequestStorage
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.segment_create_request_text_en import SegmentCreateRequestTextEn
    from ..models.segment_create_request_text_es import SegmentCreateRequestTextEs
    from ..models.segment_create_request_text_ja import SegmentCreateRequestTextJa


T = TypeVar("T", bound="SegmentCreateRequest")


@_attrs_define
class SegmentCreateRequest:
    """
    Attributes:
        position (int): Position of the segment within the episode Example: 1133.
        start_time (str): Timestamp in H:MM:SS.ffffff format indicating when the segment starts Example: 0:33:27.255000.
        end_time (str): Timestamp in H:MM:SS.ffffff format indicating when the segment ends Example: 0:33:28.464000.
        text_ja (SegmentCreateRequestTextJa):
        storage (SegmentCreateRequestStorage): Storage backend for segment assets Default:
            SegmentCreateRequestStorage.R2. Example: R2.
        hashed_id (str): Hash identifier for the segment (from segment JSON) Example: 0d39e46b14.
        status (SegmentCreateRequestStatus | Unset): Segment status Default: SegmentCreateRequestStatus.ACTIVE. Example:
            ACTIVE.
        text_es (SegmentCreateRequestTextEs | Unset):
        text_en (SegmentCreateRequestTextEn | Unset):
        is_nsfw (bool | Unset): Whether the segment contains NSFW content Default: False.
    """

    position: int
    start_time: str
    end_time: str
    text_ja: SegmentCreateRequestTextJa
    hashed_id: str
    storage: SegmentCreateRequestStorage = SegmentCreateRequestStorage.R2
    status: SegmentCreateRequestStatus | Unset = SegmentCreateRequestStatus.ACTIVE
    text_es: SegmentCreateRequestTextEs | Unset = UNSET
    text_en: SegmentCreateRequestTextEn | Unset = UNSET
    is_nsfw: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        position = self.position

        start_time = self.start_time

        end_time = self.end_time

        text_ja = self.text_ja.to_dict()

        storage = self.storage.value

        hashed_id = self.hashed_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        text_es: dict[str, Any] | Unset = UNSET
        if not isinstance(self.text_es, Unset):
            text_es = self.text_es.to_dict()

        text_en: dict[str, Any] | Unset = UNSET
        if not isinstance(self.text_en, Unset):
            text_en = self.text_en.to_dict()

        is_nsfw = self.is_nsfw

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position": position,
                "startTime": start_time,
                "endTime": end_time,
                "textJa": text_ja,
                "storage": storage,
                "hashedId": hashed_id,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if text_es is not UNSET:
            field_dict["textEs"] = text_es
        if text_en is not UNSET:
            field_dict["textEn"] = text_en
        if is_nsfw is not UNSET:
            field_dict["isNsfw"] = is_nsfw

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.segment_create_request_text_en import SegmentCreateRequestTextEn
        from ..models.segment_create_request_text_es import SegmentCreateRequestTextEs
        from ..models.segment_create_request_text_ja import SegmentCreateRequestTextJa

        d = dict(src_dict)
        position = d.pop("position")

        start_time = d.pop("startTime")

        end_time = d.pop("endTime")

        text_ja = SegmentCreateRequestTextJa.from_dict(d.pop("textJa"))

        storage = SegmentCreateRequestStorage(d.pop("storage"))

        hashed_id = d.pop("hashedId")

        _status = d.pop("status", UNSET)
        status: SegmentCreateRequestStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SegmentCreateRequestStatus(_status)

        _text_es = d.pop("textEs", UNSET)
        text_es: SegmentCreateRequestTextEs | Unset
        if isinstance(_text_es, Unset):
            text_es = UNSET
        else:
            text_es = SegmentCreateRequestTextEs.from_dict(_text_es)

        _text_en = d.pop("textEn", UNSET)
        text_en: SegmentCreateRequestTextEn | Unset
        if isinstance(_text_en, Unset):
            text_en = UNSET
        else:
            text_en = SegmentCreateRequestTextEn.from_dict(_text_en)

        is_nsfw = d.pop("isNsfw", UNSET)

        segment_create_request = cls(
            position=position,
            start_time=start_time,
            end_time=end_time,
            text_ja=text_ja,
            storage=storage,
            hashed_id=hashed_id,
            status=status,
            text_es=text_es,
            text_en=text_en,
            is_nsfw=is_nsfw,
        )

        segment_create_request.additional_properties = d
        return segment_create_request

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
