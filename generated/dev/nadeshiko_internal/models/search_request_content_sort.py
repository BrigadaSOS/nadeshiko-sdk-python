from enum import Enum


class SearchRequestContentSort(str, Enum):
    ASC = "ASC"
    DESC = "DESC"
    NONE = "NONE"
    RANDOM = "RANDOM"
    TIME_ASC = "TIME_ASC"
    TIME_DESC = "TIME_DESC"

    def __str__(self) -> str:
        return str(self.value)
