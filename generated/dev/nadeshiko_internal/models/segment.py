from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.segment_status import SegmentStatus
from ..models.segment_storage import SegmentStorage
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.japanese_content import JapaneseContent
    from ..models.morpheme import Morpheme
    from ..models.translation_content import TranslationContent


T = TypeVar("T", bound="Segment")


@_attrs_define
class Segment:
    """
    Attributes:
        id (int): Auto-generated segment ID Example: 12345.
        uuid (str): Unique identifier for the segment Example: 3fd94cef-a3e1-31ae-bc8d-e743f03e9c7e.
        position (int): Position of the segment within the episode Example: 1133.
        status (SegmentStatus): Segment status Example: ACTIVE.
        start_time (str): Timestamp in H:MM:SS.ffffff format indicating when the segment starts Example: 0:33:27.255000.
        end_time (str): Timestamp in H:MM:SS.ffffff format indicating when the segment ends Example: 0:33:28.464000.
        text_ja (JapaneseContent): Japanese content with optional character count
        text_en (TranslationContent): Translation content for a language
        text_es (TranslationContent): Translation content for a language
        is_nsfw (bool): Whether the segment contains NSFW content
        episode (int): Episode number this segment belongs to Example: 1.
        media_id (int): Media ID this segment belongs to Example: 7674.
        storage (SegmentStorage): Storage backend for segment assets Example: R2.
        hashed_id (str): Hash identifier for the segment Example: 0d39e46b14.
        image_url (None | str | Unset): URL to segment screenshot/image (generated from storage + hashedId) Example:
            https://cdn.nadeshiko.co/media/7674/1/0d39e46b14.webp.
        audio_url (None | str | Unset): URL to segment audio file (generated from storage + hashedId) Example:
            https://cdn.nadeshiko.co/media/7674/1/0d39e46b14.mp3.
        video_url (None | str | Unset): URL to segment video file (generated from storage + hashedId) Example:
            https://cdn.nadeshiko.co/media/7674/1/0d39e46b14.mp4.
        morphemes (list[Morpheme] | None | Unset): Morphological analysis of the Japanese content
    """

    id: int
    uuid: str
    position: int
    status: SegmentStatus
    start_time: str
    end_time: str
    text_ja: JapaneseContent
    text_en: TranslationContent
    text_es: TranslationContent
    is_nsfw: bool
    episode: int
    media_id: int
    storage: SegmentStorage
    hashed_id: str
    image_url: None | str | Unset = UNSET
    audio_url: None | str | Unset = UNSET
    video_url: None | str | Unset = UNSET
    morphemes: list[Morpheme] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        position = self.position

        status = self.status.value

        start_time = self.start_time

        end_time = self.end_time

        text_ja = self.text_ja.to_dict()

        text_en = self.text_en.to_dict()

        text_es = self.text_es.to_dict()

        is_nsfw = self.is_nsfw

        episode = self.episode

        media_id = self.media_id

        storage = self.storage.value

        hashed_id = self.hashed_id

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

        video_url: None | str | Unset
        if isinstance(self.video_url, Unset):
            video_url = UNSET
        else:
            video_url = self.video_url

        morphemes: list[dict[str, Any]] | None | Unset
        if isinstance(self.morphemes, Unset):
            morphemes = UNSET
        elif isinstance(self.morphemes, list):
            morphemes = []
            for morphemes_type_0_item_data in self.morphemes:
                morphemes_type_0_item = morphemes_type_0_item_data.to_dict()
                morphemes.append(morphemes_type_0_item)

        else:
            morphemes = self.morphemes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uuid": uuid,
                "position": position,
                "status": status,
                "startTime": start_time,
                "endTime": end_time,
                "textJa": text_ja,
                "textEn": text_en,
                "textEs": text_es,
                "isNsfw": is_nsfw,
                "episode": episode,
                "mediaId": media_id,
                "storage": storage,
                "hashedId": hashed_id,
            }
        )
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if audio_url is not UNSET:
            field_dict["audioUrl"] = audio_url
        if video_url is not UNSET:
            field_dict["videoUrl"] = video_url
        if morphemes is not UNSET:
            field_dict["morphemes"] = morphemes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.japanese_content import JapaneseContent
        from ..models.morpheme import Morpheme
        from ..models.translation_content import TranslationContent

        d = dict(src_dict)
        id = d.pop("id")

        uuid = d.pop("uuid")

        position = d.pop("position")

        status = SegmentStatus(d.pop("status"))

        start_time = d.pop("startTime")

        end_time = d.pop("endTime")

        text_ja = JapaneseContent.from_dict(d.pop("textJa"))

        text_en = TranslationContent.from_dict(d.pop("textEn"))

        text_es = TranslationContent.from_dict(d.pop("textEs"))

        is_nsfw = d.pop("isNsfw")

        episode = d.pop("episode")

        media_id = d.pop("mediaId")

        storage = SegmentStorage(d.pop("storage"))

        hashed_id = d.pop("hashedId")

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

        def _parse_video_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        video_url = _parse_video_url(d.pop("videoUrl", UNSET))

        def _parse_morphemes(data: object) -> list[Morpheme] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                morphemes_type_0 = []
                _morphemes_type_0 = data
                for morphemes_type_0_item_data in _morphemes_type_0:
                    morphemes_type_0_item = Morpheme.from_dict(morphemes_type_0_item_data)

                    morphemes_type_0.append(morphemes_type_0_item)

                return morphemes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Morpheme] | None | Unset, data)

        morphemes = _parse_morphemes(d.pop("morphemes", UNSET))

        segment = cls(
            id=id,
            uuid=uuid,
            position=position,
            status=status,
            start_time=start_time,
            end_time=end_time,
            text_ja=text_ja,
            text_en=text_en,
            text_es=text_es,
            is_nsfw=is_nsfw,
            episode=episode,
            media_id=media_id,
            storage=storage,
            hashed_id=hashed_id,
            image_url=image_url,
            audio_url=audio_url,
            video_url=video_url,
            morphemes=morphemes,
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
