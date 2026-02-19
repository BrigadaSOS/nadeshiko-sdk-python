from enum import Enum


class AdminHealthShowResponse200Status(str, Enum):
    DEGRADED = "degraded"
    HEALTHY = "healthy"

    def __str__(self) -> str:
        return str(self.value)
