from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_admin_dashboard_media_response_200_by_category_item import (
        GetAdminDashboardMediaResponse200ByCategoryItem,
    )
    from ..models.get_admin_dashboard_media_response_200_by_format_item import (
        GetAdminDashboardMediaResponse200ByFormatItem,
    )
    from ..models.get_admin_dashboard_media_response_200_by_genre_item import (
        GetAdminDashboardMediaResponse200ByGenreItem,
    )
    from ..models.get_admin_dashboard_media_response_200_by_status_item import (
        GetAdminDashboardMediaResponse200ByStatusItem,
    )
    from ..models.get_admin_dashboard_media_response_200_by_studio_item import (
        GetAdminDashboardMediaResponse200ByStudioItem,
    )
    from ..models.get_admin_dashboard_media_response_200_segments_by_content_rating_item import (
        GetAdminDashboardMediaResponse200SegmentsByContentRatingItem,
    )
    from ..models.get_admin_dashboard_media_response_200_segments_by_status_item import (
        GetAdminDashboardMediaResponse200SegmentsByStatusItem,
    )
    from ..models.get_admin_dashboard_media_response_200_top_media_by_exports_item import (
        GetAdminDashboardMediaResponse200TopMediaByExportsItem,
    )
    from ..models.get_admin_dashboard_media_response_200_top_media_by_plays_item import (
        GetAdminDashboardMediaResponse200TopMediaByPlaysItem,
    )
    from ..models.get_admin_dashboard_media_response_200_top_media_by_searches_item import (
        GetAdminDashboardMediaResponse200TopMediaBySearchesItem,
    )


T = TypeVar("T", bound="GetAdminDashboardMediaResponse200")


