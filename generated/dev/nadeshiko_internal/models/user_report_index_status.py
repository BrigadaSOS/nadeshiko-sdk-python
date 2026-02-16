from enum import Enum


class UserReportIndexStatus(str, Enum):
    ACCEPTED = "ACCEPTED"
    CONCERN = "CONCERN"
    IGNORED = "IGNORED"
    PENDING = "PENDING"
    REJECTED = "REJECTED"
    RESOLVED = "RESOLVED"

    def __str__(self) -> str:
        return str(self.value)
