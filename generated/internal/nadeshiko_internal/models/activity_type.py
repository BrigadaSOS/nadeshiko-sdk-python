from typing import Literal, cast

ActivityType = Literal["ANKI_EXPORT", "SEARCH", "SEGMENT_PLAY", "SHARE"]

ACTIVITY_TYPE_VALUES: set[ActivityType] = {
    "ANKI_EXPORT",
    "SEARCH",
    "SEGMENT_PLAY",
    "SHARE",
}


def check_activity_type(value: str) -> ActivityType:
    if value in ACTIVITY_TYPE_VALUES:
        return cast(ActivityType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTIVITY_TYPE_VALUES!r}")