@_attrs_define
class GetAdminDashboardMediaResponse200:
    """
    Attributes:
        by_category (list[GetAdminDashboardMediaResponse200ByCategoryItem]):
        by_format (list[GetAdminDashboardMediaResponse200ByFormatItem]):
        by_status (list[GetAdminDashboardMediaResponse200ByStatusItem]):
        by_genre (list[GetAdminDashboardMediaResponse200ByGenreItem]):
        by_studio (list[GetAdminDashboardMediaResponse200ByStudioItem]):
        segments_by_content_rating (list[GetAdminDashboardMediaResponse200SegmentsByContentRatingItem]):
        segments_by_status (list[GetAdminDashboardMediaResponse200SegmentsByStatusItem]):
        top_media_by_plays (list[GetAdminDashboardMediaResponse200TopMediaByPlaysItem]):
        top_media_by_searches (list[GetAdminDashboardMediaResponse200TopMediaBySearchesItem]):
        top_media_by_exports (list[GetAdminDashboardMediaResponse200TopMediaByExportsItem]):
    """

    by_category: list[GetAdminDashboardMediaResponse200ByCategoryItem]
    by_format: list[GetAdminDashboardMediaResponse200ByFormatItem]
    by_status: list[GetAdminDashboardMediaResponse200ByStatusItem]
    by_genre: list[GetAdminDashboardMediaResponse200ByGenreItem]
    by_studio: list[GetAdminDashboardMediaResponse200ByStudioItem]
    segments_by_content_rating: list[GetAdminDashboardMediaResponse200SegmentsByContentRatingItem]
    segments_by_status: list[GetAdminDashboardMediaResponse200SegmentsByStatusItem]
    top_media_by_plays: list[GetAdminDashboardMediaResponse200TopMediaByPlaysItem]
    top_media_by_searches: list[GetAdminDashboardMediaResponse200TopMediaBySearchesItem]
    top_media_by_exports: list[GetAdminDashboardMediaResponse200TopMediaByExportsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        by_category = []
        for by_category_item_data in self.by_category:
            by_category_item = by_category_item_data.to_dict()
            by_category.append(by_category_item)

        by_format = []
        for by_format_item_data in self.by_format:
            by_format_item = by_format_item_data.to_dict()
            by_format.append(by_format_item)

        by_status = []
        for by_status_item_data in self.by_status:
            by_status_item = by_status_item_data.to_dict()
            by_status.append(by_status_item)

        by_genre = []
        for by_genre_item_data in self.by_genre:
            by_genre_item = by_genre_item_data.to_dict()
            by_genre.append(by_genre_item)

        by_studio = []
        for by_studio_item_data in self.by_studio:
            by_studio_item = by_studio_item_data.to_dict()
            by_studio.append(by_studio_item)

        segments_by_content_rating = []
        for segments_by_content_rating_item_data in self.segments_by_content_rating:
            segments_by_content_rating_item = segments_by_content_rating_item_data.to_dict()
            segments_by_content_rating.append(segments_by_content_rating_item)

        segments_by_status = []
        for segments_by_status_item_data in self.segments_by_status:
            segments_by_status_item = segments_by_status_item_data.to_dict()
            segments_by_status.append(segments_by_status_item)

        top_media_by_plays = []
        for top_media_by_plays_item_data in self.top_media_by_plays:
            top_media_by_plays_item = top_media_by_plays_item_data.to_dict()
            top_media_by_plays.append(top_media_by_plays_item)

        top_media_by_searches = []
        for top_media_by_searches_item_data in self.top_media_by_searches:
            top_media_by_searches_item = top_media_by_searches_item_data.to_dict()
            top_media_by_searches.append(top_media_by_searches_item)

        top_media_by_exports = []
        for top_media_by_exports_item_data in self.top_media_by_exports:
            top_media_by_exports_item = top_media_by_exports_item_data.to_dict()
            top_media_by_exports.append(top_media_by_exports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "byCategory": by_category,
                "byFormat": by_format,
                "byStatus": by_status,
                "byGenre": by_genre,
                "byStudio": by_studio,
                "segmentsByContentRating": segments_by_content_rating,
                "segmentsByStatus": segments_by_status,
                "topMediaByPlays": top_media_by_plays,
                "topMediaBySearches": top_media_by_searches,
                "topMediaByExports": top_media_by_exports,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_admin_dashboard_media_response_200_by_category_item import (
            GetAdminDashboardMediaResponse200ByCategoryItem,
        )
        from ..models.get_admin_dashboard_media_response_200_by_format_item import (
            GetAdminDashboardMediaResponse200ByFormatItem,
        )
        from ..models.get_admin_dashboard_media_response_200_by_genre_item import (
            GetAdminDashboardMediaResponse200ByGenreItem,
        )
        from ..models.get_admin_dashboard_media_response_200_by_status_item import (
            GetAdminDashboardMediaResponse200ByStatusItem,
        )
        from ..models.get_admin_dashboard_media_response_200_by_studio_item import (
            GetAdminDashboardMediaResponse200ByStudioItem,
        )
        from ..models.get_admin_dashboard_media_response_200_segments_by_content_rating_item import (
            GetAdminDashboardMediaResponse200SegmentsByContentRatingItem,
        )
        from ..models.get_admin_dashboard_media_response_200_segments_by_status_item import (
            GetAdminDashboardMediaResponse200SegmentsByStatusItem,
        )
        from ..models.get_admin_dashboard_media_response_200_top_media_by_exports_item import (
            GetAdminDashboardMediaResponse200TopMediaByExportsItem,
        )
        from ..models.get_admin_dashboard_media_response_200_top_media_by_plays_item import (
            GetAdminDashboardMediaResponse200TopMediaByPlaysItem,
        )
        from ..models.get_admin_dashboard_media_response_200_top_media_by_searches_item import (
            GetAdminDashboardMediaResponse200TopMediaBySearchesItem,
        )

        d = dict(src_dict)
        by_category = []
        _by_category = d.pop("byCategory")
        for by_category_item_data in _by_category:
            by_category_item = GetAdminDashboardMediaResponse200ByCategoryItem.from_dict(
                by_category_item_data
            )

            by_category.append(by_category_item)

        by_format = []
        _by_format = d.pop("byFormat")
        for by_format_item_data in _by_format:
            by_format_item = GetAdminDashboardMediaResponse200ByFormatItem.from_dict(
                by_format_item_data
            )

            by_format.append(by_format_item)

        by_status = []
        _by_status = d.pop("byStatus")
        for by_status_item_data in _by_status:
            by_status_item = GetAdminDashboardMediaResponse200ByStatusItem.from_dict(
                by_status_item_data
            )

            by_status.append(by_status_item)

        by_genre = []
        _by_genre = d.pop("byGenre")
        for by_genre_item_data in _by_genre:
            by_genre_item = GetAdminDashboardMediaResponse200ByGenreItem.from_dict(
                by_genre_item_data
            )

            by_genre.append(by_genre_item)

        by_studio = []
        _by_studio = d.pop("byStudio")
        for by_studio_item_data in _by_studio:
            by_studio_item = GetAdminDashboardMediaResponse200ByStudioItem.from_dict(
                by_studio_item_data
            )

            by_studio.append(by_studio_item)

        segments_by_content_rating = []
        _segments_by_content_rating = d.pop("segmentsByContentRating")
        for segments_by_content_rating_item_data in _segments_by_content_rating:
            segments_by_content_rating_item = (
                GetAdminDashboardMediaResponse200SegmentsByContentRatingItem.from_dict(
                    segments_by_content_rating_item_data
                )
            )

            segments_by_content_rating.append(segments_by_content_rating_item)

        segments_by_status = []
        _segments_by_status = d.pop("segmentsByStatus")
        for segments_by_status_item_data in _segments_by_status:
            segments_by_status_item = (
                GetAdminDashboardMediaResponse200SegmentsByStatusItem.from_dict(
                    segments_by_status_item_data
                )
            )

            segments_by_status.append(segments_by_status_item)

        top_media_by_plays = []
        _top_media_by_plays = d.pop("topMediaByPlays")
        for top_media_by_plays_item_data in _top_media_by_plays:
            top_media_by_plays_item = (
                GetAdminDashboardMediaResponse200TopMediaByPlaysItem.from_dict(
                    top_media_by_plays_item_data
                )
            )

            top_media_by_plays.append(top_media_by_plays_item)

        top_media_by_searches = []
        _top_media_by_searches = d.pop("topMediaBySearches")
        for top_media_by_searches_item_data in _top_media_by_searches:
            top_media_by_searches_item = (
                GetAdminDashboardMediaResponse200TopMediaBySearchesItem.from_dict(
                    top_media_by_searches_item_data
                )
            )

            top_media_by_searches.append(top_media_by_searches_item)

        top_media_by_exports = []
        _top_media_by_exports = d.pop("topMediaByExports")
        for top_media_by_exports_item_data in _top_media_by_exports:
            top_media_by_exports_item = (
                GetAdminDashboardMediaResponse200TopMediaByExportsItem.from_dict(
                    top_media_by_exports_item_data
                )
            )

            top_media_by_exports.append(top_media_by_exports_item)

        get_admin_dashboard_media_response_200 = cls(
            by_category=by_category,
            by_format=by_format,
            by_status=by_status,
            by_genre=by_genre,
            by_studio=by_studio,
            segments_by_content_rating=segments_by_content_rating,
            segments_by_status=segments_by_status,
            top_media_by_plays=top_media_by_plays,
            top_media_by_searches=top_media_by_searches,
            top_media_by_exports=top_media_by_exports,
        )

        get_admin_dashboard_media_response_200.additional_properties = d
        return get_admin_dashboard_media_response_200

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
