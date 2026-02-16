from enum import Enum


class ReviewCheckThresholdSchemaItemType(str, Enum):
    BOOLEAN = "boolean"
    NUMBER = "number"

    def __str__(self) -> str:
        return str(self.value)
