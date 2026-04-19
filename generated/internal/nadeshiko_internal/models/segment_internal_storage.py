from typing import Literal, cast

SegmentInternalStorage = Literal["LOCAL", "R2"]

SEGMENT_INTERNAL_STORAGE_VALUES: set[SegmentInternalStorage] = {
    "LOCAL",
    "R2",
}


def check_segment_internal_storage(value: str) -> SegmentInternalStorage:
    if value in SEGMENT_INTERNAL_STORAGE_VALUES:
        return cast(SegmentInternalStorage, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SEGMENT_INTERNAL_STORAGE_VALUES!r}"
    )
