from enum import Enum


class UserPreferencesMediaNameLanguage(str, Enum):
    ENGLISH = "ENGLISH"
    JAPANESE = "JAPANESE"
    ROMAJI = "ROMAJI"

    def __str__(self) -> str:
        return str(self.value)
