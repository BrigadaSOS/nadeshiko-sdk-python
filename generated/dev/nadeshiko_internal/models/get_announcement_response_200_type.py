from enum import Enum


class GetAnnouncementResponse200Type(str, Enum):
    INFO = "info"
    MAINTENANCE = "maintenance"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
