from enum import Enum


class GetCoveredWordsFilter(str, Enum):
    ALL = "ALL"
    COVERED = "COVERED"
    UNCOVERED = "UNCOVERED"

    def __str__(self) -> str:
        return str(self.value)
