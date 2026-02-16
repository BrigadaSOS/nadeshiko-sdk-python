from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.category import Category
from ..models.search_request_content_sort import SearchRequestContentSort
from ..models.search_request_status_item import SearchRequestStatusItem
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
        uuid (UUID | Unset): Unique ID from segment (Useful to get a specific segment) Example: 3fd94cef-a3e1-31ae-
            bc8d-e743f03e9c7e.
        category (list[Category] | Unset): Media category filter
        media_id (int | Unset): Unique ID from media Example: 5.
        episode (list[int] | Unset): Array of episodes to get Example: [5, 8].
        random_seed (int | Unset): Non-negative integer seed for deterministic random sorting Example: 42.
        content_sort (SearchRequestContentSort | Unset): Order by amount of characters Default:
            SearchRequestContentSort.NONE. Example: NONE.
        cursor (list[float] | Unset): Current page of search Example: [23.31727, 7].
        exact_match (bool | Unset): Whether to use exact phrase matching Default: False.
        min_length (int | Unset): Minimum content length Example: 10.
        max_length (int | Unset): Maximum content length Example: 50.
        excluded_media_ids (list[int] | Unset): Media IDs to exclude from results
        status (list[SearchRequestStatusItem] | Unset): Segment status filter
        media (list[SearchRequestMediaItem] | Unset): Media filter with episodes
    """

    query: str | Unset = UNSET
    limit: int | Unset = 10
    uuid: UUID | Unset = UNSET
    category: list[Category] | Unset = UNSET
    media_id: int | Unset = UNSET
    episode: list[int] | Unset = UNSET
    random_seed: int | Unset = UNSET
    content_sort: SearchRequestContentSort | Unset = SearchRequestContentSort.NONE
    cursor: list[float] | Unset = UNSET
    exact_match: bool | Unset = False
    min_length: int | Unset = UNSET
    max_length: int | Unset = UNSET
    excluded_media_ids: list[int] | Unset = UNSET
    status: list[SearchRequestStatusItem] | Unset = UNSET
    media: list[SearchRequestMediaItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        limit = self.limit

        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        category: list[str] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = []
            for category_item_data in self.category:
                category_item = category_item_data.value
                category.append(category_item)

        media_id = self.media_id

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

        min_length = self.min_length

        max_length = self.max_length

        excluded_media_ids: list[int] | Unset = UNSET
        if not isinstance(self.excluded_media_ids, Unset):
            excluded_media_ids = self.excluded_media_ids

        status: list[str] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = []
            for status_item_data in self.status:
                status_item = status_item_data.value
                status.append(status_item)

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
        if media_id is not UNSET:
            field_dict["mediaId"] = media_id
        if episode is not UNSET:
            field_dict["episode"] = episode
        if random_seed is not UNSET:
            field_dict["randomSeed"] = random_seed
        if content_sort is not UNSET:
            field_dict["contentSort"] = content_sort
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if exact_match is not UNSET:
            field_dict["exactMatch"] = exact_match
        if min_length is not UNSET:
            field_dict["minLength"] = min_length
        if max_length is not UNSET:
            field_dict["maxLength"] = max_length
        if excluded_media_ids is not UNSET:
            field_dict["excludedMediaIds"] = excluded_media_ids
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

        _category = d.pop("category", UNSET)
        category: list[Category] | Unset = UNSET
        if _category is not UNSET:
            category = []
            for category_item_data in _category:
                category_item = Category(category_item_data)

                category.append(category_item)

        media_id = d.pop("mediaId", UNSET)

        episode = cast(list[int], d.pop("episode", UNSET))

        random_seed = d.pop("randomSeed", UNSET)

        _content_sort = d.pop("contentSort", UNSET)
        content_sort: SearchRequestContentSort | Unset
        if isinstance(_content_sort, Unset):
            content_sort = UNSET
        else:
            content_sort = SearchRequestContentSort(_content_sort)

        cursor = cast(list[float], d.pop("cursor", UNSET))

        exact_match = d.pop("exactMatch", UNSET)

        min_length = d.pop("minLength", UNSET)

        max_length = d.pop("maxLength", UNSET)

        excluded_media_ids = cast(list[int], d.pop("excludedMediaIds", UNSET))

        _status = d.pop("status", UNSET)
        status: list[SearchRequestStatusItem] | Unset = UNSET
        if _status is not UNSET:
            status = []
            for status_item_data in _status:
                status_item = SearchRequestStatusItem(status_item_data)

                status.append(status_item)

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
            media_id=media_id,
            episode=episode,
            random_seed=random_seed,
            content_sort=content_sort,
            cursor=cursor,
            exact_match=exact_match,
            min_length=min_length,
            max_length=max_length,
            excluded_media_ids=excluded_media_ids,
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
