from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SegmentInfo")


@_attrs_define
class SegmentInfo:
    """Detailed information about a subtitle segment

    Attributes:
        status (int): Segment status (0=Deleted, 1=Active, 2=Suspended, 3=Verified, 100=Invalid Sentence, 101=Sentence
            Too Long) Example: 1.
        uuid (UUID): Unique identifier for the segment Example: 3fd94cef-a3e1-31ae-bc8d-e743f03e9c7e.
        position (int): Position of the segment within the episode Example: 1133.
        start_time (str): Timestamp in H:MM:SS.ffffff format (variable-length hours, microseconds) indicating when the
            segment starts Example: 0:33:27.255000.
        end_time (str): Timestamp in H:MM:SS.ffffff format (variable-length hours, microseconds) indicating when the
            segment ends Example: 0:33:28.464000.
        content_jp (str): Original Japanese content of the segment Example: 僕は僕で、君は君だ。.
        content_en_mt (bool): Indicates whether the English translation was machine-translated
        content_es_mt (bool): Indicates whether the Spanish translation was machine-translated
        is_nsfw (bool): Indicates whether the segment contains NSFW (Not Safe For Work) content
        content_jp_highlight (str | Unset): Japanese content with search terms highlighted Example:
            <em>僕</em>は<em>僕</em>で、<em>君</em>は<em>君</em>だ。.
        content_en (str | Unset): English translation of the segment content Example: I am me, and you are you..
        content_en_highlight (str | Unset): English content with search terms highlighted Example: <em>I</em> am
            <em>me</em>, and <em>you</em> are <em>you</em>..
        content_es (str | Unset): Spanish translation of the segment content Example: Yo soy yo, y tú eres tú..
        content_es_highlight (str | Unset): Spanish content with search terms highlighted Example: <em>Yo</em> soy
            <em>yo</em>, y <em>tú</em> eres <em>tú</em>..
        actor_ja (str | Unset): Name of the Japanese voice actor for this segment Example: Mamoru Miyano.
        actor_en (str | Unset): Name of the English voice actor for this segment Example: J. Michael Tatum.
        actor_es (str | Unset): Name of the Spanish voice actor for this segment Example: Alejandro Levis.
    """

    status: int
    uuid: UUID
    position: int
    start_time: str
    end_time: str
    content_jp: str
    content_en_mt: bool
    content_es_mt: bool
    is_nsfw: bool
    content_jp_highlight: str | Unset = UNSET
    content_en: str | Unset = UNSET
    content_en_highlight: str | Unset = UNSET
    content_es: str | Unset = UNSET
    content_es_highlight: str | Unset = UNSET
    actor_ja: str | Unset = UNSET
    actor_en: str | Unset = UNSET
    actor_es: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        uuid = str(self.uuid)

        position = self.position

        start_time = self.start_time

        end_time = self.end_time

        content_jp = self.content_jp

        content_en_mt = self.content_en_mt

        content_es_mt = self.content_es_mt

        is_nsfw = self.is_nsfw

        content_jp_highlight = self.content_jp_highlight

        content_en = self.content_en

        content_en_highlight = self.content_en_highlight

        content_es = self.content_es

        content_es_highlight = self.content_es_highlight

        actor_ja = self.actor_ja

        actor_en = self.actor_en

        actor_es = self.actor_es

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "uuid": uuid,
                "position": position,
                "start_time": start_time,
                "end_time": end_time,
                "content_jp": content_jp,
                "content_en_mt": content_en_mt,
                "content_es_mt": content_es_mt,
                "is_nsfw": is_nsfw,
            }
        )
        if content_jp_highlight is not UNSET:
            field_dict["content_jp_highlight"] = content_jp_highlight
        if content_en is not UNSET:
            field_dict["content_en"] = content_en
        if content_en_highlight is not UNSET:
            field_dict["content_en_highlight"] = content_en_highlight
        if content_es is not UNSET:
            field_dict["content_es"] = content_es
        if content_es_highlight is not UNSET:
            field_dict["content_es_highlight"] = content_es_highlight
        if actor_ja is not UNSET:
            field_dict["actor_ja"] = actor_ja
        if actor_en is not UNSET:
            field_dict["actor_en"] = actor_en
        if actor_es is not UNSET:
            field_dict["actor_es"] = actor_es

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status")

        uuid = UUID(d.pop("uuid"))

        position = d.pop("position")

        start_time = d.pop("start_time")

        end_time = d.pop("end_time")

        content_jp = d.pop("content_jp")

        content_en_mt = d.pop("content_en_mt")

        content_es_mt = d.pop("content_es_mt")

        is_nsfw = d.pop("is_nsfw")

        content_jp_highlight = d.pop("content_jp_highlight", UNSET)

        content_en = d.pop("content_en", UNSET)

        content_en_highlight = d.pop("content_en_highlight", UNSET)

        content_es = d.pop("content_es", UNSET)

        content_es_highlight = d.pop("content_es_highlight", UNSET)

        actor_ja = d.pop("actor_ja", UNSET)

        actor_en = d.pop("actor_en", UNSET)

        actor_es = d.pop("actor_es", UNSET)

        segment_info = cls(
            status=status,
            uuid=uuid,
            position=position,
            start_time=start_time,
            end_time=end_time,
            content_jp=content_jp,
            content_en_mt=content_en_mt,
            content_es_mt=content_es_mt,
            is_nsfw=is_nsfw,
            content_jp_highlight=content_jp_highlight,
            content_en=content_en,
            content_en_highlight=content_en_highlight,
            content_es=content_es,
            content_es_highlight=content_es_highlight,
            actor_ja=actor_ja,
            actor_en=actor_en,
            actor_es=actor_es,
        )

        segment_info.additional_properties = d
        return segment_info

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
