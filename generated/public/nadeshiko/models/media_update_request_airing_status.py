from enum import Enum


class MediaUpdateRequestAiringStatus(str, Enum):
    CANCELLED = "CANCELLED"
    FINISHED = "FINISHED"
    NOT_YET_RELEASED = "NOT_YET_RELEASED"
    RELEASING = "RELEASING"

    def __str__(self) -> str:
        return str(self.value)
