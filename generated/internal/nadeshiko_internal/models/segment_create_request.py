from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.content_rating import ContentRating, check_content_rating
from ..models.segment_create_request_storage import (
    SegmentCreateRequestStorage,
    check_segment_create_request_storage,
)
from ..models.segment_status import SegmentStatus, check_segment_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.segment_create_request_rating_analysis_type_0 import (
        SegmentCreateRequestRatingAnalysisType0,
    )
    from ..models.segment_create_request_text_en import SegmentCreateRequestTextEn
    from ..models.segment_create_request_text_es import SegmentCreateRequestTextEs
    from ..models.segment_create_request_text_ja import SegmentCreateRequestTextJa


T = TypeVar("T", bound="SegmentCreateRequest")


@_attrs_define
class SegmentCreateRequest:
    """
    Attributes:
        position (int): Position of the segment within the episode Example: 1133.
        start_time_ms (int): Start time of the segment in milliseconds from the beginning of the episode Example:
            2007255.
        end_time_ms (int): End time of the segment in milliseconds from the beginning of the episode Example: 2008464.
        text_ja (SegmentCreateRequestTextJa):
        storage (SegmentCreateRequestStorage): Storage backend for segment assets Default: 'R2'. Example: R2.
        hashed_id (str): Hash identifier for the segment (from segment JSON) Example: 0d39e46b14.
        status (SegmentStatus | Unset): Segment status Default: 'ACTIVE'. Example: ACTIVE.
        text_es (SegmentCreateRequestTextEs | Unset):
        text_en (SegmentCreateRequestTextEn | Unset):
        content_rating (ContentRating | Unset): Content rating level for the segment Example: SAFE.
        rating_analysis (None | SegmentCreateRequestRatingAnalysisType0 | Unset): Raw WD Tagger v3 classifier output
            used to derive content rating
    """

    position: int
    start_time_ms: int
    end_time_ms: int
    text_ja: SegmentCreateRequestTextJa
    hashed_id: str
    storage: SegmentCreateRequestStorage = "R2"
    status: SegmentStatus | Unset = "ACTIVE"
    text_es: SegmentCreateRequestTextEs | Unset = UNSET
    text_en: SegmentCreateRequestTextEn | Unset = UNSET
    content_rating: ContentRating | Unset = UNSET
    rating_analysis: None | SegmentCreateRequestRatingAnalysisType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.segment_create_request_rating_analysis_type_0 import (
            SegmentCreateRequestRatingAnalysisType0,
        )

        position = self.position

        start_time_ms = self.start_time_ms

        end_time_ms = self.end_time_ms

        text_ja = self.text_ja.to_dict()

        storage: str = self.storage

        hashed_id = self.hashed_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        text_es: dict[str, Any] | Unset = UNSET
        if not isinstance(self.text_es, Unset):
            text_es = self.text_es.to_dict()

        text_en: dict[str, Any] | Unset = UNSET
        if not isinstance(self.text_en, Unset):
            text_en = self.text_en.to_dict()

        content_rating: str | Unset = UNSET
        if not isinstance(self.content_rating, Unset):
            content_rating = self.content_rating

        rating_analysis: dict[str, Any] | None | Unset
        if isinstance(self.rating_analysis, Unset):
            rating_analysis = UNSET
        elif isinstance(self.rating_analysis, SegmentCreateRequestRatingAnalysisType0):
            rating_analysis = self.rating_analysis.to_dict()
        else:
            rating_analysis = self.rating_analysis

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position": position,
                "startTimeMs": start_time_ms,
                "endTimeMs": end_time_ms,
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
        if content_rating is not UNSET:
            field_dict["contentRating"] = content_rating
        if rating_analysis is not UNSET:
            field_dict["ratingAnalysis"] = rating_analysis

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.segment_create_request_rating_analysis_type_0 import (
            SegmentCreateRequestRatingAnalysisType0,
        )
        from ..models.segment_create_request_text_en import SegmentCreateRequestTextEn
        from ..models.segment_create_request_text_es import SegmentCreateRequestTextEs
        from ..models.segment_create_request_text_ja import SegmentCreateRequestTextJa

        _src = dict(src_dict)
        position = _src.pop("position")

        start_time_ms = _src.pop("startTimeMs")

        end_time_ms = _src.pop("endTimeMs")

        text_ja = SegmentCreateRequestTextJa.from_dict(_src.pop("textJa"))

        storage = check_segment_create_request_storage(_src.pop("storage"))

        hashed_id = _src.pop("hashedId")

        _status = _src.pop("status", UNSET)
        status: SegmentStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_segment_status(_status)

        _text_es = _src.pop("textEs", UNSET)
        text_es: SegmentCreateRequestTextEs | Unset
        if isinstance(_text_es, Unset):
            text_es = UNSET
        else:
            text_es = SegmentCreateRequestTextEs.from_dict(_text_es)

        _text_en = _src.pop("textEn", UNSET)
        text_en: SegmentCreateRequestTextEn | Unset
        if isinstance(_text_en, Unset):
            text_en = UNSET
        else:
            text_en = SegmentCreateRequestTextEn.from_dict(_text_en)

        _content_rating = _src.pop("contentRating", UNSET)
        content_rating: ContentRating | Unset
        if isinstance(_content_rating, Unset):
            content_rating = UNSET
        else:
            content_rating = check_content_rating(_content_rating)

        def _parse_rating_analysis(
            data: object,
        ) -> None | SegmentCreateRequestRatingAnalysisType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rating_analysis_type_0 = SegmentCreateRequestRatingAnalysisType0.from_dict(data)

                return rating_analysis_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SegmentCreateRequestRatingAnalysisType0 | Unset, data)

        rating_analysis = _parse_rating_analysis(_src.pop("ratingAnalysis", UNSET))

        segment_create_request = cls(
            position=position,
            start_time_ms=start_time_ms,
            end_time_ms=end_time_ms,
            text_ja=text_ja,
            storage=storage,
            hashed_id=hashed_id,
            status=status,
            text_es=text_es,
            text_en=text_en,
            content_rating=content_rating,
            rating_analysis=rating_analysis,
        )

        segment_create_request.additional_properties = _src
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
