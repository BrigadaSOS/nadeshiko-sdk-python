from typing import Literal

MediaUpdateRequestSeasonName = Literal["FALL", "NONE", "SPRING", "SUMMER", "WINTER"]

MEDIA_UPDATE_REQUEST_SEASON_NAME_VALUES: set[MediaUpdateRequestSeasonName] = {
    "FALL",
    "NONE",
    "SPRING",
    "SUMMER",
    "WINTER",
}


def check_media_update_request_season_name(value: str) -> MediaUpdateRequestSeasonName:
    if value in MEDIA_UPDATE_REQUEST_SEASON_NAME_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEDIA_UPDATE_REQUEST_SEASON_NAME_VALUES!r}"
    )
