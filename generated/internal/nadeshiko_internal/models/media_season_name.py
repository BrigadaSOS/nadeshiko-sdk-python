from typing import Literal

MediaSeasonName = Literal["FALL", "NONE", "SPRING", "SUMMER", "WINTER"]

MEDIA_SEASON_NAME_VALUES: set[MediaSeasonName] = {
    "FALL",
    "NONE",
    "SPRING",
    "SUMMER",
    "WINTER",
}


def check_media_season_name(value: str) -> MediaSeasonName:
    if value in MEDIA_SEASON_NAME_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MEDIA_SEASON_NAME_VALUES!r}")
