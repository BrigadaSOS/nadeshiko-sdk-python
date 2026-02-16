from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.segment_update_request_status import SegmentUpdateRequestStatus
from ..models.segment_update_request_storage import SegmentUpdateRequestStorage
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.segment_update_request_en import SegmentUpdateRequestEn
    from ..models.segment_update_request_es import SegmentUpdateRequestEs
    from ..models.segment_update_request_ja import SegmentUpdateRequestJa


T = TypeVar("T", bound="SegmentUpdateRequest")


@_attrs_define
class SegmentUpdateRequest:
    """All fields are optional for partial updates

    Attributes:
        position (int | Unset): Position of the segment within the episode Example: 1133.
        status (SegmentUpdateRequestStatus | Unset): Segment status Default: SegmentUpdateRequestStatus.ACTIVE. Example:
            ACTIVE.
        start_time (str | Unset): Timestamp in H:MM:SS.ffffff format indicating when the segment starts Example:
            0:33:27.255000.
        end_time (str | Unset): Timestamp in H:MM:SS.ffffff format indicating when the segment ends Example:
            0:33:28.464000.
        ja (SegmentUpdateRequestJa | Unset):
        es (SegmentUpdateRequestEs | Unset):
        en (SegmentUpdateRequestEn | Unset):
        is_nsfw (bool | Unset): Whether the segment contains NSFW content Default: False.
        storage (SegmentUpdateRequestStorage | Unset): Storage backend for segment assets Default:
            SegmentUpdateRequestStorage.R2. Example: R2.
        hashed_id (str | Unset): Hash identifier for the segment (from segment JSON) Example: 0d39e46b14.
    """

    position: int | Unset = UNSET
    status: SegmentUpdateRequestStatus | Unset = SegmentUpdateRequestStatus.ACTIVE
    start_time: str | Unset = UNSET
    end_time: str | Unset = UNSET
    ja: SegmentUpdateRequestJa | Unset = UNSET
    es: SegmentUpdateRequestEs | Unset = UNSET
    en: SegmentUpdateRequestEn | Unset = UNSET
    is_nsfw: bool | Unset = False
    storage: SegmentUpdateRequestStorage | Unset = SegmentUpdateRequestStorage.R2
    hashed_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        position = self.position

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        start_time = self.start_time

        end_time = self.end_time

        ja: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ja, Unset):
            ja = self.ja.to_dict()

        es: dict[str, Any] | Unset = UNSET
        if not isinstance(self.es, Unset):
            es = self.es.to_dict()

        en: dict[str, Any] | Unset = UNSET
        if not isinstance(self.en, Unset):
            en = self.en.to_dict()

        is_nsfw = self.is_nsfw

        storage: str | Unset = UNSET
        if not isinstance(self.storage, Unset):
            storage = self.storage.value

        hashed_id = self.hashed_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if position is not UNSET:
            field_dict["position"] = position
        if status is not UNSET:
            field_dict["status"] = status
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if ja is not UNSET:
            field_dict["ja"] = ja
        if es is not UNSET:
            field_dict["es"] = es
        if en is not UNSET:
            field_dict["en"] = en
        if is_nsfw is not UNSET:
            field_dict["isNsfw"] = is_nsfw
        if storage is not UNSET:
            field_dict["storage"] = storage
        if hashed_id is not UNSET:
            field_dict["hashedId"] = hashed_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.segment_update_request_en import SegmentUpdateRequestEn
        from ..models.segment_update_request_es import SegmentUpdateRequestEs
        from ..models.segment_update_request_ja import SegmentUpdateRequestJa

        d = dict(src_dict)
        position = d.pop("position", UNSET)

        _status = d.pop("status", UNSET)
        status: SegmentUpdateRequestStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SegmentUpdateRequestStatus(_status)

        start_time = d.pop("startTime", UNSET)

        end_time = d.pop("endTime", UNSET)

        _ja = d.pop("ja", UNSET)
        ja: SegmentUpdateRequestJa | Unset
        if isinstance(_ja, Unset):
            ja = UNSET
        else:
            ja = SegmentUpdateRequestJa.from_dict(_ja)

        _es = d.pop("es", UNSET)
        es: SegmentUpdateRequestEs | Unset
        if isinstance(_es, Unset):
            es = UNSET
        else:
            es = SegmentUpdateRequestEs.from_dict(_es)

        _en = d.pop("en", UNSET)
        en: SegmentUpdateRequestEn | Unset
        if isinstance(_en, Unset):
            en = UNSET
        else:
            en = SegmentUpdateRequestEn.from_dict(_en)

        is_nsfw = d.pop("isNsfw", UNSET)

        _storage = d.pop("storage", UNSET)
        storage: SegmentUpdateRequestStorage | Unset
        if isinstance(_storage, Unset):
            storage = UNSET
        else:
            storage = SegmentUpdateRequestStorage(_storage)

        hashed_id = d.pop("hashedId", UNSET)

        segment_update_request = cls(
            position=position,
            status=status,
            start_time=start_time,
            end_time=end_time,
            ja=ja,
            es=es,
            en=en,
            is_nsfw=is_nsfw,
            storage=storage,
            hashed_id=hashed_id,
        )

        segment_update_request.additional_properties = d
        return segment_update_request

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
