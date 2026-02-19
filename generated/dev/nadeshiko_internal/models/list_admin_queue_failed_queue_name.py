from enum import Enum


class ListAdminQueueFailedQueueName(str, Enum):
    ES_SYNC_CREATE = "es-sync-create"
    ES_SYNC_DELETE = "es-sync-delete"
    ES_SYNC_UPDATE = "es-sync-update"

    def __str__(self) -> str:
        return str(self.value)
