from enum import Enum


class ReportTargetType(str, Enum):
    EPISODE = "EPISODE"
    MEDIA = "MEDIA"
    SEGMENT = "SEGMENT"

    def __str__(self) -> str:
        return str(self.value)
