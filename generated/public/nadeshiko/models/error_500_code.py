from enum import Enum


class Error500Code(str, Enum):
    INTERNAL_SERVER_EXCEPTION = "INTERNAL_SERVER_EXCEPTION"

    def __str__(self) -> str:
        return str(self.value)
