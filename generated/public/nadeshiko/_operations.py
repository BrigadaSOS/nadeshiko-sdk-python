from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class OperationMetadata:
    name: str
    module_path: str
    paginated: bool = False
    doc: str = ''


OPERATIONS: tuple[OperationMetadata, ...] = (
    OperationMetadata(name="add_excluded_media", module_path=".api.user.add_excluded_media", paginated=False, doc="Exclude media from search results"),
    OperationMetadata(name="add_segment_to_collection", module_path=".api.collections.add_segment_to_collection", paginated=False, doc="Add segment to collection"),
    OperationMetadata(name="create_collection", module_path=".api.collections.create_collection", paginated=False, doc="Create collection"),
    OperationMetadata(name="delete_collection", module_path=".api.collections.delete_collection", paginated=False, doc="Delete collection"),
    OperationMetadata(name="get_collection", module_path=".api.collections.get_collection", paginated=False, doc="Get collection details"),
    OperationMetadata(name="get_episode", module_path=".api.media.get_episode", paginated=False, doc="Get single episode"),
    OperationMetadata(name="get_me", module_path=".api.user.get_me", paginated=False, doc="Get current user profile"),
    OperationMetadata(name="get_media", module_path=".api.media.get_media", paginated=False, doc="Get single media"),
    OperationMetadata(name="get_search_stats", module_path=".api.search.get_search_stats", paginated=False, doc="Get search statistics"),
    OperationMetadata(name="get_segment", module_path=".api.media.get_segment", paginated=False, doc="Get single segment"),
    OperationMetadata(name="get_segment_context", module_path=".api.media.get_segment_context", paginated=False, doc="Get surrounding context for a segment"),
    OperationMetadata(name="get_stats_overview", module_path=".api.stats.get_stats_overview", paginated=False, doc="Get corpus statistics overview"),
    OperationMetadata(name="get_user_activity_heatmap", module_path=".api.activity.get_user_activity_heatmap", paginated=False, doc="Get activity heatmap data"),
    OperationMetadata(name="get_user_activity_stats", module_path=".api.activity.get_user_activity_stats", paginated=False, doc="Get user activity statistics"),
    OperationMetadata(name="list_collections", module_path=".api.collections.list_collections", paginated=True, doc="List collections"),
    OperationMetadata(name="list_episodes", module_path=".api.media.list_episodes", paginated=True, doc="List episodes for a media"),
    OperationMetadata(name="list_excluded_media", module_path=".api.user.list_excluded_media", paginated=False, doc="List excluded media"),
    OperationMetadata(name="list_media", module_path=".api.media.list_media", paginated=True, doc="List all media"),
    OperationMetadata(name="list_user_activity", module_path=".api.activity.list_user_activity", paginated=True, doc="List user activity"),
    OperationMetadata(name="remove_excluded_media", module_path=".api.user.remove_excluded_media", paginated=False, doc="Remove media from excluded list"),
    OperationMetadata(name="remove_segment_from_collection", module_path=".api.collections.remove_segment_from_collection", paginated=False, doc="Remove segment from collection"),
    OperationMetadata(name="search", module_path=".api.search.search", paginated=True, doc="Search segments by query"),
    OperationMetadata(name="search_collection_segments", module_path=".api.collections.search_collection_segments", paginated=True, doc="Search segments in a collection"),
    OperationMetadata(name="search_media", module_path=".api.search.search_media", paginated=False, doc="Find media by name"),
    OperationMetadata(name="search_words", module_path=".api.search.search_words", paginated=False, doc="Search by multiple words"),
)
