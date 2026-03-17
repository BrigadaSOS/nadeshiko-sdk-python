from enum import Enum


class GetAdminDashboardResponse200SystemElasticsearchStatus(str, Enum):
    CONNECTED = "connected"
    DISCONNECTED = "disconnected"

    def __str__(self) -> str:
        return str(self.value)
