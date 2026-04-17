from enum import Enum


class MediaUpdateRequestAiringFormat(str, Enum):
    MOVIE = "MOVIE"
    ONA = "ONA"
    OVA = "OVA"
    SPECIAL = "SPECIAL"
    TV = "TV"

    def __str__(self) -> str:
        return str(self.value)
