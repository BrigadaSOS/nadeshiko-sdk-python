from enum import Enum


class PaginationInfoEstimatedTotalHitsRelation(str, Enum):
    EXACT = "EXACT"
    LOWER_BOUND = "LOWER_BOUND"

    def __str__(self) -> str:
        return str(self.value)
