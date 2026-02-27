from enum import Enum


class ActivityType(str, Enum):
    ANKI_EXPORT = "ANKI_EXPORT"
    LIST_ADD_SEGMENT = "LIST_ADD_SEGMENT"
    SEARCH = "SEARCH"
    SEGMENT_PLAY = "SEGMENT_PLAY"
    SHARE = "SHARE"

    def __str__(self) -> str:
        return str(self.value)
