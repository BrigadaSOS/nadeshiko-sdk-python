from enum import IntEnum


class Error500Status(IntEnum):
    VALUE_500 = 500

    def __str__(self) -> str:
        return str(self.value)
