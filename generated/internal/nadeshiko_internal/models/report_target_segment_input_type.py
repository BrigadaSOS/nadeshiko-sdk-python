from enum import Enum


class ReportTargetSegmentInputType(str, Enum):
    SEGMENT = "SEGMENT"

    def __str__(self) -> str:
        return str(self.value)
