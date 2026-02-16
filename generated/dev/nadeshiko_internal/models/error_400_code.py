from enum import Enum


class Error400Code(str, Enum):
    INVALID_JSON = "INVALID_JSON"
    INVALID_REQUEST = "INVALID_REQUEST"
    VALIDATION_FAILED = "VALIDATION_FAILED"

    def __str__(self) -> str:
        return str(self.value)
