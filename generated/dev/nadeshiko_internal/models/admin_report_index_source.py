from enum import Enum


class AdminReportIndexSource(str, Enum):
    AUTO = "AUTO"
    USER = "USER"

    def __str__(self) -> str:
        return str(self.value)
