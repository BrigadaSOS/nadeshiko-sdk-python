from enum import Enum


class ReportTargetSegmentType(str, Enum):
    SEGMENT = "SEGMENT"

    def __str__(self) -> str:
        return str(self.value)
