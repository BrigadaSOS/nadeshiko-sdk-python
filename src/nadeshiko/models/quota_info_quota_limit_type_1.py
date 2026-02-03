from enum import Enum


class QuotaInfoQuotaLimitType1(str, Enum):
    NO_LIMIT = "NO_LIMIT"

    def __str__(self) -> str:
        return str(self.value)
