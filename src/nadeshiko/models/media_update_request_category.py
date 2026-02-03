from enum import Enum


class MediaUpdateRequestCategory(str, Enum):
    ANIME = "ANIME"
    AUDIOBOOK = "AUDIOBOOK"

    def __str__(self) -> str:
        return str(self.value)
