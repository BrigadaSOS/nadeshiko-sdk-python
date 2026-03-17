from enum import Enum


class GetAdminHealthResponse200ElasticsearchStatus(str, Enum):
    CONNECTED = "connected"
    DISCONNECTED = "disconnected"

    def __str__(self) -> str:
        return str(self.value)
