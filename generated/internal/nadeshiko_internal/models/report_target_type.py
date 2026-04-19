from typing import Literal, cast

ReportTargetType = Literal["EPISODE", "MEDIA", "SEGMENT"]

REPORT_TARGET_TYPE_VALUES: set[ReportTargetType] = {
    "EPISODE",
    "MEDIA",
    "SEGMENT",
}


def check_report_target_type(value: str) -> ReportTargetType:
    if value in REPORT_TARGET_TYPE_VALUES:
        return cast(ReportTargetType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_TARGET_TYPE_VALUES!r}")
