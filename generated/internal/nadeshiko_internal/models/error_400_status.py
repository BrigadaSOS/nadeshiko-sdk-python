from enum import IntEnum


class Error400Status(IntEnum):
    VALUE_400 = 400

    def __str__(self) -> str:
        return str(self.value)
