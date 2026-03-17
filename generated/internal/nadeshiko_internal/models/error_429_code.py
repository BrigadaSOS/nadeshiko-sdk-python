from enum import Enum


class Error429Code(str, Enum):
    QUOTA_EXCEEDED = "QUOTA_EXCEEDED"
    RATE_LIMIT_EXCEEDED = "RATE_LIMIT_EXCEEDED"

    def __str__(self) -> str:
        return str(self.value)
