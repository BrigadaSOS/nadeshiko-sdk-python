from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.segment_update_request_status import SegmentUpdateRequestStatus
from ..models.segment_update_request_storage import SegmentUpdateRequestStorage
from ..types import UNSET, Unset






T = TypeVar("T", bound="SegmentUpdateRequest")



@_attrs_define
class SegmentUpdateRequest:
    """ All fields are optional for partial updates

        Attributes:
            position (int | Unset): Position of the segment within the episode Example: 1133.
            status (SegmentUpdateRequestStatus | Unset): Segment status (default is 1=Active) Default:
                SegmentUpdateRequestStatus.VALUE_1. Example: 1.
            start_time (str | Unset): Timestamp in H:MM:SS.ffffff format indicating when the segment starts Example:
                2007.255.
            end_time (str | Unset): Timestamp in H:MM:SS.ffffff format indicating when the segment ends Example: 2008.464.
            content (str | Unset): Original Japanese content of the segment Example: 僕は僕で、君は君だ。.
            content_spanish (str | Unset): Spanish translation of the segment content Example: Yo soy yo, y tú eres tú..
            content_spanish_mt (bool | Unset): Whether the Spanish translation was machine-translated Default: False.
            content_english (str | Unset): English translation of the segment content Example: I am me, and you are you..
            content_english_mt (bool | Unset): Whether the English translation was machine-translated Default: False.
            is_nsfw (bool | Unset): Whether the segment contains NSFW content Default: False.
            storage (SegmentUpdateRequestStorage | Unset): Storage backend for segment assets Default:
                SegmentUpdateRequestStorage.R2. Example: r2.
            hashed_id (str | Unset): Hash identifier for the segment (from segment JSON) Example: 0d39e46b14.
            actor_ja (str | Unset): Japanese voice actor name Example: Mamoru Miyano.
            actor_es (str | Unset): Spanish voice actor name Example: Alejandro Levis.
            actor_en (str | Unset): English voice actor name Example: J. Michael Tatum.
     """

    position: int | Unset = UNSET
    status: SegmentUpdateRequestStatus | Unset = SegmentUpdateRequestStatus.VALUE_1
    start_time: str | Unset = UNSET
    end_time: str | Unset = UNSET
    content: str | Unset = UNSET
    content_spanish: str | Unset = UNSET
    content_spanish_mt: bool | Unset = False
    content_english: str | Unset = UNSET
    content_english_mt: bool | Unset = False
    is_nsfw: bool | Unset = False
    storage: SegmentUpdateRequestStorage | Unset = SegmentUpdateRequestStorage.R2
    hashed_id: str | Unset = UNSET
    actor_ja: str | Unset = UNSET
    actor_es: str | Unset = UNSET
    actor_en: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        position = self.position

        status: int | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        start_time = self.start_time

        end_time = self.end_time

        content = self.content

        content_spanish = self.content_spanish

        content_spanish_mt = self.content_spanish_mt

        content_english = self.content_english

        content_english_mt = self.content_english_mt

        is_nsfw = self.is_nsfw

        storage: str | Unset = UNSET
        if not isinstance(self.storage, Unset):
            storage = self.storage.value


        hashed_id = self.hashed_id

        actor_ja = self.actor_ja

        actor_es = self.actor_es

        actor_en = self.actor_en


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if position is not UNSET:
            field_dict["position"] = position
        if status is not UNSET:
            field_dict["status"] = status
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if content is not UNSET:
            field_dict["content"] = content
        if content_spanish is not UNSET:
            field_dict["contentSpanish"] = content_spanish
        if content_spanish_mt is not UNSET:
            field_dict["contentSpanishMt"] = content_spanish_mt
        if content_english is not UNSET:
            field_dict["contentEnglish"] = content_english
        if content_english_mt is not UNSET:
            field_dict["contentEnglishMt"] = content_english_mt
        if is_nsfw is not UNSET:
            field_dict["isNsfw"] = is_nsfw
        if storage is not UNSET:
            field_dict["storage"] = storage
        if hashed_id is not UNSET:
            field_dict["hashedId"] = hashed_id
        if actor_ja is not UNSET:
            field_dict["actorJa"] = actor_ja
        if actor_es is not UNSET:
            field_dict["actorEs"] = actor_es
        if actor_en is not UNSET:
            field_dict["actorEn"] = actor_en

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        position = d.pop("position", UNSET)

        _status = d.pop("status", UNSET)
        status: SegmentUpdateRequestStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = SegmentUpdateRequestStatus(_status)




        start_time = d.pop("startTime", UNSET)

        end_time = d.pop("endTime", UNSET)

        content = d.pop("content", UNSET)

        content_spanish = d.pop("contentSpanish", UNSET)

        content_spanish_mt = d.pop("contentSpanishMt", UNSET)

        content_english = d.pop("contentEnglish", UNSET)

        content_english_mt = d.pop("contentEnglishMt", UNSET)

        is_nsfw = d.pop("isNsfw", UNSET)

        _storage = d.pop("storage", UNSET)
        storage: SegmentUpdateRequestStorage | Unset
        if isinstance(_storage,  Unset):
            storage = UNSET
        else:
            storage = SegmentUpdateRequestStorage(_storage)




        hashed_id = d.pop("hashedId", UNSET)

        actor_ja = d.pop("actorJa", UNSET)

        actor_es = d.pop("actorEs", UNSET)

        actor_en = d.pop("actorEn", UNSET)

        segment_update_request = cls(
            position=position,
            status=status,
            start_time=start_time,
            end_time=end_time,
            content=content,
            content_spanish=content_spanish,
            content_spanish_mt=content_spanish_mt,
            content_english=content_english,
            content_english_mt=content_english_mt,
            is_nsfw=is_nsfw,
            storage=storage,
            hashed_id=hashed_id,
            actor_ja=actor_ja,
            actor_es=actor_es,
            actor_en=actor_en,
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
