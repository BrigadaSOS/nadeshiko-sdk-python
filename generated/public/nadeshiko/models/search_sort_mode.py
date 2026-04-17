from enum import Enum


class SearchSortMode(str, Enum):
    ASC = "ASC"
    DESC = "DESC"
    RANDOM = "RANDOM"
    RELEVANCE = "RELEVANCE"
    TIME_ASC = "TIME_ASC"
    TIME_DESC = "TIME_DESC"

    def __str__(self) -> str:
        return str(self.value)
