from enum import Enum

class MediaCreateRequestStorage(str, Enum):
    LOCAL = "local"
    R2 = "r2"

    def __str__(self) -> str:
        return str(self.value)
