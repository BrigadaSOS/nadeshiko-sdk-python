from enum import Enum


class SearchStatsRequestStatusItem(str, Enum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"
    INVALID = "INVALID"
    SUSPENDED = "SUSPENDED"
    TOO_LONG = "TOO_LONG"
    VERIFIED = "VERIFIED"

    def __str__(self) -> str:
        return str(self.value)
