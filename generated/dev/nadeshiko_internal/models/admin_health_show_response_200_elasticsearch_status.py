from enum import Enum


class AdminHealthShowResponse200ElasticsearchStatus(str, Enum):
    CONNECTED = "connected"
    DISCONNECTED = "disconnected"

    def __str__(self) -> str:
        return str(self.value)
