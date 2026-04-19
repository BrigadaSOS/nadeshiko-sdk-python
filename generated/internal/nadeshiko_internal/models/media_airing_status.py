from typing import Literal, cast

MediaAiringStatus = Literal["CANCELLED", "FINISHED", "NOT_YET_RELEASED", "RELEASING"]

MEDIA_AIRING_STATUS_VALUES: set[MediaAiringStatus] = {
    "CANCELLED",
    "FINISHED",
    "NOT_YET_RELEASED",
    "RELEASING",
}


def check_media_airing_status(value: str) -> MediaAiringStatus:
    if value in MEDIA_AIRING_STATUS_VALUES:
        return cast(MediaAiringStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MEDIA_AIRING_STATUS_VALUES!r}")
