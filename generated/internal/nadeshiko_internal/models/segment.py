from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.content_rating import ContentRating, check_content_rating
from ..models.segment_status import SegmentStatus, check_segment_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.segment_text_en import SegmentTextEn
    from ..models.segment_text_es import SegmentTextEs
    from ..models.segment_text_ja import SegmentTextJa
    from ..models.segment_urls import SegmentUrls


T = TypeVar("T", bound="Segment")


@_attrs_define
class Segment:
    """Segment with content, translations, search-related highlights, and media URLs

    Attributes:
        public_id (str): Public ID for the segment (nanoid) Example: V1StGXR8_Z5d.
        position (int): Position of the segment within the episode Example: 1133.
        status (SegmentStatus): Segment status Example: ACTIVE.
        start_time_ms (int): Start time of the segment in milliseconds from the beginning of the episode Example:
            2007255.
        end_time_ms (int): End time of the segment in milliseconds from the beginning of the episode Example: 2008464.
        content_rating (ContentRating): Content rating level for the segment Example: SAFE.
        episode (int): Episode number this segment belongs to (0 for movies/specials) Example: 1.
        external_video_id (None | str): External source video ID of this segment's episode (YouTube video ID) Example:
            ZJFMStE1Tjo.
        media_public_id (str): Public ID of the media this segment belongs to (nanoid) Example: V1StGXR8_Z5d.
        text_ja (SegmentTextJa):
        text_en (SegmentTextEn):
        text_es (SegmentTextEs):
        urls (SegmentUrls): URLs to media resources for this segment
        episode_title (None | str | Unset): Title of this segment's episode when it has one (an audiobook chapter's
            title), else null Example: (1)とにかく比企谷八幡はくさっている。.
    """

    public_id: str
    position: int
    status: SegmentStatus
    start_time_ms: int
    end_time_ms: int
    content_rating: ContentRating
    episode: int
    external_video_id: None | str
    media_public_id: str
    text_ja: SegmentTextJa
    text_en: SegmentTextEn
    text_es: SegmentTextEs
    urls: SegmentUrls
    episode_title: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_id = self.public_id

        position = self.position

        status: str = self.status

        start_time_ms = self.start_time_ms

        end_time_ms = self.end_time_ms

        content_rating: str = self.content_rating

        episode = self.episode

        external_video_id: None | str
        external_video_id = self.external_video_id

        media_public_id = self.media_public_id

        text_ja = self.text_ja.to_dict()

        text_en = self.text_en.to_dict()

        text_es = self.text_es.to_dict()

        urls = self.urls.to_dict()

        episode_title: None | str | Unset
        if isinstance(self.episode_title, Unset):
            episode_title = UNSET
        else:
            episode_title = self.episode_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "publicId": public_id,
                "position": position,
                "status": status,
                "startTimeMs": start_time_ms,
                "endTimeMs": end_time_ms,
                "contentRating": content_rating,
                "episode": episode,
                "externalVideoId": external_video_id,
                "mediaPublicId": media_public_id,
                "textJa": text_ja,
                "textEn": text_en,
                "textEs": text_es,
                "urls": urls,
            }
        )
        if episode_title is not UNSET:
            field_dict["episodeTitle"] = episode_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.segment_text_en import SegmentTextEn  # noqa: PLC0415
        from ..models.segment_text_es import SegmentTextEs  # noqa: PLC0415
        from ..models.segment_text_ja import SegmentTextJa  # noqa: PLC0415
        from ..models.segment_urls import SegmentUrls  # noqa: PLC0415

        _src = dict(src_dict)
        public_id = _src.pop("publicId")

        position = _src.pop("position")

        status = check_segment_status(_src.pop("status"))

        start_time_ms = _src.pop("startTimeMs")

        end_time_ms = _src.pop("endTimeMs")

        content_rating = check_content_rating(_src.pop("contentRating"))

        episode = _src.pop("episode")

        def _parse_external_video_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        external_video_id = _parse_external_video_id(_src.pop("externalVideoId"))

        media_public_id = _src.pop("mediaPublicId")

        text_ja = SegmentTextJa.from_dict(_src.pop("textJa"))

        text_en = SegmentTextEn.from_dict(_src.pop("textEn"))

        text_es = SegmentTextEs.from_dict(_src.pop("textEs"))

        urls = SegmentUrls.from_dict(_src.pop("urls"))

        def _parse_episode_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        episode_title = _parse_episode_title(_src.pop("episodeTitle", UNSET))

        segment = cls(
            public_id=public_id,
            position=position,
            status=status,
            start_time_ms=start_time_ms,
            end_time_ms=end_time_ms,
            content_rating=content_rating,
            episode=episode,
            external_video_id=external_video_id,
            media_public_id=media_public_id,
            text_ja=text_ja,
            text_en=text_en,
            text_es=text_es,
            urls=urls,
            episode_title=episode_title,
        )

        segment.additional_properties = _src
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
