from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_request_content_sort import SearchRequestContentSort
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_request_media_item import SearchRequestMediaItem


T = TypeVar("T", bound="SearchRequest")


@_attrs_define
class SearchRequest:
    """
    Attributes:
        query (str | Unset): Text or sentence to search (null to search without query) Example: 彼女.
        limit (int | Unset): Max amount of entries by response Default: 10.
        uuid (UUID | Unset): Unique ID from sentence (Useful to get a specific sentence) Example: 3fd94cef-a3e1-31ae-
            bc8d-e743f03e9c7e.
        category (list[int] | Unset): Media category filter (1=Anime, 2=Unknown, 3=J-Drama, 4=Audiobook)
        anime_id (int | Unset): Unique ID from media Example: 5.
        season (list[int] | Unset): Array of seasons to get Example: [1].
        episode (list[int] | Unset): Array of episodes to get Example: [5, 8].
        random_seed (float | Unset): A value from 0 to 1 for random sorting Example: 0.5.
        content_sort (SearchRequestContentSort | Unset): Order by amount of characters Default:
            SearchRequestContentSort.NONE. Example: none.
        cursor (list[float] | Unset): Current page of search Example: [23.31727, 7].
        exact_match (bool | Unset): Whether to use exact phrase matching Default: False.
        extra (bool | Unset): Include extra content Default: False.
        min_length (int | Unset): Minimum content length Example: 10.
        max_length (int | Unset): Maximum content length Example: 50.
        excluded_anime_ids (list[int] | Unset): Anime IDs to exclude from results
        status (list[int] | Unset): Segment status filter
        media (list[SearchRequestMediaItem] | Unset): Media filter with seasons and episodes
    """

    query: str | Unset = UNSET
    limit: int | Unset = 10
    uuid: UUID | Unset = UNSET
    category: list[int] | Unset = UNSET
    anime_id: int | Unset = UNSET
    season: list[int] | Unset = UNSET
    episode: list[int] | Unset = UNSET
    random_seed: float | Unset = UNSET
    content_sort: SearchRequestContentSort | Unset = SearchRequestContentSort.NONE
    cursor: list[float] | Unset = UNSET
    exact_match: bool | Unset = False
    extra: bool | Unset = False
    min_length: int | Unset = UNSET
    max_length: int | Unset = UNSET
    excluded_anime_ids: list[int] | Unset = UNSET
    status: list[int] | Unset = UNSET
    media: list[SearchRequestMediaItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        limit = self.limit

        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        category: list[int] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category

        anime_id = self.anime_id

        season: list[int] | Unset = UNSET
        if not isinstance(self.season, Unset):
            season = self.season

        episode: list[int] | Unset = UNSET
        if not isinstance(self.episode, Unset):
            episode = self.episode

        random_seed = self.random_seed

        content_sort: str | Unset = UNSET
        if not isinstance(self.content_sort, Unset):
            content_sort = self.content_sort.value

        cursor: list[float] | Unset = UNSET
        if not isinstance(self.cursor, Unset):
            cursor = self.cursor

        exact_match = self.exact_match

        extra = self.extra

        min_length = self.min_length

        max_length = self.max_length

        excluded_anime_ids: list[int] | Unset = UNSET
        if not isinstance(self.excluded_anime_ids, Unset):
            excluded_anime_ids = self.excluded_anime_ids

        status: list[int] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        media: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.media, Unset):
            media = []
            for media_item_data in self.media:
                media_item = media_item_data.to_dict()
                media.append(media_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query is not UNSET:
            field_dict["query"] = query
        if limit is not UNSET:
            field_dict["limit"] = limit
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if category is not UNSET:
            field_dict["category"] = category
        if anime_id is not UNSET:
            field_dict["anime_id"] = anime_id
        if season is not UNSET:
            field_dict["season"] = season
        if episode is not UNSET:
            field_dict["episode"] = episode
        if random_seed is not UNSET:
            field_dict["random_seed"] = random_seed
        if content_sort is not UNSET:
            field_dict["content_sort"] = content_sort
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if exact_match is not UNSET:
            field_dict["exact_match"] = exact_match
        if extra is not UNSET:
            field_dict["extra"] = extra
        if min_length is not UNSET:
            field_dict["min_length"] = min_length
        if max_length is not UNSET:
            field_dict["max_length"] = max_length
        if excluded_anime_ids is not UNSET:
            field_dict["excluded_anime_ids"] = excluded_anime_ids
        if status is not UNSET:
            field_dict["status"] = status
        if media is not UNSET:
            field_dict["media"] = media

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_request_media_item import SearchRequestMediaItem

        d = dict(src_dict)
        query = d.pop("query", UNSET)

        limit = d.pop("limit", UNSET)

        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        category = cast(list[int], d.pop("category", UNSET))

        anime_id = d.pop("anime_id", UNSET)

        season = cast(list[int], d.pop("season", UNSET))

        episode = cast(list[int], d.pop("episode", UNSET))

        random_seed = d.pop("random_seed", UNSET)

        _content_sort = d.pop("content_sort", UNSET)
        content_sort: SearchRequestContentSort | Unset
        if isinstance(_content_sort, Unset):
            content_sort = UNSET
        else:
            content_sort = SearchRequestContentSort(_content_sort)

        cursor = cast(list[float], d.pop("cursor", UNSET))

        exact_match = d.pop("exact_match", UNSET)

        extra = d.pop("extra", UNSET)

        min_length = d.pop("min_length", UNSET)

        max_length = d.pop("max_length", UNSET)

        excluded_anime_ids = cast(list[int], d.pop("excluded_anime_ids", UNSET))

        status = cast(list[int], d.pop("status", UNSET))

        _media = d.pop("media", UNSET)
        media: list[SearchRequestMediaItem] | Unset = UNSET
        if _media is not UNSET:
            media = []
            for media_item_data in _media:
                media_item = SearchRequestMediaItem.from_dict(media_item_data)

                media.append(media_item)

        search_request = cls(
            query=query,
            limit=limit,
            uuid=uuid,
            category=category,
            anime_id=anime_id,
            season=season,
            episode=episode,
            random_seed=random_seed,
            content_sort=content_sort,
            cursor=cursor,
            exact_match=exact_match,
            extra=extra,
            min_length=min_length,
            max_length=max_length,
            excluded_anime_ids=excluded_anime_ids,
            status=status,
            media=media,
        )

        search_request.additional_properties = d
        return search_request

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
