from typing import Literal, cast

SegmentStatus = Literal["ACTIVE", "DELETED", "HIDDEN"]

SEGMENT_STATUS_VALUES: set[SegmentStatus] = {
    "ACTIVE",
    "DELETED",
    "HIDDEN",
}


def check_segment_status(value: str) -> SegmentStatus:
    if value in SEGMENT_STATUS_VALUES:
        return cast(SegmentStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SEGMENT_STATUS_VALUES!r}")
