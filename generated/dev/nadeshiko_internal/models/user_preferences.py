from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_preferences_media_name_language import UserPreferencesMediaNameLanguage
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_preferences_labs import UserPreferencesLabs
    from ..models.user_preferences_search_history import UserPreferencesSearchHistory


T = TypeVar("T", bound="UserPreferences")


@_attrs_define
class UserPreferences:
    """
    Attributes:
        labs (UserPreferencesLabs | Unset): Lab feature opt-in flags keyed by feature key
        media_name_language (UserPreferencesMediaNameLanguage | Unset): Preferred language for media names display
        search_history (UserPreferencesSearchHistory | Unset):
    """

    labs: UserPreferencesLabs | Unset = UNSET
    media_name_language: UserPreferencesMediaNameLanguage | Unset = UNSET
    search_history: UserPreferencesSearchHistory | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        labs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labs, Unset):
            labs = self.labs.to_dict()

        media_name_language: str | Unset = UNSET
        if not isinstance(self.media_name_language, Unset):
            media_name_language = self.media_name_language.value

        search_history: dict[str, Any] | Unset = UNSET
        if not isinstance(self.search_history, Unset):
            search_history = self.search_history.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if labs is not UNSET:
            field_dict["labs"] = labs
        if media_name_language is not UNSET:
            field_dict["mediaNameLanguage"] = media_name_language
        if search_history is not UNSET:
            field_dict["searchHistory"] = search_history

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_preferences_labs import UserPreferencesLabs
        from ..models.user_preferences_search_history import UserPreferencesSearchHistory

        d = dict(src_dict)
        _labs = d.pop("labs", UNSET)
        labs: UserPreferencesLabs | Unset
        if isinstance(_labs, Unset):
            labs = UNSET
        else:
            labs = UserPreferencesLabs.from_dict(_labs)

        _media_name_language = d.pop("mediaNameLanguage", UNSET)
        media_name_language: UserPreferencesMediaNameLanguage | Unset
        if isinstance(_media_name_language, Unset):
            media_name_language = UNSET
        else:
            media_name_language = UserPreferencesMediaNameLanguage(_media_name_language)

        _search_history = d.pop("searchHistory", UNSET)
        search_history: UserPreferencesSearchHistory | Unset
        if isinstance(_search_history, Unset):
            search_history = UNSET
        else:
            search_history = UserPreferencesSearchHistory.from_dict(_search_history)

        user_preferences = cls(
            labs=labs,
            media_name_language=media_name_language,
            search_history=search_history,
        )

        user_preferences.additional_properties = d
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
