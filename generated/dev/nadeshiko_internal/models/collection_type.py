from enum import Enum


class CollectionType(str, Enum):
    ANKI_EXPORT = "ANKI_EXPORT"
    USER = "USER"

    def __str__(self) -> str:
        return str(self.value)
