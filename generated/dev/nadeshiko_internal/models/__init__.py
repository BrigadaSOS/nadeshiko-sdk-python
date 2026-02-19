"""Contains all the data models used in inputs/outputs"""

from .activity_type import ActivityType
from .add_media_to_series_body import AddMediaToSeriesBody
from .add_segment_to_collection_body import AddSegmentToCollectionBody
from .admin_report import AdminReport
from .admin_report_list_response import AdminReportListResponse
from .autocomplete_media_category import AutocompleteMediaCategory
from .category import Category
from .category_count import CategoryCount
from .character import Character
from .character_input import CharacterInput
from .character_input_role import CharacterInputRole
from .character_with_media import CharacterWithMedia
from .character_with_media_media_appearances_item import CharacterWithMediaMediaAppearancesItem
from .character_with_media_media_appearances_item_role import (
    CharacterWithMediaMediaAppearancesItemRole,
)
from .collection import Collection
from .collection_list_response import CollectionListResponse
from .collection_requests import CollectionRequests
from .collection_requests_visibility import CollectionRequestsVisibility
from .collection_visibility import CollectionVisibility
from .collection_with_segments import CollectionWithSegments
from .collection_with_segments_includes import CollectionWithSegmentsIncludes
from .collection_with_segments_includes_media import CollectionWithSegmentsIncludesMedia
from .collection_with_segments_segments_item import CollectionWithSegmentsSegmentsItem
from .collection_with_segments_visibility import CollectionWithSegmentsVisibility
from .content_rating import ContentRating
from .create_admin_review_allowlist_entry_body import CreateAdminReviewAllowlistEntryBody
from .create_report_request import CreateReportRequest
from .create_report_request_reason import CreateReportRequestReason
from .create_series_body import CreateSeriesBody
from .cursor_pagination import CursorPagination
from .delete_user_activity_response_200 import DeleteUserActivityResponse200
from .episode import Episode
from .episode_create_request import EpisodeCreateRequest
from .episode_list_response import EpisodeListResponse
from .episode_update_request import EpisodeUpdateRequest
from .error_400 import Error400
from .error_400_code import Error400Code
from .error_400_errors import Error400Errors
from .error_400_status import Error400Status
from .error_401 import Error401
from .error_401_code import Error401Code
from .error_401_errors import Error401Errors
from .error_401_status import Error401Status
from .error_403 import Error403
from .error_403_code import Error403Code
from .error_403_errors import Error403Errors
from .error_403_status import Error403Status
from .error_404 import Error404
from .error_404_code import Error404Code
from .error_404_errors import Error404Errors
from .error_404_status import Error404Status
from .error_409 import Error409
from .error_409_code import Error409Code
from .error_409_errors import Error409Errors
from .error_409_status import Error409Status
from .error_429 import Error429
from .error_429_code import Error429Code
from .error_429_errors import Error429Errors
from .error_429_status import Error429Status
from .error_500 import Error500
from .error_500_code import Error500Code
from .error_500_errors import Error500Errors
from .error_500_status import Error500Status
from .external_id import ExternalId
from .get_admin_dashboard_response_200 import GetAdminDashboardResponse200
from .get_admin_dashboard_response_200_activity import GetAdminDashboardResponse200Activity
from .get_admin_dashboard_response_200_activity_daily_activity_30d_item import (
    GetAdminDashboardResponse200ActivityDailyActivity30DItem,
)
from .get_admin_dashboard_response_200_activity_top_queries_7d_item import (
    GetAdminDashboardResponse200ActivityTopQueries7DItem,
)
from .get_admin_dashboard_response_200_media import GetAdminDashboardResponse200Media
from .get_admin_dashboard_response_200_system import GetAdminDashboardResponse200System
from .get_admin_dashboard_response_200_system_app import GetAdminDashboardResponse200SystemApp
from .get_admin_dashboard_response_200_system_database import (
    GetAdminDashboardResponse200SystemDatabase,
)
from .get_admin_dashboard_response_200_system_database_status import (
    GetAdminDashboardResponse200SystemDatabaseStatus,
)
from .get_admin_dashboard_response_200_system_elasticsearch import (
    GetAdminDashboardResponse200SystemElasticsearch,
)
from .get_admin_dashboard_response_200_system_elasticsearch_status import (
    GetAdminDashboardResponse200SystemElasticsearchStatus,
)
from .get_admin_dashboard_response_200_system_queues_item import (
    GetAdminDashboardResponse200SystemQueuesItem,
)
from .get_admin_dashboard_response_200_system_status import GetAdminDashboardResponse200SystemStatus
from .get_admin_dashboard_response_200_users import GetAdminDashboardResponse200Users
from .get_admin_health_response_200 import GetAdminHealthResponse200
from .get_admin_health_response_200_app import GetAdminHealthResponse200App
from .get_admin_health_response_200_database import GetAdminHealthResponse200Database
from .get_admin_health_response_200_database_status import GetAdminHealthResponse200DatabaseStatus
from .get_admin_health_response_200_elasticsearch import GetAdminHealthResponse200Elasticsearch
from .get_admin_health_response_200_elasticsearch_status import (
    GetAdminHealthResponse200ElasticsearchStatus,
)
from .get_admin_health_response_200_status import GetAdminHealthResponse200Status
from .get_admin_queue_queue_name import GetAdminQueueQueueName
from .get_admin_queue_response_200 import GetAdminQueueResponse200
from .get_admin_queue_response_200_metadata import GetAdminQueueResponse200Metadata
from .get_admin_queue_response_200_stats import GetAdminQueueResponse200Stats
from .get_admin_review_run_response_200 import GetAdminReviewRunResponse200
from .get_seiyuu_include_item import GetSeiyuuIncludeItem
from .get_user_activity_heatmap_response_200 import GetUserActivityHeatmapResponse200
from .get_user_activity_heatmap_response_200_counts import GetUserActivityHeatmapResponse200Counts
from .get_user_activity_stats_response_200 import GetUserActivityStatsResponse200
from .get_user_activity_stats_response_200_top_media_item import (
    GetUserActivityStatsResponse200TopMediaItem,
)
from .include_expansion import IncludeExpansion
from .list_admin_queue_failed_queue_name import ListAdminQueueFailedQueueName
from .list_admin_queue_failed_response_200_item import ListAdminQueueFailedResponse200Item
from .list_admin_queue_stats_response_200_item import ListAdminQueueStatsResponse200Item
from .list_admin_reports_source import ListAdminReportsSource
from .list_admin_reports_status import ListAdminReportsStatus
from .list_admin_reports_target_type import ListAdminReportsTargetType
from .list_admin_review_runs_response_200 import ListAdminReviewRunsResponse200
from .list_collections_visibility import ListCollectionsVisibility
from .list_media_category import ListMediaCategory
from .list_segments_response_200 import ListSegmentsResponse200
from .list_user_activity_response_200 import ListUserActivityResponse200
from .list_user_reports_status import ListUserReportsStatus
from .media import Media
from .media_autocomplete_response import MediaAutocompleteResponse
from .media_character import MediaCharacter
from .media_character_role import MediaCharacterRole
from .media_create_request import MediaCreateRequest
from .media_create_request_category import MediaCreateRequestCategory
from .media_create_request_storage import MediaCreateRequestStorage
from .media_filter_item import MediaFilterItem
from .media_include_expansion import MediaIncludeExpansion
from .media_list_response import MediaListResponse
from .media_search_stats import MediaSearchStats
from .media_search_stats_episode_hits import MediaSearchStatsEpisodeHits
from .media_update_request import MediaUpdateRequest
from .media_update_request_category import MediaUpdateRequestCategory
from .media_update_request_storage import MediaUpdateRequestStorage
from .pagination_info import PaginationInfo
from .pagination_info_estimated_total_hits_relation import PaginationInfoEstimatedTotalHitsRelation
from .purge_admin_queue_failed_queue_name import PurgeAdminQueueFailedQueueName
from .purge_admin_queue_failed_response_200 import PurgeAdminQueueFailedResponse200
from .reindex_request import ReindexRequest
from .reindex_request_media_item import ReindexRequestMediaItem
from .reindex_response import ReindexResponse
from .reindex_response_errors_item import ReindexResponseErrorsItem
from .reindex_response_stats import ReindexResponseStats
from .report import Report
from .report_data_type_0 import ReportDataType0
from .report_list_response import ReportListResponse
from .report_reason import ReportReason
from .report_source import ReportSource
from .report_status import ReportStatus
from .report_target_episode import ReportTargetEpisode
from .report_target_episode_type import ReportTargetEpisodeType
from .report_target_media import ReportTargetMedia
from .report_target_media_type import ReportTargetMediaType
from .report_target_segment import ReportTargetSegment
from .report_target_segment_type import ReportTargetSegmentType
from .retry_admin_queue_failed_queue_name import RetryAdminQueueFailedQueueName
from .retry_admin_queue_failed_response_200 import RetryAdminQueueFailedResponse200
from .review_allowlist import ReviewAllowlist
from .review_check import ReviewCheck
from .review_check_latest_run_type_0 import ReviewCheckLatestRunType0
from .review_check_run import ReviewCheckRun
from .review_check_run_threshold_used import ReviewCheckRunThresholdUsed
from .review_check_target_type import ReviewCheckTargetType
from .review_check_threshold import ReviewCheckThreshold
from .review_check_threshold_schema_item import ReviewCheckThresholdSchemaItem
from .review_check_threshold_schema_item_type import ReviewCheckThresholdSchemaItemType
from .run_admin_review_category import RunAdminReviewCategory
from .run_review_response import RunReviewResponse
from .run_review_response_checks_run_item import RunReviewResponseChecksRunItem
from .search_filters import SearchFilters
from .search_filters_languages import SearchFiltersLanguages
from .search_filters_languages_exclude_item import SearchFiltersLanguagesExcludeItem
from .search_filters_media import SearchFiltersMedia
from .search_filters_segment_duration_ms import SearchFiltersSegmentDurationMs
from .search_filters_segment_length_chars import SearchFiltersSegmentLengthChars
from .search_filters_status_item import SearchFiltersStatusItem
from .search_multiple_request import SearchMultipleRequest
from .search_multiple_request_query import SearchMultipleRequestQuery
from .search_multiple_response import SearchMultipleResponse
from .search_multiple_response_includes import SearchMultipleResponseIncludes
from .search_multiple_response_includes_media import SearchMultipleResponseIncludesMedia
from .search_request import SearchRequest
from .search_request_query import SearchRequestQuery
from .search_request_sort import SearchRequestSort
from .search_request_sort_mode import SearchRequestSortMode
from .search_response import SearchResponse
from .search_response_includes import SearchResponseIncludes
from .search_response_includes_media import SearchResponseIncludesMedia
from .search_stats_request import SearchStatsRequest
from .search_stats_request_query import SearchStatsRequestQuery
from .search_stats_response import SearchStatsResponse
from .search_stats_response_includes import SearchStatsResponseIncludes
from .search_stats_response_includes_media import SearchStatsResponseIncludesMedia
from .segment import Segment
from .segment_context_response import SegmentContextResponse
from .segment_context_response_includes import SegmentContextResponseIncludes
from .segment_context_response_includes_media import SegmentContextResponseIncludesMedia
from .segment_create_request import SegmentCreateRequest
from .segment_create_request_pos_analysis_type_0 import SegmentCreateRequestPosAnalysisType0
from .segment_create_request_rating_analysis_type_0 import SegmentCreateRequestRatingAnalysisType0
from .segment_create_request_status import SegmentCreateRequestStatus
from .segment_create_request_storage import SegmentCreateRequestStorage
from .segment_create_request_text_en import SegmentCreateRequestTextEn
from .segment_create_request_text_es import SegmentCreateRequestTextEs
from .segment_create_request_text_ja import SegmentCreateRequestTextJa
from .segment_internal import SegmentInternal
from .segment_internal_pos_analysis_type_0 import SegmentInternalPosAnalysisType0
from .segment_internal_rating_analysis_type_0 import SegmentInternalRatingAnalysisType0
from .segment_internal_storage import SegmentInternalStorage
from .segment_status import SegmentStatus
from .segment_text_en import SegmentTextEn
from .segment_text_es import SegmentTextEs
from .segment_text_ja import SegmentTextJa
from .segment_update_request import SegmentUpdateRequest
from .segment_update_request_pos_analysis_type_0 import SegmentUpdateRequestPosAnalysisType0
from .segment_update_request_rating_analysis_type_0 import SegmentUpdateRequestRatingAnalysisType0
from .segment_update_request_status import SegmentUpdateRequestStatus
from .segment_update_request_storage import SegmentUpdateRequestStorage
from .segment_update_request_text_en import SegmentUpdateRequestTextEn
from .segment_update_request_text_es import SegmentUpdateRequestTextEs
from .segment_update_request_text_ja import SegmentUpdateRequestTextJa
from .segment_urls import SegmentUrls
from .seiyuu import Seiyuu
from .seiyuu_with_roles import SeiyuuWithRoles
from .seiyuu_with_roles_characters_item import SeiyuuWithRolesCharactersItem
from .seiyuu_with_roles_characters_item_role import SeiyuuWithRolesCharactersItemRole
from .series import Series
from .series_list_response import SeriesListResponse
from .series_with_media import SeriesWithMedia
from .series_with_media_media_item import SeriesWithMediaMediaItem
from .update_admin_review_check_body import UpdateAdminReviewCheckBody
from .update_admin_review_check_body_threshold import UpdateAdminReviewCheckBodyThreshold
from .update_collection_body import UpdateCollectionBody
from .update_collection_body_visibility import UpdateCollectionBodyVisibility
from .update_collection_segment_body import UpdateCollectionSegmentBody
from .update_report_request import UpdateReportRequest
from .update_report_request_status import UpdateReportRequestStatus
from .update_series_body import UpdateSeriesBody
from .update_series_media_body import UpdateSeriesMediaBody
from .user_activity import UserActivity
from .user_export_collection import UserExportCollection
from .user_export_response import UserExportResponse
from .user_export_response_profile import UserExportResponseProfile
from .user_lab_feature import UserLabFeature
from .user_preferences import UserPreferences
from .user_preferences_anki_profiles_item import UserPreferencesAnkiProfilesItem
from .user_preferences_anki_profiles_item_fields_item import (
    UserPreferencesAnkiProfilesItemFieldsItem,
)
from .user_preferences_content_rating_preferences import UserPreferencesContentRatingPreferences
from .user_preferences_content_rating_preferences_explicit import (
    UserPreferencesContentRatingPreferencesExplicit,
)
from .user_preferences_content_rating_preferences_suggestive import (
    UserPreferencesContentRatingPreferencesSuggestive,
)
from .user_preferences_hidden_media_item import UserPreferencesHiddenMediaItem
from .user_preferences_labs import UserPreferencesLabs
from .user_preferences_media_name_language import UserPreferencesMediaNameLanguage
from .user_preferences_search_history import UserPreferencesSearchHistory
from .user_quota_response import UserQuotaResponse
from .word_match import WordMatch
from .word_match_media import WordMatchMedia

