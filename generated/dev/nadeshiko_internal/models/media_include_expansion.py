from enum import Enum


class MediaIncludeExpansion(str, Enum):
    MEDIA = "media"
    MEDIA_CHARACTERS = "media.characters"

    def __str__(self) -> str:
        return str(self.value)
