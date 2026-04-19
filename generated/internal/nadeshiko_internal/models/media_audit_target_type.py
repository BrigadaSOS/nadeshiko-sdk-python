from typing import Literal, cast

MediaAuditTargetType = Literal["EPISODE", "MEDIA"]

MEDIA_AUDIT_TARGET_TYPE_VALUES: set[MediaAuditTargetType] = {
    "EPISODE",
    "MEDIA",
}


def check_media_audit_target_type(value: str) -> MediaAuditTargetType:
    if value in MEDIA_AUDIT_TARGET_TYPE_VALUES:
        return cast(MediaAuditTargetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEDIA_AUDIT_TARGET_TYPE_VALUES!r}"
    )
