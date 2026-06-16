from typing import Literal

SegmentUpdateRequestStorage = Literal["LOCAL", "R2"]

SEGMENT_UPDATE_REQUEST_STORAGE_VALUES: set[SegmentUpdateRequestStorage] = {
    "LOCAL",
    "R2",
}


def check_segment_update_request_storage(value: str) -> SegmentUpdateRequestStorage:
    if value in SEGMENT_UPDATE_REQUEST_STORAGE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SEGMENT_UPDATE_REQUEST_STORAGE_VALUES!r}"
    )
