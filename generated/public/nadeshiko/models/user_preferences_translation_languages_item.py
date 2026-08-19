from typing import Literal

UserPreferencesTranslationLanguagesItem = Literal["EN", "ES"]

USER_PREFERENCES_TRANSLATION_LANGUAGES_ITEM_VALUES: set[UserPreferencesTranslationLanguagesItem] = {
    "EN",
    "ES",
}


def check_user_preferences_translation_languages_item(
    value: str,
) -> UserPreferencesTranslationLanguagesItem:
    if value in USER_PREFERENCES_TRANSLATION_LANGUAGES_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {USER_PREFERENCES_TRANSLATION_LANGUAGES_ITEM_VALUES!r}"
    )
