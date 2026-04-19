from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.category import Category, check_category
from ..models.content_rating import ContentRating, check_content_rating
from ..models.search_filters_languages_type_0_item import (
    SearchFiltersLanguagesType0Item,
    check_search_filters_languages_type_0_item,
)
from ..models.segment_status import SegmentStatus, check_segment_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_filters_languages_type_1 import SearchFiltersLanguagesType1
    from ..models.search_filters_media import SearchFiltersMedia
    from ..models.search_filters_segment_duration_ms import SearchFiltersSegmentDurationMs
    from ..models.search_filters_segment_length_chars import SearchFiltersSegmentLengthChars


T = TypeVar("T", bound="SearchFilters")


@_attrs_define
class SearchFilters:
    """Search filters for narrowing segment results

    Attributes:
        media (SearchFiltersMedia | Unset): Media inclusion/exclusion filters
        category (list[Category] | Unset): Media category filter
        content_rating (list[ContentRating] | Unset): Content ratings to include (omit for all ratings)
        status (list[SegmentStatus] | Unset): Segment status filter
        segment_length_chars (SearchFiltersSegmentLengthChars | Unset): Content character count range filter
        segment_duration_ms (SearchFiltersSegmentDurationMs | Unset): Segment audio duration range filter (in
            milliseconds)
        languages (list[SearchFiltersLanguagesType0Item] | SearchFiltersLanguagesType1 | Unset): Translation languages
            to include alongside Japanese in search matching.
            - Omitted / `null`: match against Japanese and all translation languages (default)
            - `[]`: match against Japanese only
            - `["EN"]` / `["ES"]` / `["EN", "ES"]`: match against Japanese plus the listed translation languages

            Also accepts the legacy object form `{ exclude: ["en", "es"] }` for backward compatibility.
            The legacy form is translated on receipt: listed codes are excluded from the default language set.
    """

    media: SearchFiltersMedia | Unset = UNSET
    category: list[Category] | Unset = UNSET
    content_rating: list[ContentRating] | Unset = UNSET
    status: list[SegmentStatus] | Unset = UNSET
    segment_length_chars: SearchFiltersSegmentLengthChars | Unset = UNSET
    segment_duration_ms: SearchFiltersSegmentDurationMs | Unset = UNSET
    languages: list[SearchFiltersLanguagesType0Item] | SearchFiltersLanguagesType1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media: dict[str, Any] | Unset = UNSET
        if not isinstance(self.media, Unset):
            media = self.media.to_dict()

        category: list[str] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = []
            for category_item_data in self.category:
                category_item: str = category_item_data
                category.append(category_item)

        content_rating: list[str] | Unset = UNSET
        if not isinstance(self.content_rating, Unset):
            content_rating = []
            for content_rating_item_data in self.content_rating:
                content_rating_item: str = content_rating_item_data
                content_rating.append(content_rating_item)

        status: list[str] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = []
            for status_item_data in self.status:
                status_item: str = status_item_data
                status.append(status_item)

        segment_length_chars: dict[str, Any] | Unset = UNSET
        if not isinstance(self.segment_length_chars, Unset):
            segment_length_chars = self.segment_length_chars.to_dict()

        segment_duration_ms: dict[str, Any] | Unset = UNSET
        if not isinstance(self.segment_duration_ms, Unset):
            segment_duration_ms = self.segment_duration_ms.to_dict()

        languages: dict[str, Any] | list[str] | Unset
        if isinstance(self.languages, Unset):
            languages = UNSET
        elif isinstance(self.languages, list):
            languages = []
            for languages_type_0_item_data in self.languages:
                languages_type_0_item: str = languages_type_0_item_data
                languages.append(languages_type_0_item)

        else:
            languages = self.languages.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if media is not UNSET:
            field_dict["media"] = media
        if category is not UNSET:
            field_dict["category"] = category
        if content_rating is not UNSET:
            field_dict["contentRating"] = content_rating
        if status is not UNSET:
            field_dict["status"] = status
        if segment_length_chars is not UNSET:
            field_dict["segmentLengthChars"] = segment_length_chars
        if segment_duration_ms is not UNSET:
            field_dict["segmentDurationMs"] = segment_duration_ms
        if languages is not UNSET:
            field_dict["languages"] = languages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_filters_languages_type_1 import SearchFiltersLanguagesType1
        from ..models.search_filters_media import SearchFiltersMedia
        from ..models.search_filters_segment_duration_ms import SearchFiltersSegmentDurationMs
        from ..models.search_filters_segment_length_chars import SearchFiltersSegmentLengthChars

        _src = dict(src_dict)
        _media = _src.pop("media", UNSET)
        media: SearchFiltersMedia | Unset
        if isinstance(_media, Unset):
            media = UNSET
        else:
            media = SearchFiltersMedia.from_dict(_media)

        _category = _src.pop("category", UNSET)
        category: list[Category] | Unset = UNSET
        if _category is not UNSET:
            category = []
            for category_item_data in _category:
                category_item = check_category(category_item_data)

                category.append(category_item)

        _content_rating = _src.pop("contentRating", UNSET)
        content_rating: list[ContentRating] | Unset = UNSET
        if _content_rating is not UNSET:
            content_rating = []
            for content_rating_item_data in _content_rating:
                content_rating_item = check_content_rating(content_rating_item_data)

                content_rating.append(content_rating_item)

        _status = _src.pop("status", UNSET)
        status: list[SegmentStatus] | Unset = UNSET
        if _status is not UNSET:
            status = []
            for status_item_data in _status:
                status_item = check_segment_status(status_item_data)

                status.append(status_item)

        _segment_length_chars = _src.pop("segmentLengthChars", UNSET)
        segment_length_chars: SearchFiltersSegmentLengthChars | Unset
        if isinstance(_segment_length_chars, Unset):
            segment_length_chars = UNSET
        else:
            segment_length_chars = SearchFiltersSegmentLengthChars.from_dict(_segment_length_chars)

        _segment_duration_ms = _src.pop("segmentDurationMs", UNSET)
        segment_duration_ms: SearchFiltersSegmentDurationMs | Unset
        if isinstance(_segment_duration_ms, Unset):
            segment_duration_ms = UNSET
        else:
            segment_duration_ms = SearchFiltersSegmentDurationMs.from_dict(_segment_duration_ms)

        def _parse_languages(
            data: object,
        ) -> list[SearchFiltersLanguagesType0Item] | SearchFiltersLanguagesType1 | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                languages_type_0 = []
                _languages_type_0 = data
                for languages_type_0_item_data in _languages_type_0:
                    languages_type_0_item = check_search_filters_languages_type_0_item(
                        languages_type_0_item_data
                    )

                    languages_type_0.append(languages_type_0_item)

                return languages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            languages_type_1 = SearchFiltersLanguagesType1.from_dict(data)

            return languages_type_1

        languages = _parse_languages(_src.pop("languages", UNSET))

        search_filters = cls(
            media=media,
            category=category,
            content_rating=content_rating,
            status=status,
            segment_length_chars=segment_length_chars,
            segment_duration_ms=segment_duration_ms,
            languages=languages,
        )

        search_filters.additional_properties = _src
        return search_filters

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
