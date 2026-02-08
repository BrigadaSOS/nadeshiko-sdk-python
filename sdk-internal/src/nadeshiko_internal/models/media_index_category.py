from enum import Enum

class MediaIndexCategory(str, Enum):
    ANIME = "ANIME"
    JDRAMA = "JDRAMA"

    def __str__(self) -> str:
        return str(self.value)
