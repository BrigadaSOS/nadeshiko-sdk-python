from enum import Enum


class ReviewCheckTargetType(str, Enum):
    EPISODE = "EPISODE"
    MEDIA = "MEDIA"

    def __str__(self) -> str:
        return str(self.value)
