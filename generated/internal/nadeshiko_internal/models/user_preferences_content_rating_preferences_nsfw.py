from typing import Literal

UserPreferencesContentRatingPreferencesNsfw = Literal["BLUR", "HIDE", "SHOW"]

USER_PREFERENCES_CONTENT_RATING_PREFERENCES_NSFW_VALUES: set[
    UserPreferencesContentRatingPreferencesNsfw
] = {
    "BLUR",
    "HIDE",
    "SHOW",
}


def check_user_preferences_content_rating_preferences_nsfw(
    value: str,
) -> UserPreferencesContentRatingPreferencesNsfw:
    if value in USER_PREFERENCES_CONTENT_RATING_PREFERENCES_NSFW_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {USER_PREFERENCES_CONTENT_RATING_PREFERENCES_NSFW_VALUES!r}"
    )
