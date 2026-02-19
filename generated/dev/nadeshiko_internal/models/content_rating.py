from enum import Enum


class ContentRating(str, Enum):
    EXPLICIT = "EXPLICIT"
    QUESTIONABLE = "QUESTIONABLE"
    SAFE = "SAFE"
    SUGGESTIVE = "SUGGESTIVE"

    def __str__(self) -> str:
        return str(self.value)
