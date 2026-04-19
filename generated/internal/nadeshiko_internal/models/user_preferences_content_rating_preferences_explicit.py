from typing import Literal, cast

UserPreferencesContentRatingPreferencesExplicit = Literal["BLUR", "HIDE", "SHOW"]

USER_PREFERENCES_CONTENT_RATING_PREFERENCES_EXPLICIT_VALUES: set[
    UserPreferencesContentRatingPreferencesExplicit
] = {
    "BLUR",
    "HIDE",
    "SHOW",
}


def check_user_preferences_content_rating_preferences_explicit(
    value: str,
) -> UserPreferencesContentRatingPreferencesExplicit:
    if value in USER_PREFERENCES_CONTENT_RATING_PREFERENCES_EXPLICIT_VALUES:
        return cast(UserPreferencesContentRatingPreferencesExplicit, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {USER_PREFERENCES_CONTENT_RATING_PREFERENCES_EXPLICIT_VALUES!r}"
    )