__all__ = (
    "ActivityType",
    "AddMediaToSeriesBody",
    "AddSegmentToCollectionBody",
    "AdminReport",
    "AdminReportListResponse",
    "AutocompleteMediaCategory",
    "Category",
    "CategoryCount",
    "Character",
    "CharacterInput",
    "CharacterInputRole",
    "CharacterWithMedia",
    "CharacterWithMediaMediaAppearancesItem",
    "CharacterWithMediaMediaAppearancesItemRole",
    "Collection",
    "CollectionListResponse",
    "CollectionRequests",
    "CollectionRequestsVisibility",
    "CollectionVisibility",
    "CollectionWithSegments",
    "CollectionWithSegmentsIncludes",
    "CollectionWithSegmentsIncludesMedia",
    "CollectionWithSegmentsSegmentsItem",
    "CollectionWithSegmentsVisibility",
    "ContentRating",
    "CreateAdminReviewAllowlistEntryBody",
    "CreateReportRequest",
    "CreateReportRequestReason",
    "CreateSeriesBody",
    "CursorPagination",
    "DeleteUserActivityResponse200",
    "Episode",
    "EpisodeCreateRequest",
    "EpisodeListResponse",
    "EpisodeUpdateRequest",
    "Error400",
    "Error400Code",
    "Error400Errors",
    "Error400Status",
    "Error401",
    "Error401Code",
    "Error401Errors",
    "Error401Status",
    "Error403",
    "Error403Code",
    "Error403Errors",
    "Error403Status",
    "Error404",
    "Error404Code",
    "Error404Errors",
    "Error404Status",
    "Error409",
    "Error409Code",
    "Error409Errors",
    "Error409Status",
    "Error429",
    "Error429Code",
    "Error429Errors",
    "Error429Status",
    "Error500",
    "Error500Code",
    "Error500Errors",
    "Error500Status",
    "ExternalId",
    "GetAdminDashboardResponse200",
    "GetAdminDashboardResponse200Activity",
    "GetAdminDashboardResponse200ActivityDailyActivity30DItem",
    "GetAdminDashboardResponse200ActivityTopQueries7DItem",
    "GetAdminDashboardResponse200Media",
    "GetAdminDashboardResponse200System",
    "GetAdminDashboardResponse200SystemApp",
    "GetAdminDashboardResponse200SystemDatabase",
    "GetAdminDashboardResponse200SystemDatabaseStatus",
    "GetAdminDashboardResponse200SystemElasticsearch",
    "GetAdminDashboardResponse200SystemElasticsearchStatus",
    "GetAdminDashboardResponse200SystemQueuesItem",
    "GetAdminDashboardResponse200SystemStatus",
    "GetAdminDashboardResponse200Users",
    "GetAdminHealthResponse200",
    "GetAdminHealthResponse200App",
    "GetAdminHealthResponse200Database",
    "GetAdminHealthResponse200DatabaseStatus",
    "GetAdminHealthResponse200Elasticsearch",
    "GetAdminHealthResponse200ElasticsearchStatus",
    "GetAdminHealthResponse200Status",
    "GetAdminQueueQueueName",
    "GetAdminQueueResponse200",
    "GetAdminQueueResponse200Metadata",
    "GetAdminQueueResponse200Stats",
    "GetAdminReviewRunResponse200",
    "GetSeiyuuIncludeItem",
    "GetUserActivityHeatmapResponse200",
    "GetUserActivityHeatmapResponse200Counts",
    "GetUserActivityStatsResponse200",
    "GetUserActivityStatsResponse200TopMediaItem",
    "IncludeExpansion",
    "ListAdminQueueFailedQueueName",
    "ListAdminQueueFailedResponse200Item",
    "ListAdminQueueStatsResponse200Item",
    "ListAdminReportsSource",
    "ListAdminReportsStatus",
    "ListAdminReportsTargetType",
    "ListAdminReviewRunsResponse200",
    "ListCollectionsVisibility",
    "ListMediaCategory",
    "ListSegmentsResponse200",
    "ListUserActivityResponse200",
    "ListUserReportsStatus",
    "Media",
    "MediaAutocompleteResponse",
    "MediaCharacter",
    "MediaCharacterRole",
    "MediaCreateRequest",
    "MediaCreateRequestCategory",
    "MediaCreateRequestStorage",
    "MediaFilterItem",
    "MediaIncludeExpansion",
    "MediaListResponse",
    "MediaSearchStats",
    "MediaSearchStatsEpisodeHits",
    "MediaUpdateRequest",
    "MediaUpdateRequestCategory",
    "MediaUpdateRequestStorage",
    "PaginationInfo",
    "PaginationInfoEstimatedTotalHitsRelation",
    "PurgeAdminQueueFailedQueueName",
    "PurgeAdminQueueFailedResponse200",
    "ReindexRequest",
    "ReindexRequestMediaItem",
    "ReindexResponse",
    "ReindexResponseErrorsItem",
    "ReindexResponseStats",
    "Report",
    "ReportDataType0",
    "ReportListResponse",
    "ReportReason",
    "ReportSource",
    "ReportStatus",
    "ReportTargetEpisode",
    "ReportTargetEpisodeType",
    "ReportTargetMedia",
    "ReportTargetMediaType",
    "ReportTargetSegment",
    "ReportTargetSegmentType",
    "RetryAdminQueueFailedQueueName",
    "RetryAdminQueueFailedResponse200",
    "ReviewAllowlist",
    "ReviewCheck",
    "ReviewCheckLatestRunType0",
    "ReviewCheckRun",
    "ReviewCheckRunThresholdUsed",
    "ReviewCheckTargetType",
    "ReviewCheckThreshold",
    "ReviewCheckThresholdSchemaItem",
    "ReviewCheckThresholdSchemaItemType",
    "RunAdminReviewCategory",
    "RunReviewResponse",
    "RunReviewResponseChecksRunItem",
    "SearchFilters",
    "SearchFiltersLanguages",
    "SearchFiltersLanguagesExcludeItem",
    "SearchFiltersMedia",
    "SearchFiltersSegmentDurationMs",
    "SearchFiltersSegmentLengthChars",
    "SearchFiltersStatusItem",
    "SearchMultipleRequest",
    "SearchMultipleRequestQuery",
    "SearchMultipleResponse",
    "SearchMultipleResponseIncludes",
    "SearchMultipleResponseIncludesMedia",
    "SearchRequest",
    "SearchRequestQuery",
    "SearchRequestSort",
    "SearchRequestSortMode",
    "SearchResponse",
    "SearchResponseIncludes",
    "SearchResponseIncludesMedia",
    "SearchStatsRequest",
    "SearchStatsRequestQuery",
    "SearchStatsResponse",
    "SearchStatsResponseIncludes",
    "SearchStatsResponseIncludesMedia",
    "Segment",
    "SegmentContextResponse",
    "SegmentContextResponseIncludes",
    "SegmentContextResponseIncludesMedia",
    "SegmentCreateRequest",
    "SegmentCreateRequestPosAnalysisType0",
    "SegmentCreateRequestRatingAnalysisType0",
    "SegmentCreateRequestStatus",
    "SegmentCreateRequestStorage",
    "SegmentCreateRequestTextEn",
    "SegmentCreateRequestTextEs",
    "SegmentCreateRequestTextJa",
    "SegmentInternal",
    "SegmentInternalPosAnalysisType0",
    "SegmentInternalRatingAnalysisType0",
    "SegmentInternalStorage",
    "SegmentStatus",
    "SegmentTextEn",
    "SegmentTextEs",
    "SegmentTextJa",
    "SegmentUpdateRequest",
    "SegmentUpdateRequestPosAnalysisType0",
    "SegmentUpdateRequestRatingAnalysisType0",
    "SegmentUpdateRequestStatus",
    "SegmentUpdateRequestStorage",
    "SegmentUpdateRequestTextEn",
    "SegmentUpdateRequestTextEs",
    "SegmentUpdateRequestTextJa",
    "SegmentUrls",
    "Seiyuu",
    "SeiyuuWithRoles",
    "SeiyuuWithRolesCharactersItem",
    "SeiyuuWithRolesCharactersItemRole",
    "Series",
    "SeriesListResponse",
    "SeriesWithMedia",
    "SeriesWithMediaMediaItem",
    "UpdateAdminReviewCheckBody",
    "UpdateAdminReviewCheckBodyThreshold",
    "UpdateCollectionBody",
    "UpdateCollectionBodyVisibility",
    "UpdateCollectionSegmentBody",
    "UpdateReportRequest",
    "UpdateReportRequestStatus",
    "UpdateSeriesBody",
    "UpdateSeriesMediaBody",
    "UserActivity",
    "UserExportCollection",
    "UserExportResponse",
    "UserExportResponseProfile",
    "UserLabFeature",
    "UserPreferences",
    "UserPreferencesAnkiProfilesItem",
    "UserPreferencesAnkiProfilesItemFieldsItem",
    "UserPreferencesContentRatingPreferences",
    "UserPreferencesContentRatingPreferencesExplicit",
    "UserPreferencesContentRatingPreferencesSuggestive",
    "UserPreferencesHiddenMediaItem",
    "UserPreferencesLabs",
    "UserPreferencesMediaNameLanguage",
    "UserPreferencesSearchHistory",
    "UserQuotaResponse",
    "WordMatch",
    "WordMatchMedia",
)
