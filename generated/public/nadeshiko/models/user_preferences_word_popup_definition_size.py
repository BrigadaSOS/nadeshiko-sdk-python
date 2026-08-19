from typing import Literal

UserPreferencesWordPopupDefinitionSize = Literal["LARGE", "MEDIUM", "SMALL"]

USER_PREFERENCES_WORD_POPUP_DEFINITION_SIZE_VALUES: set[UserPreferencesWordPopupDefinitionSize] = {
    "LARGE",
    "MEDIUM",
    "SMALL",
}


def check_user_preferences_word_popup_definition_size(
    value: str,
) -> UserPreferencesWordPopupDefinitionSize:
    if value in USER_PREFERENCES_WORD_POPUP_DEFINITION_SIZE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {USER_PREFERENCES_WORD_POPUP_DEFINITION_SIZE_VALUES!r}"
    )
