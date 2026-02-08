from enum import Enum

class ListWithMediaType(str, Enum):
    CUSTOM = "CUSTOM"
    SERIES = "SERIES"

    def __str__(self) -> str:
        return str(self.value)
