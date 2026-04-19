from typing import Literal, cast

UserPreferencesContentRatingPreferencesSuggestive = Literal["BLUR", "HIDE", "SHOW"]

USER_PREFERENCES_CONTENT_RATING_PREFERENCES_SUGGESTIVE_VALUES: set[
    UserPreferencesContentRatingPreferencesSuggestive
] = {
    "BLUR",
    "HIDE",
    "SHOW",
}


def check_user_preferences_content_rating_preferences_suggestive(
    value: str,
) -> UserPreferencesContentRatingPreferencesSuggestive:
    if value in USER_PREFERENCES_CONTENT_RATING_PREFERENCES_SUGGESTIVE_VALUES:
        return cast(UserPreferencesContentRatingPreferencesSuggestive, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {USER_PREFERENCES_CONTENT_RATING_PREFERENCES_SUGGESTIVE_VALUES!r}"
    )
