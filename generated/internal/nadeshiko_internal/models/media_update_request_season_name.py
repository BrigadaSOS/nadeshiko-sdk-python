from typing import Literal, cast

MediaUpdateRequestSeasonName = Literal["FALL", "SPRING", "SUMMER", "WINTER"]

MEDIA_UPDATE_REQUEST_SEASON_NAME_VALUES: set[MediaUpdateRequestSeasonName] = {
    "FALL",
    "SPRING",
    "SUMMER",
    "WINTER",
}


def check_media_update_request_season_name(value: str) -> MediaUpdateRequestSeasonName:
    if value in MEDIA_UPDATE_REQUEST_SEASON_NAME_VALUES:
        return cast(MediaUpdateRequestSeasonName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEDIA_UPDATE_REQUEST_SEASON_NAME_VALUES!r}"
    )
