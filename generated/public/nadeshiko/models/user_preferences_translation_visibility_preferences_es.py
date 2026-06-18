from typing import Literal

UserPreferencesTranslationVisibilityPreferencesES = Literal["hidden", "show", "spoiler"]

USER_PREFERENCES_TRANSLATION_VISIBILITY_PREFERENCES_ES_VALUES: set[
    UserPreferencesTranslationVisibilityPreferencesES
] = {
    "hidden",
    "show",
    "spoiler",
}


def check_user_preferences_translation_visibility_preferences_es(
    value: str,
) -> UserPreferencesTranslationVisibilityPreferencesES:
    if value in USER_PREFERENCES_TRANSLATION_VISIBILITY_PREFERENCES_ES_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {USER_PREFERENCES_TRANSLATION_VISIBILITY_PREFERENCES_ES_VALUES!r}"
    )
