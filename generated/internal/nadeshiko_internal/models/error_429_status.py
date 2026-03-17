from enum import IntEnum


class Error429Status(IntEnum):
    VALUE_429 = 429

    def __str__(self) -> str:
        return str(self.value)
