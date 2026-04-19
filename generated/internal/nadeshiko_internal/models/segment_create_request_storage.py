from typing import Literal, cast

SegmentCreateRequestStorage = Literal["LOCAL", "R2"]

SEGMENT_CREATE_REQUEST_STORAGE_VALUES: set[SegmentCreateRequestStorage] = {
    "LOCAL",
    "R2",
}


def check_segment_create_request_storage(value: str) -> SegmentCreateRequestStorage:
    if value in SEGMENT_CREATE_REQUEST_STORAGE_VALUES:
        return cast(SegmentCreateRequestStorage, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SEGMENT_CREATE_REQUEST_STORAGE_VALUES!r}"
    )
