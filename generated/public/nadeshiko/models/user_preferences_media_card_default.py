from typing import Literal

UserPreferencesMediaCardDefault = Literal["CLOSED", "OPEN"]

USER_PREFERENCES_MEDIA_CARD_DEFAULT_VALUES: set[UserPreferencesMediaCardDefault] = {
    "CLOSED",
    "OPEN",
}


def check_user_preferences_media_card_default(value: str) -> UserPreferencesMediaCardDefault:
    if value in USER_PREFERENCES_MEDIA_CARD_DEFAULT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {USER_PREFERENCES_MEDIA_CARD_DEFAULT_VALUES!r}"
    )
