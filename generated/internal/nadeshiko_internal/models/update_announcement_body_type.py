from enum import Enum


class UpdateAnnouncementBodyType(str, Enum):
    INFO = "info"
    MAINTENANCE = "maintenance"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
