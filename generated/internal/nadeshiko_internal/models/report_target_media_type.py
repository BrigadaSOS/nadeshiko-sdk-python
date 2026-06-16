from typing import Literal

ReportTargetMediaType = Literal["MEDIA"]

REPORT_TARGET_MEDIA_TYPE_VALUES: set[ReportTargetMediaType] = {
    "MEDIA",
}


def check_report_target_media_type(value: str) -> ReportTargetMediaType:
    if value in REPORT_TARGET_MEDIA_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_TARGET_MEDIA_TYPE_VALUES!r}"
    )
