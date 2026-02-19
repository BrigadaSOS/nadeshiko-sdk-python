from enum import Enum


class SeiyuuShowIncludeItem(str, Enum):
    CHARACTER = "character"

    def __str__(self) -> str:
        return str(self.value)
