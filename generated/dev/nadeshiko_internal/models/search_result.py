from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.search_result_media import SearchResultMedia
    from ..models.search_result_segment import SearchResultSegment
    from ..models.search_result_urls import SearchResultUrls


T = TypeVar("T", bound="SearchResult")


@_attrs_define
class SearchResult:
    """A complete search result combining media info, segment details, and URLs

    Attributes:
        media (SearchResultMedia): Media information included in search results
        segment (SearchResultSegment): Segment details in search results
        urls (SearchResultUrls): URLs to media resources for a segment
    """

    media: SearchResultMedia
    segment: SearchResultSegment
    urls: SearchResultUrls
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media = self.media.to_dict()

        segment = self.segment.to_dict()

        urls = self.urls.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "media": media,
                "segment": segment,
                "urls": urls,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_result_media import SearchResultMedia
        from ..models.search_result_segment import SearchResultSegment
        from ..models.search_result_urls import SearchResultUrls

        d = dict(src_dict)
        media = SearchResultMedia.from_dict(d.pop("media"))

        segment = SearchResultSegment.from_dict(d.pop("segment"))

        urls = SearchResultUrls.from_dict(d.pop("urls"))

        search_result = cls(
            media=media,
            segment=segment,
            urls=urls,
        )

        search_result.additional_properties = d
        return search_result

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
