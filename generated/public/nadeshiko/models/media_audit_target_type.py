from enum import Enum


class MediaAuditTargetType(str, Enum):
    EPISODE = "EPISODE"
    MEDIA = "MEDIA"

    def __str__(self) -> str:
        return str(self.value)
