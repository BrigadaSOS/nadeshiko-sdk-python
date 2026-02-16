from enum import Enum


class ListType(str, Enum):
    CUSTOM = "CUSTOM"
    SEGMENT = "SEGMENT"
    SERIES = "SERIES"

    def __str__(self) -> str:
        return str(self.value)
