from enum import Enum


class MediaCreateRequestCategory(str, Enum):
    ANIME = "ANIME"
    AUDIOBOOK = "AUDIOBOOK"
    BOOK = "BOOK"
    JDRAMA = "JDRAMA"

    def __str__(self) -> str:
        return str(self.value)
