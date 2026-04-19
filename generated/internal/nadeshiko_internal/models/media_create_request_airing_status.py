from typing import Literal, cast

MediaCreateRequestAiringStatus = Literal["CANCELLED", "FINISHED", "NOT_YET_RELEASED", "RELEASING"]

MEDIA_CREATE_REQUEST_AIRING_STATUS_VALUES: set[MediaCreateRequestAiringStatus] = {
    "CANCELLED",
    "FINISHED",
    "NOT_YET_RELEASED",
    "RELEASING",
}


def check_media_create_request_airing_status(value: str) -> MediaCreateRequestAiringStatus:
    if value in MEDIA_CREATE_REQUEST_AIRING_STATUS_VALUES:
        return cast(MediaCreateRequestAiringStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEDIA_CREATE_REQUEST_AIRING_STATUS_VALUES!r}"
    )
