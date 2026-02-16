from enum import Enum


class UserPreferencesMediaNameLanguage(str, Enum):
    ENGLISH = "english"
    JAPANESE = "japanese"
    ROMAJI = "romaji"

    def __str__(self) -> str:
        return str(self.value)
