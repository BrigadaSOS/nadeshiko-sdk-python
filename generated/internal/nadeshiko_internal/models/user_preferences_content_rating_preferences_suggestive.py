from enum import Enum


class UserPreferencesContentRatingPreferencesSuggestive(str, Enum):
    BLUR = "BLUR"
    HIDE = "HIDE"
    SHOW = "SHOW"

    def __str__(self) -> str:
        return str(self.value)
