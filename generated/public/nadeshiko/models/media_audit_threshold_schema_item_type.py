from enum import Enum


class MediaAuditThresholdSchemaItemType(str, Enum):
    BOOLEAN = "boolean"
    NUMBER = "number"

    def __str__(self) -> str:
        return str(self.value)
