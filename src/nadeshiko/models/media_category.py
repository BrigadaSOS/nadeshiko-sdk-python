from enum import Enum


class MediaCategory(str, Enum):
    ANIME = "ANIME"
    AUDIOBOOK = "AUDIOBOOK"
    BOOK = "BOOK"
    JDRAMA = "JDRAMA"

    def __str__(self) -> str:
        return str(self.value)
