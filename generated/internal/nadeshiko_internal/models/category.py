from enum import Enum


class Category(str, Enum):
    ANIME = "ANIME"
    JDRAMA = "JDRAMA"

    def __str__(self) -> str:
        return str(self.value)
