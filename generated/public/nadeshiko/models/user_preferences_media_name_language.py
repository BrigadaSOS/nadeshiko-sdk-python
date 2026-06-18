from typing import Literal

UserPreferencesMediaNameLanguage = Literal["ENGLISH", "JAPANESE", "ROMAJI"]

USER_PREFERENCES_MEDIA_NAME_LANGUAGE_VALUES: set[UserPreferencesMediaNameLanguage] = {
    "ENGLISH",
    "JAPANESE",
    "ROMAJI",
}


def check_user_preferences_media_name_language(value: str) -> UserPreferencesMediaNameLanguage:
    if value in USER_PREFERENCES_MEDIA_NAME_LANGUAGE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {USER_PREFERENCES_MEDIA_NAME_LANGUAGE_VALUES!r}"
    )
