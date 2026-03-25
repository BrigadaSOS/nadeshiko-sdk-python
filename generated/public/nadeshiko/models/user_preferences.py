from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.user_preferences_media_name_language import UserPreferencesMediaNameLanguage
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_preferences_anki_profiles_item import UserPreferencesAnkiProfilesItem
    from ..models.user_preferences_content_rating_preferences import (
        UserPreferencesContentRatingPreferences,
    )
    from ..models.user_preferences_hidden_media_item import UserPreferencesHiddenMediaItem
    from ..models.user_preferences_search_history import UserPreferencesSearchHistory


T = TypeVar("T", bound="UserPreferences")


@_attrs_define
class UserPreferences:
    """
    Attributes:
        media_name_language (UserPreferencesMediaNameLanguage | Unset): Preferred language for media names display
        content_rating_preferences (UserPreferencesContentRatingPreferences | Unset): Per-category content rating
            display preferences
        search_history (UserPreferencesSearchHistory | Unset):
        blog_last_visited (datetime.datetime | Unset): ISO timestamp of when the user last visited the blog page
        anki_profiles (list[UserPreferencesAnkiProfilesItem] | Unset):
        hidden_media (list[UserPreferencesHiddenMediaItem] | Unset): Media hidden from search results by the user
    """

    media_name_language: UserPreferencesMediaNameLanguage | Unset = UNSET
    content_rating_preferences: UserPreferencesContentRatingPreferences | Unset = UNSET
    search_history: UserPreferencesSearchHistory | Unset = UNSET
    blog_last_visited: datetime.datetime | Unset = UNSET
    anki_profiles: list[UserPreferencesAnkiProfilesItem] | Unset = UNSET
    hidden_media: list[UserPreferencesHiddenMediaItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media_name_language: str | Unset = UNSET
        if not isinstance(self.media_name_language, Unset):
            media_name_language = self.media_name_language.value

        content_rating_preferences: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content_rating_preferences, Unset):
            content_rating_preferences = self.content_rating_preferences.to_dict()

        search_history: dict[str, Any] | Unset = UNSET
        if not isinstance(self.search_history, Unset):
            search_history = self.search_history.to_dict()

        blog_last_visited: str | Unset = UNSET
        if not isinstance(self.blog_last_visited, Unset):
            blog_last_visited = self.blog_last_visited.isoformat()

        anki_profiles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.anki_profiles, Unset):
            anki_profiles = []
            for anki_profiles_item_data in self.anki_profiles:
                anki_profiles_item = anki_profiles_item_data.to_dict()
                anki_profiles.append(anki_profiles_item)

        hidden_media: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hidden_media, Unset):
            hidden_media = []
            for hidden_media_item_data in self.hidden_media:
                hidden_media_item = hidden_media_item_data.to_dict()
                hidden_media.append(hidden_media_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if media_name_language is not UNSET:
            field_dict["mediaNameLanguage"] = media_name_language
        if content_rating_preferences is not UNSET:
            field_dict["contentRatingPreferences"] = content_rating_preferences
        if search_history is not UNSET:
            field_dict["searchHistory"] = search_history
        if blog_last_visited is not UNSET:
            field_dict["blogLastVisited"] = blog_last_visited
        if anki_profiles is not UNSET:
            field_dict["ankiProfiles"] = anki_profiles
        if hidden_media is not UNSET:
            field_dict["hiddenMedia"] = hidden_media

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_preferences_anki_profiles_item import UserPreferencesAnkiProfilesItem
        from ..models.user_preferences_content_rating_preferences import (
            UserPreferencesContentRatingPreferences,
        )
        from ..models.user_preferences_hidden_media_item import UserPreferencesHiddenMediaItem
        from ..models.user_preferences_search_history import UserPreferencesSearchHistory

        _src = dict(src_dict)
        _media_name_language = _src.pop("mediaNameLanguage", UNSET)
        media_name_language: UserPreferencesMediaNameLanguage | Unset
        if isinstance(_media_name_language, Unset):
            media_name_language = UNSET
        else:
            media_name_language = UserPreferencesMediaNameLanguage(_media_name_language)

        _content_rating_preferences = _src.pop("contentRatingPreferences", UNSET)
        content_rating_preferences: UserPreferencesContentRatingPreferences | Unset
        if isinstance(_content_rating_preferences, Unset):
            content_rating_preferences = UNSET
        else:
            content_rating_preferences = UserPreferencesContentRatingPreferences.from_dict(
                _content_rating_preferences
            )

        _search_history = _src.pop("searchHistory", UNSET)
        search_history: UserPreferencesSearchHistory | Unset
        if isinstance(_search_history, Unset):
            search_history = UNSET
        else:
            search_history = UserPreferencesSearchHistory.from_dict(_search_history)

        _blog_last_visited = _src.pop("blogLastVisited", UNSET)
        blog_last_visited: datetime.datetime | Unset
        if isinstance(_blog_last_visited, Unset):
            blog_last_visited = UNSET
        else:
            blog_last_visited = isoparse(_blog_last_visited)

        _anki_profiles = _src.pop("ankiProfiles", UNSET)
        anki_profiles: list[UserPreferencesAnkiProfilesItem] | Unset = UNSET
        if _anki_profiles is not UNSET:
            anki_profiles = []
            for anki_profiles_item_data in _anki_profiles:
                anki_profiles_item = UserPreferencesAnkiProfilesItem.from_dict(
                    anki_profiles_item_data
                )

                anki_profiles.append(anki_profiles_item)

        _hidden_media = _src.pop("hiddenMedia", UNSET)
        hidden_media: list[UserPreferencesHiddenMediaItem] | Unset = UNSET
        if _hidden_media is not UNSET:
            hidden_media = []
            for hidden_media_item_data in _hidden_media:
                hidden_media_item = UserPreferencesHiddenMediaItem.from_dict(hidden_media_item_data)

                hidden_media.append(hidden_media_item)

        user_preferences = cls(
            media_name_language=media_name_language,
            content_rating_preferences=content_rating_preferences,
            search_history=search_history,
            blog_last_visited=blog_last_visited,
            anki_profiles=anki_profiles,
            hidden_media=hidden_media,
        )

        user_preferences.additional_properties = _src
        return user_preferences

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
