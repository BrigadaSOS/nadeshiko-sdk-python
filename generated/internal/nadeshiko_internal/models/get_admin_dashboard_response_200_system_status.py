from enum import Enum


class GetAdminDashboardResponse200SystemStatus(str, Enum):
    DEGRADED = "degraded"
    HEALTHY = "healthy"

    def __str__(self) -> str:
        return str(self.value)
