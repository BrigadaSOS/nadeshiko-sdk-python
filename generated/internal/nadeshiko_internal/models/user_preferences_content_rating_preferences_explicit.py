from enum import Enum


class UserPreferencesContentRatingPreferencesExplicit(str, Enum):
    BLUR = "BLUR"
    HIDE = "HIDE"
    SHOW = "SHOW"

    def __str__(self) -> str:
        return str(self.value)
