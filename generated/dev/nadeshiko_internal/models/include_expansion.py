from enum import Enum


class IncludeExpansion(str, Enum):
    MEDIA = "media"

    def __str__(self) -> str:
        return str(self.value)
