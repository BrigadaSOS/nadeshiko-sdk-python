from enum import Enum


class SegmentStatus(str, Enum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"
    HIDDEN = "HIDDEN"

    def __str__(self) -> str:
        return str(self.value)
