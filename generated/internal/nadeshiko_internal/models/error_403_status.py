from enum import IntEnum


class Error403Status(IntEnum):
    VALUE_403 = 403

    def __str__(self) -> str:
        return str(self.value)
