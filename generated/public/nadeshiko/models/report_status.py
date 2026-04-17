from enum import Enum


class ReportStatus(str, Enum):
    DISMISSED = "DISMISSED"
    FIXED = "FIXED"
    OPEN = "OPEN"
    PROCESSING = "PROCESSING"

    def __str__(self) -> str:
        return str(self.value)
