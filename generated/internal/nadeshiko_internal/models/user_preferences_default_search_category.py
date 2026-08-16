from typing import Literal

UserPreferencesDefaultSearchCategory = Literal["ALL", "ANIME", "JDRAMA", "YOUTUBE"]

USER_PREFERENCES_DEFAULT_SEARCH_CATEGORY_VALUES: set[UserPreferencesDefaultSearchCategory] = {
    "ALL",
    "ANIME",
    "JDRAMA",
    "YOUTUBE",
}


def check_user_preferences_default_search_category(
    value: str,
) -> UserPreferencesDefaultSearchCategory:
    if value in USER_PREFERENCES_DEFAULT_SEARCH_CATEGORY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {USER_PREFERENCES_DEFAULT_SEARCH_CATEGORY_VALUES!r}"
    )
