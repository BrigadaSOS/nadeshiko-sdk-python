from enum import Enum


class Error409Code(str, Enum):
    ACCOUNT_CONFLICT = "ACCOUNT_CONFLICT"
    DUPLICATE_KEY = "DUPLICATE_KEY"

    def __str__(self) -> str:
        return str(self.value)
