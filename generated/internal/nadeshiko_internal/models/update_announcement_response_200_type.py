from enum import Enum


class UpdateAnnouncementResponse200Type(str, Enum):
    INFO = "info"
    MAINTENANCE = "maintenance"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
