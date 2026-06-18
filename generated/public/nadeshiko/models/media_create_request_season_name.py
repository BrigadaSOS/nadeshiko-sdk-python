from typing import Literal

MediaCreateRequestSeasonName = Literal["FALL", "NONE", "SPRING", "SUMMER", "WINTER"]

MEDIA_CREATE_REQUEST_SEASON_NAME_VALUES: set[MediaCreateRequestSeasonName] = {
    "FALL",
    "NONE",
    "SPRING",
    "SUMMER",
    "WINTER",
}


def check_media_create_request_season_name(value: str) -> MediaCreateRequestSeasonName:
    if value in MEDIA_CREATE_REQUEST_SEASON_NAME_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEDIA_CREATE_REQUEST_SEASON_NAME_VALUES!r}"
    )
