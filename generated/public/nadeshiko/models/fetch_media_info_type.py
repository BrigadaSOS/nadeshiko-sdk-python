from enum import Enum

class FetchMediaInfoType(str, Enum):
    ANIME = "anime"
    AUDIOBOOK = "audiobook"
    LIVEACTION = "liveaction"

    def __str__(self) -> str:
        return str(self.value)
