from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.content_rating import ContentRating
from ..models.segment_status import SegmentStatus

if TYPE_CHECKING:
    from ..models.segment_text_en import SegmentTextEn
    from ..models.segment_text_es import SegmentTextEs
    from ..models.segment_text_ja import SegmentTextJa
    from ..models.segment_urls import SegmentUrls


T = TypeVar("T", bound="Segment")


@_attrs_define
class Segment:
    """Segment with content, optional highlights, and media URLs

    Attributes:
        id (int): Numeric identifier for the segment Example: 120045.
        uuid (str): Unique identifier for the segment Example: 3fd94cef-a3e1-31ae-bc8d-e743f03e9c7e.
        public_id (str): Public identifier for the segment (use this instead of uuid in public URLs) Example:
            V1StGXR8_Z5d.
        position (int): Position of the segment within the episode Example: 1133.
        status (SegmentStatus): Segment status Example: ACTIVE.
        start_time_ms (int): Start time of the segment in milliseconds from the beginning of the episode Example:
            2007255.
        end_time_ms (int): End time of the segment in milliseconds from the beginning of the episode Example: 2008464.
        content_rating (ContentRating): Content rating level for the segment Example: SAFE.
        episode (int): Episode number this segment belongs to Example: 1.
        media_id (int): Media ID this segment belongs to Example: 7674.
        media_public_id (str): Public ID of the media this segment belongs to Example: V1StGXR8_Z5d.
        text_ja (SegmentTextJa):
        text_en (SegmentTextEn):
        text_es (SegmentTextEs):
        urls (SegmentUrls): URLs to media resources for this segment
    """

    id: int
    uuid: str
    public_id: str
    position: int
    status: SegmentStatus
    start_time_ms: int
    end_time_ms: int
    content_rating: ContentRating
    episode: int
    media_id: int
    media_public_id: str
    text_ja: SegmentTextJa
    text_en: SegmentTextEn
    text_es: SegmentTextEs
    urls: SegmentUrls
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        public_id = self.public_id

        position = self.position

        status = self.status.value

        start_time_ms = self.start_time_ms

        end_time_ms = self.end_time_ms

        content_rating = self.content_rating.value

        episode = self.episode

        media_id = self.media_id

        media_public_id = self.media_public_id

        text_ja = self.text_ja.to_dict()

        text_en = self.text_en.to_dict()

        text_es = self.text_es.to_dict()

        urls = self.urls.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uuid": uuid,
                "publicId": public_id,
                "position": position,
                "status": status,
                "startTimeMs": start_time_ms,
                "endTimeMs": end_time_ms,
                "contentRating": content_rating,
                "episode": episode,
                "mediaId": media_id,
                "mediaPublicId": media_public_id,
                "textJa": text_ja,
                "textEn": text_en,
                "textEs": text_es,
                "urls": urls,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.segment_text_en import SegmentTextEn
        from ..models.segment_text_es import SegmentTextEs
        from ..models.segment_text_ja import SegmentTextJa
        from ..models.segment_urls import SegmentUrls

        d = dict(src_dict)
        id = d.pop("id")

        uuid = d.pop("uuid")

        public_id = d.pop("publicId")

        position = d.pop("position")

        status = SegmentStatus(d.pop("status"))

        start_time_ms = d.pop("startTimeMs")

        end_time_ms = d.pop("endTimeMs")

        content_rating = ContentRating(d.pop("contentRating"))

        episode = d.pop("episode")

        media_id = d.pop("mediaId")

        media_public_id = d.pop("mediaPublicId")

        text_ja = SegmentTextJa.from_dict(d.pop("textJa"))

        text_en = SegmentTextEn.from_dict(d.pop("textEn"))

        text_es = SegmentTextEs.from_dict(d.pop("textEs"))

        urls = SegmentUrls.from_dict(d.pop("urls"))

        segment = cls(
            id=id,
            uuid=uuid,
            public_id=public_id,
            position=position,
            status=status,
            start_time_ms=start_time_ms,
            end_time_ms=end_time_ms,
            content_rating=content_rating,
            episode=episode,
            media_id=media_id,
            media_public_id=media_public_id,
            text_ja=text_ja,
            text_en=text_en,
            text_es=text_es,
            urls=urls,
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
