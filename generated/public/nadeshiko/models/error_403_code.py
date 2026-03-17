from enum import Enum


class Error403Code(str, Enum):
    ACCESS_DENIED = "ACCESS_DENIED"
    INSUFFICIENT_PERMISSIONS = "INSUFFICIENT_PERMISSIONS"

    def __str__(self) -> str:
        return str(self.value)
