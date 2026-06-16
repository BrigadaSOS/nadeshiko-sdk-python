from typing import Literal

UserPreferencesTranslationVisibilityPreferencesEN = Literal["hidden", "show", "spoiler"]

USER_PREFERENCES_TRANSLATION_VISIBILITY_PREFERENCES_EN_VALUES: set[
    UserPreferencesTranslationVisibilityPreferencesEN
] = {
    "hidden",
    "show",
    "spoiler",
}


def check_user_preferences_translation_visibility_preferences_en(
    value: str,
) -> UserPreferencesTranslationVisibilityPreferencesEN:
    if value in USER_PREFERENCES_TRANSLATION_VISIBILITY_PREFERENCES_EN_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {USER_PREFERENCES_TRANSLATION_VISIBILITY_PREFERENCES_EN_VALUES!r}"
    )
