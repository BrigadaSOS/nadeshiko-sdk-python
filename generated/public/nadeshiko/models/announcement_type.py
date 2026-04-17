from enum import Enum


class AnnouncementType(str, Enum):
    INFO = "INFO"
    MAINTENANCE = "MAINTENANCE"
    WARNING = "WARNING"

    def __str__(self) -> str:
        return str(self.value)
