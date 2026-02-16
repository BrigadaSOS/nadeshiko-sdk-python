from enum import Enum


class SegmentStorage(str, Enum):
    LOCAL = "LOCAL"
    R2 = "R2"

    def __str__(self) -> str:
        return str(self.value)
