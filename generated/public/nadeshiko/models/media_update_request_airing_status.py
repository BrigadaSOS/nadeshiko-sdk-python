from typing import Literal

MediaUpdateRequestAiringStatus = Literal["CANCELLED", "FINISHED", "NOT_YET_RELEASED", "RELEASING"]

MEDIA_UPDATE_REQUEST_AIRING_STATUS_VALUES: set[MediaUpdateRequestAiringStatus] = {
    "CANCELLED",
    "FINISHED",
    "NOT_YET_RELEASED",
    "RELEASING",
}


def check_media_update_request_airing_status(value: str) -> MediaUpdateRequestAiringStatus:
    if value in MEDIA_UPDATE_REQUEST_AIRING_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEDIA_UPDATE_REQUEST_AIRING_STATUS_VALUES!r}"
    )
