from enum import Enum


class UserPreferencesContentRatingPreferencesSuggestive(str, Enum):
    BLUR = "blur"
    HIDE = "hide"
    SHOW = "show"

    def __str__(self) -> str:
        return str(self.value)
