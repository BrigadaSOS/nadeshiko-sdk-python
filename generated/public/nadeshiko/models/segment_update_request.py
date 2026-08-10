from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.content_rating import ContentRating, check_content_rating
from ..models.segment_status import SegmentStatus, check_segment_status
from ..models.segment_update_request_storage import (
    SegmentUpdateRequestStorage,
    check_segment_update_request_storage,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.segment_update_request_rating_analysis_type_0 import (
        SegmentUpdateRequestRatingAnalysisType0,
    )
    from ..models.segment_update_request_text_en import SegmentUpdateRequestTextEn
    from ..models.segment_update_request_text_es import SegmentUpdateRequestTextEs
    from ..models.segment_update_request_text_ja import SegmentUpdateRequestTextJa


T = TypeVar("T", bound="SegmentUpdateRequest")


@_attrs_define
class SegmentUpdateRequest:
    """All fields are optional for partial updates

    Attributes:
        position (int | Unset): Position of the segment within the episode Example: 1133.
        status (SegmentStatus | Unset): Segment status Example: ACTIVE.
        start_time_ms (int | Unset): Start time of the segment in milliseconds from the beginning of the episode
            Example: 2007255.
        end_time_ms (int | Unset): End time of the segment in milliseconds from the beginning of the episode Example:
            2008464.
        text_ja (SegmentUpdateRequestTextJa | Unset):
        text_es (SegmentUpdateRequestTextEs | Unset):
        text_en (SegmentUpdateRequestTextEn | Unset):
        content_rating (ContentRating | Unset): Content rating level for the segment Example: SAFE.
        rating_analysis (None | SegmentUpdateRequestRatingAnalysisType0 | Unset): Raw WD Tagger v3 classifier output
            used to derive content rating
        storage (SegmentUpdateRequestStorage | Unset): Storage backend for segment assets Example: R2.
        hashed_id (str | Unset): Hash identifier for the segment (from segment JSON) Example: 0d39e46b14.
        report_id (int | Unset): The report this edit answers, recorded on the resulting revision.

            Optional, and only meaningful for moderation traffic — it is what lets the
            agent activity feed show which reported problem an edit was made for. Edits
            that did not come from a report leave it unset.
             Example: 4821.
    """

    position: int | Unset = UNSET
    status: SegmentStatus | Unset = UNSET
    start_time_ms: int | Unset = UNSET
    end_time_ms: int | Unset = UNSET
    text_ja: SegmentUpdateRequestTextJa | Unset = UNSET
    text_es: SegmentUpdateRequestTextEs | Unset = UNSET
    text_en: SegmentUpdateRequestTextEn | Unset = UNSET
    content_rating: ContentRating | Unset = UNSET
    rating_analysis: None | SegmentUpdateRequestRatingAnalysisType0 | Unset = UNSET
    storage: SegmentUpdateRequestStorage | Unset = UNSET
    hashed_id: str | Unset = UNSET
    report_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.segment_update_request_rating_analysis_type_0 import (
            SegmentUpdateRequestRatingAnalysisType0,
        )

        position = self.position

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        start_time_ms = self.start_time_ms

        end_time_ms = self.end_time_ms

        text_ja: dict[str, Any] | Unset = UNSET
        if not isinstance(self.text_ja, Unset):
            text_ja = self.text_ja.to_dict()

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
        elif isinstance(self.rating_analysis, SegmentUpdateRequestRatingAnalysisType0):
            rating_analysis = self.rating_analysis.to_dict()
        else:
            rating_analysis = self.rating_analysis

        storage: str | Unset = UNSET
        if not isinstance(self.storage, Unset):
            storage = self.storage

        hashed_id = self.hashed_id

        report_id = self.report_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if position is not UNSET:
            field_dict["position"] = position
        if status is not UNSET:
            field_dict["status"] = status
        if start_time_ms is not UNSET:
            field_dict["startTimeMs"] = start_time_ms
        if end_time_ms is not UNSET:
            field_dict["endTimeMs"] = end_time_ms
        if text_ja is not UNSET:
            field_dict["textJa"] = text_ja
        if text_es is not UNSET:
            field_dict["textEs"] = text_es
        if text_en is not UNSET:
            field_dict["textEn"] = text_en
        if content_rating is not UNSET:
            field_dict["contentRating"] = content_rating
        if rating_analysis is not UNSET:
            field_dict["ratingAnalysis"] = rating_analysis
        if storage is not UNSET:
            field_dict["storage"] = storage
        if hashed_id is not UNSET:
            field_dict["hashedId"] = hashed_id
        if report_id is not UNSET:
            field_dict["reportId"] = report_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.segment_update_request_rating_analysis_type_0 import (
            SegmentUpdateRequestRatingAnalysisType0,
        )
        from ..models.segment_update_request_text_en import SegmentUpdateRequestTextEn
        from ..models.segment_update_request_text_es import SegmentUpdateRequestTextEs
        from ..models.segment_update_request_text_ja import SegmentUpdateRequestTextJa

        _src = dict(src_dict)
        position = _src.pop("position", UNSET)

        _status = _src.pop("status", UNSET)
        status: SegmentStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_segment_status(_status)

        start_time_ms = _src.pop("startTimeMs", UNSET)

        end_time_ms = _src.pop("endTimeMs", UNSET)

        _text_ja = _src.pop("textJa", UNSET)
        text_ja: SegmentUpdateRequestTextJa | Unset
        if isinstance(_text_ja, Unset):
            text_ja = UNSET
        else:
            text_ja = SegmentUpdateRequestTextJa.from_dict(_text_ja)

        _text_es = _src.pop("textEs", UNSET)
        text_es: SegmentUpdateRequestTextEs | Unset
        if isinstance(_text_es, Unset):
            text_es = UNSET
        else:
            text_es = SegmentUpdateRequestTextEs.from_dict(_text_es)

        _text_en = _src.pop("textEn", UNSET)
        text_en: SegmentUpdateRequestTextEn | Unset
        if isinstance(_text_en, Unset):
            text_en = UNSET
        else:
            text_en = SegmentUpdateRequestTextEn.from_dict(_text_en)

        _content_rating = _src.pop("contentRating", UNSET)
        content_rating: ContentRating | Unset
        if isinstance(_content_rating, Unset):
            content_rating = UNSET
        else:
            content_rating = check_content_rating(_content_rating)

        def _parse_rating_analysis(
            data: object,
        ) -> None | SegmentUpdateRequestRatingAnalysisType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rating_analysis_type_0 = SegmentUpdateRequestRatingAnalysisType0.from_dict(data)

                return rating_analysis_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SegmentUpdateRequestRatingAnalysisType0 | Unset, data)

        rating_analysis = _parse_rating_analysis(_src.pop("ratingAnalysis", UNSET))

        _storage = _src.pop("storage", UNSET)
        storage: SegmentUpdateRequestStorage | Unset
        if isinstance(_storage, Unset):
            storage = UNSET
        else:
            storage = check_segment_update_request_storage(_storage)

        hashed_id = _src.pop("hashedId", UNSET)

        report_id = _src.pop("reportId", UNSET)

        segment_update_request = cls(
            position=position,
            status=status,
            start_time_ms=start_time_ms,
            end_time_ms=end_time_ms,
            text_ja=text_ja,
            text_es=text_es,
            text_en=text_en,
            content_rating=content_rating,
            rating_analysis=rating_analysis,
            storage=storage,
            hashed_id=hashed_id,
            report_id=report_id,
        )

        segment_update_request.additional_properties = _src
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
