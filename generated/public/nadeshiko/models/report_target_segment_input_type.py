from typing import Literal

ReportTargetSegmentInputType = Literal["SEGMENT"]

REPORT_TARGET_SEGMENT_INPUT_TYPE_VALUES: set[ReportTargetSegmentInputType] = {
    "SEGMENT",
}


def check_report_target_segment_input_type(value: str) -> ReportTargetSegmentInputType:
    if value in REPORT_TARGET_SEGMENT_INPUT_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_TARGET_SEGMENT_INPUT_TYPE_VALUES!r}"
    )
