from enum import Enum


class UserActivityRequestActivityType(str, Enum):
    ANKI_EXPORT = "ANKI_EXPORT"
    SEARCH = "SEARCH"
    SEGMENT_PLAY = "SEGMENT_PLAY"
    SHARE = "SHARE"

    def __str__(self) -> str:
        return str(self.value)
