from enum import Enum


class ReportTargetMediaType(str, Enum):
    MEDIA = "MEDIA"

    def __str__(self) -> str:
        return str(self.value)
