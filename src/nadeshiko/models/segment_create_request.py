from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.segment_create_request_status import SegmentCreateRequestStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="SegmentCreateRequest")


@_attrs_define
class SegmentCreateRequest:
    """
    Attributes:
        uuid (str): Unique identifier for the segment Example: 3fd94cef-a3e1-31ae-bc8d-e743f03e9c7e.
        position (int): Position of the segment within the episode Example: 1133.
        start_time (str): Timestamp in H:MM:SS.ffffff format indicating when the segment starts Example: 0:33:27.255000.
        end_time (str): Timestamp in H:MM:SS.ffffff format indicating when the segment ends Example: 0:33:28.464000.
        content (str): Original Japanese content of the segment Example: 僕は僕で、君は君だ。.
        status (SegmentCreateRequestStatus | Unset): Segment status (default is 1=Active) Default:
            SegmentCreateRequestStatus.VALUE_1. Example: 1.
        content_spanish (str | Unset): Spanish translation of the segment content Example: Yo soy yo, y tú eres tú..
        content_spanish_mt (bool | Unset): Whether the Spanish translation was machine-translated Default: False.
        content_english (str | Unset): English translation of the segment content Example: I am me, and you are you..
        content_english_mt (bool | Unset): Whether the English translation was machine-translated Default: False.
        is_nsfw (bool | Unset): Whether the segment contains NSFW content Default: False.
        image_url (str | Unset): URL to segment screenshot/image Example: https://example.com/images/segment.jpg.
        audio_url (str | Unset): URL to segment audio file Example: https://example.com/audio/segment.mp3.
        actor_ja (str | Unset): Japanese voice actor name Example: Mamoru Miyano.
        actor_es (str | Unset): Spanish voice actor name Example: Alejandro Levis.
        actor_en (str | Unset): English voice actor name Example: J. Michael Tatum.
    """

    uuid: str
    position: int
    start_time: str
    end_time: str
    content: str
    status: SegmentCreateRequestStatus | Unset = SegmentCreateRequestStatus.VALUE_1
    content_spanish: str | Unset = UNSET
    content_spanish_mt: bool | Unset = False
    content_english: str | Unset = UNSET
    content_english_mt: bool | Unset = False
    is_nsfw: bool | Unset = False
    image_url: str | Unset = UNSET
    audio_url: str | Unset = UNSET
    actor_ja: str | Unset = UNSET
    actor_es: str | Unset = UNSET
    actor_en: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        position = self.position

        start_time = self.start_time

        end_time = self.end_time

        content = self.content

        status: int | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        content_spanish = self.content_spanish

        content_spanish_mt = self.content_spanish_mt

        content_english = self.content_english

        content_english_mt = self.content_english_mt

        is_nsfw = self.is_nsfw

        image_url = self.image_url

        audio_url = self.audio_url

        actor_ja = self.actor_ja

        actor_es = self.actor_es

        actor_en = self.actor_en

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "position": position,
                "startTime": start_time,
                "endTime": end_time,
                "content": content,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
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
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if audio_url is not UNSET:
            field_dict["audioUrl"] = audio_url
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
        uuid = d.pop("uuid")

        position = d.pop("position")

        start_time = d.pop("startTime")

        end_time = d.pop("endTime")

        content = d.pop("content")

        _status = d.pop("status", UNSET)
        status: SegmentCreateRequestStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SegmentCreateRequestStatus(_status)

        content_spanish = d.pop("contentSpanish", UNSET)

        content_spanish_mt = d.pop("contentSpanishMt", UNSET)

        content_english = d.pop("contentEnglish", UNSET)

        content_english_mt = d.pop("contentEnglishMt", UNSET)

        is_nsfw = d.pop("isNsfw", UNSET)

        image_url = d.pop("imageUrl", UNSET)

        audio_url = d.pop("audioUrl", UNSET)

        actor_ja = d.pop("actorJa", UNSET)

        actor_es = d.pop("actorEs", UNSET)

        actor_en = d.pop("actorEn", UNSET)

        segment_create_request = cls(
            uuid=uuid,
            position=position,
            start_time=start_time,
            end_time=end_time,
            content=content,
            status=status,
            content_spanish=content_spanish,
            content_spanish_mt=content_spanish_mt,
            content_english=content_english,
            content_english_mt=content_english_mt,
            is_nsfw=is_nsfw,
            image_url=image_url,
            audio_url=audio_url,
            actor_ja=actor_ja,
            actor_es=actor_es,
            actor_en=actor_en,
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
