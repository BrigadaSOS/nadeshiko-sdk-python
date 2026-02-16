from enum import Enum


class CreateReportRequestTargetType(str, Enum):
    MEDIA = "MEDIA"
    SEGMENT = "SEGMENT"

    def __str__(self) -> str:
        return str(self.value)
