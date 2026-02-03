from enum import Enum


class SearchRequestContentSort(str, Enum):
    ASC = "asc"
    DESC = "desc"
    NONE = "none"
    RANDOM = "random"
    TIME_ASC = "time_asc"
    TIME_DESC = "time_desc"

    def __str__(self) -> str:
        return str(self.value)
