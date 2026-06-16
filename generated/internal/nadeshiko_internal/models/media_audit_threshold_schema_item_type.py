from typing import Literal

MediaAuditThresholdSchemaItemType = Literal["boolean", "number"]

MEDIA_AUDIT_THRESHOLD_SCHEMA_ITEM_TYPE_VALUES: set[MediaAuditThresholdSchemaItemType] = {
    "boolean",
    "number",
}


def check_media_audit_threshold_schema_item_type(value: str) -> MediaAuditThresholdSchemaItemType:
    if value in MEDIA_AUDIT_THRESHOLD_SCHEMA_ITEM_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEDIA_AUDIT_THRESHOLD_SCHEMA_ITEM_TYPE_VALUES!r}"
    )
