from enum import Enum


class ListCreateRequestType(str, Enum):
    CUSTOM = "CUSTOM"
    SEGMENT = "SEGMENT"
    SERIES = "SERIES"

    def __str__(self) -> str:
        return str(self.value)
