from enum import Enum


class AdminDashboardShowResponse200SystemStatus(str, Enum):
    DEGRADED = "degraded"
    HEALTHY = "healthy"

    def __str__(self) -> str:
        return str(self.value)
