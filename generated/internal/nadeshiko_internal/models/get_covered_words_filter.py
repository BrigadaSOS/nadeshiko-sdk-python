from enum import Enum


class GetCoveredWordsFilter(str, Enum):
    ALL = "all"
    COVERED = "covered"
    UNCOVERED = "uncovered"

    def __str__(self) -> str:
        return str(self.value)
