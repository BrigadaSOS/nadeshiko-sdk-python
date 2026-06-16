from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.content_rating import ContentRating, check_content_rating
from ..models.segment_internal_storage import SegmentInternalStorage, check_segment_internal_storage
from ..models.segment_status import SegmentStatus, check_segment_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.segment_internal_pos_analysis_type_0 import SegmentInternalPosAnalysisType0
    from ..models.segment_internal_rating_analysis_type_0 import SegmentInternalRatingAnalysisType0
    from ..models.segment_text_en import SegmentTextEn
    from ..models.segment_text_es import SegmentTextEs
    from ..models.segment_text_ja import SegmentTextJa
    from ..models.segment_urls import SegmentUrls


T = TypeVar("T", bound="SegmentInternal")


@_attrs_define
class SegmentInternal:
    """Segment with internal fields. For write operations (create, update) all fields are always populated.
    For GET, optional fields are only populated when requested via include[].

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
            storage (SegmentInternalStorage | Unset): Storage backend for segment assets Example: R2.
            hashed_id (None | str | Unset): Hash identifier for the segment Example: 0d39e46b14.
            storage_base_path (None | str | Unset): Base path in the storage backend Example: anime/steins-gate.
            rating_analysis (None | SegmentInternalRatingAnalysisType0 | Unset): Raw WD Tagger v3 classifier output used to
                derive content rating
            pos_analysis (None | SegmentInternalPosAnalysisType0 | Unset): POS tokenization results keyed by engine
                (sudachi, unidic)
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
    storage: SegmentInternalStorage | Unset = UNSET
    hashed_id: None | str | Unset = UNSET
    storage_base_path: None | str | Unset = UNSET
    rating_analysis: None | SegmentInternalRatingAnalysisType0 | Unset = UNSET
    pos_analysis: None | SegmentInternalPosAnalysisType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.segment_internal_pos_analysis_type_0 import SegmentInternalPosAnalysisType0
        from ..models.segment_internal_rating_analysis_type_0 import (
            SegmentInternalRatingAnalysisType0,
        )

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

        storage: str | Unset = UNSET
        if not isinstance(self.storage, Unset):
            storage = self.storage

        hashed_id: None | str | Unset
        if isinstance(self.hashed_id, Unset):
            hashed_id = UNSET
        else:
            hashed_id = self.hashed_id

        storage_base_path: None | str | Unset
        if isinstance(self.storage_base_path, Unset):
            storage_base_path = UNSET
        else:
            storage_base_path = self.storage_base_path

        rating_analysis: dict[str, Any] | None | Unset
        if isinstance(self.rating_analysis, Unset):
            rating_analysis = UNSET
        elif isinstance(self.rating_analysis, SegmentInternalRatingAnalysisType0):
            rating_analysis = self.rating_analysis.to_dict()
        else:
            rating_analysis = self.rating_analysis

        pos_analysis: dict[str, Any] | None | Unset
        if isinstance(self.pos_analysis, Unset):
            pos_analysis = UNSET
        elif isinstance(self.pos_analysis, SegmentInternalPosAnalysisType0):
            pos_analysis = self.pos_analysis.to_dict()
        else:
            pos_analysis = self.pos_analysis

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
        if storage is not UNSET:
            field_dict["storage"] = storage
        if hashed_id is not UNSET:
            field_dict["hashedId"] = hashed_id
        if storage_base_path is not UNSET:
            field_dict["storageBasePath"] = storage_base_path
        if rating_analysis is not UNSET:
            field_dict["ratingAnalysis"] = rating_analysis
        if pos_analysis is not UNSET:
            field_dict["posAnalysis"] = pos_analysis

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.segment_internal_pos_analysis_type_0 import SegmentInternalPosAnalysisType0
        from ..models.segment_internal_rating_analysis_type_0 import (
            SegmentInternalRatingAnalysisType0,
        )
        from ..models.segment_text_en import SegmentTextEn
        from ..models.segment_text_es import SegmentTextEs
        from ..models.segment_text_ja import SegmentTextJa
        from ..models.segment_urls import SegmentUrls

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

        _storage = _src.pop("storage", UNSET)
        storage: SegmentInternalStorage | Unset
        if isinstance(_storage, Unset):
            storage = UNSET
        else:
            storage = check_segment_internal_storage(_storage)

        def _parse_hashed_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hashed_id = _parse_hashed_id(_src.pop("hashedId", UNSET))

        def _parse_storage_base_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_base_path = _parse_storage_base_path(_src.pop("storageBasePath", UNSET))

        def _parse_rating_analysis(
            data: object,
        ) -> None | SegmentInternalRatingAnalysisType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rating_analysis_type_0 = SegmentInternalRatingAnalysisType0.from_dict(data)

                return rating_analysis_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SegmentInternalRatingAnalysisType0 | Unset, data)

        rating_analysis = _parse_rating_analysis(_src.pop("ratingAnalysis", UNSET))

        def _parse_pos_analysis(data: object) -> None | SegmentInternalPosAnalysisType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pos_analysis_type_0 = SegmentInternalPosAnalysisType0.from_dict(data)

                return pos_analysis_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SegmentInternalPosAnalysisType0 | Unset, data)

        pos_analysis = _parse_pos_analysis(_src.pop("posAnalysis", UNSET))

        segment_internal = cls(
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
            storage=storage,
            hashed_id=hashed_id,
            storage_base_path=storage_base_path,
            rating_analysis=rating_analysis,
            pos_analysis=pos_analysis,
        )

        segment_internal.additional_properties = _src
        return segment_internal

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
