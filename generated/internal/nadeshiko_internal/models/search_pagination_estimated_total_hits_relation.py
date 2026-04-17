from enum import Enum


class SearchPaginationEstimatedTotalHitsRelation(str, Enum):
    AT_LEAST = "AT_LEAST"
    EXACT = "EXACT"

    def __str__(self) -> str:
        return str(self.value)
