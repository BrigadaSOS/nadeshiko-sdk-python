from typing import Literal

ReportTargetSegmentType = Literal["SEGMENT"]

REPORT_TARGET_SEGMENT_TYPE_VALUES: set[ReportTargetSegmentType] = {
    "SEGMENT",
}


def check_report_target_segment_type(value: str) -> ReportTargetSegmentType:
    if value in REPORT_TARGET_SEGMENT_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_TARGET_SEGMENT_TYPE_VALUES!r}"
    )
