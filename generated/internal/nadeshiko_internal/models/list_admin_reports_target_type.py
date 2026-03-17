from enum import Enum


class ListAdminReportsTargetType(str, Enum):
    EPISODE = "EPISODE"
    MEDIA = "MEDIA"
    SEGMENT = "SEGMENT"

    def __str__(self) -> str:
        return str(self.value)
