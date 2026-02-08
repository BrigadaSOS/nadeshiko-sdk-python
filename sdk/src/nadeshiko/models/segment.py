from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.segment_status import SegmentStatus
from ..models.segment_storage import SegmentStorage
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Segment")



@_attrs_define
class Segment:
    """ 
        Attributes:
            id (int): Auto-generated segment ID Example: 12345.
            uuid (str): Unique identifier for the segment Example: 3fd94cef-a3e1-31ae-bc8d-e743f03e9c7e.
            position (int): Position of the segment within the episode Example: 1133.
            status (SegmentStatus): Segment status (0=Deleted, 1=Active, 2=Suspended, 3=Verified, 100=Invalid Sentence,
                101=Sentence Too Long) Example: 1.
            start_time (str): Timestamp in H:MM:SS.ffffff format indicating when the segment starts Example: 0:33:27.255000.
            end_time (str): Timestamp in H:MM:SS.ffffff format indicating when the segment ends Example: 0:33:28.464000.
            content (str): Original Japanese content of the segment Example: 僕は僕で、君は君だ。.
            content_length (int): Length of the content Example: 10.
            content_spanish_mt (bool): Whether the Spanish translation was machine-translated
            content_english_mt (bool): Whether the English translation was machine-translated
            is_nsfw (bool): Whether the segment contains NSFW content
            episode (int): Episode number this segment belongs to Example: 1.
            media_id (int): Media ID this segment belongs to Example: 7674.
            storage (SegmentStorage): Storage backend for segment assets Example: r2.
            hashed_id (str): Hash identifier for the segment Example: 0d39e46b14.
            content_spanish (None | str | Unset): Spanish translation of the segment content Example: Yo soy yo, y tú eres
                tú..
            content_english (None | str | Unset): English translation of the segment content Example: I am me, and you are
                you..
            image_url (None | str | Unset): URL to segment screenshot/image (generated from storage + hashedId) Example:
                https://cdn.nadeshiko.co/media/7674/1/0d39e46b14.webp.
            audio_url (None | str | Unset): URL to segment audio file (generated from storage + hashedId) Example:
                https://cdn.nadeshiko.co/media/7674/1/0d39e46b14.mp3.
            actor_ja (None | str | Unset): Japanese voice actor name Example: Mamoru Miyano.
            actor_es (None | str | Unset): Spanish voice actor name Example: Alejandro Levis.
            actor_en (None | str | Unset): English voice actor name Example: J. Michael Tatum.
     """

    id: int
    uuid: str
    position: int
    status: SegmentStatus
    start_time: str
    end_time: str
    content: str
    content_length: int
    content_spanish_mt: bool
    content_english_mt: bool
    is_nsfw: bool
    episode: int
    media_id: int
    storage: SegmentStorage
    hashed_id: str
    content_spanish: None | str | Unset = UNSET
    content_english: None | str | Unset = UNSET
    image_url: None | str | Unset = UNSET
    audio_url: None | str | Unset = UNSET
    actor_ja: None | str | Unset = UNSET
    actor_es: None | str | Unset = UNSET
    actor_en: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        position = self.position

        status = self.status.value

        start_time = self.start_time

        end_time = self.end_time

        content = self.content

        content_length = self.content_length

        content_spanish_mt = self.content_spanish_mt

        content_english_mt = self.content_english_mt

        is_nsfw = self.is_nsfw

        episode = self.episode

        media_id = self.media_id

        storage = self.storage.value

        hashed_id = self.hashed_id

        content_spanish: None | str | Unset
        if isinstance(self.content_spanish, Unset):
            content_spanish = UNSET
        else:
            content_spanish = self.content_spanish

        content_english: None | str | Unset
        if isinstance(self.content_english, Unset):
            content_english = UNSET
        else:
            content_english = self.content_english

        image_url: None | str | Unset
        if isinstance(self.image_url, Unset):
            image_url = UNSET
        else:
            image_url = self.image_url

        audio_url: None | str | Unset
        if isinstance(self.audio_url, Unset):
            audio_url = UNSET
        else:
            audio_url = self.audio_url

        actor_ja: None | str | Unset
        if isinstance(self.actor_ja, Unset):
            actor_ja = UNSET
        else:
            actor_ja = self.actor_ja

        actor_es: None | str | Unset
        if isinstance(self.actor_es, Unset):
            actor_es = UNSET
        else:
            actor_es = self.actor_es

        actor_en: None | str | Unset
        if isinstance(self.actor_en, Unset):
            actor_en = UNSET
        else:
            actor_en = self.actor_en


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "uuid": uuid,
            "position": position,
            "status": status,
            "startTime": start_time,
            "endTime": end_time,
            "content": content,
            "contentLength": content_length,
            "contentSpanishMt": content_spanish_mt,
            "contentEnglishMt": content_english_mt,
            "isNsfw": is_nsfw,
            "episode": episode,
            "mediaId": media_id,
            "storage": storage,
            "hashedId": hashed_id,
        })
        if content_spanish is not UNSET:
            field_dict["contentSpanish"] = content_spanish
        if content_english is not UNSET:
            field_dict["contentEnglish"] = content_english
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
        id = d.pop("id")

        uuid = d.pop("uuid")

        position = d.pop("position")

        status = SegmentStatus(d.pop("status"))




        start_time = d.pop("startTime")

        end_time = d.pop("endTime")

        content = d.pop("content")

        content_length = d.pop("contentLength")

        content_spanish_mt = d.pop("contentSpanishMt")

        content_english_mt = d.pop("contentEnglishMt")

        is_nsfw = d.pop("isNsfw")

        episode = d.pop("episode")

        media_id = d.pop("mediaId")

        storage = SegmentStorage(d.pop("storage"))




        hashed_id = d.pop("hashedId")

        def _parse_content_spanish(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_spanish = _parse_content_spanish(d.pop("contentSpanish", UNSET))


        def _parse_content_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_english = _parse_content_english(d.pop("contentEnglish", UNSET))


        def _parse_image_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_url = _parse_image_url(d.pop("imageUrl", UNSET))


        def _parse_audio_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        audio_url = _parse_audio_url(d.pop("audioUrl", UNSET))


        def _parse_actor_ja(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        actor_ja = _parse_actor_ja(d.pop("actorJa", UNSET))


        def _parse_actor_es(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        actor_es = _parse_actor_es(d.pop("actorEs", UNSET))


        def _parse_actor_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        actor_en = _parse_actor_en(d.pop("actorEn", UNSET))


        segment = cls(
            id=id,
            uuid=uuid,
            position=position,
            status=status,
            start_time=start_time,
            end_time=end_time,
            content=content,
            content_length=content_length,
            content_spanish_mt=content_spanish_mt,
            content_english_mt=content_english_mt,
            is_nsfw=is_nsfw,
            episode=episode,
            media_id=media_id,
            storage=storage,
            hashed_id=hashed_id,
            content_spanish=content_spanish,
            content_english=content_english,
            image_url=image_url,
            audio_url=audio_url,
            actor_ja=actor_ja,
            actor_es=actor_es,
            actor_en=actor_en,
        )


        segment.additional_properties = d
        return segment

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
