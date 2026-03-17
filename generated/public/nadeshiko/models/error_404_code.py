from enum import Enum


class Error404Code(str, Enum):
    NOT_FOUND = "NOT_FOUND"

    def __str__(self) -> str:
        return str(self.value)
