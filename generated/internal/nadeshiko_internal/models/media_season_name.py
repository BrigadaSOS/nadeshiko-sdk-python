from typing import Literal, cast

MediaSeasonName = Literal["FALL", "SPRING", "SUMMER", "WINTER"]

MEDIA_SEASON_NAME_VALUES: set[MediaSeasonName] = {
    "FALL",
    "SPRING",
    "SUMMER",
    "WINTER",
}


def check_media_season_name(value: str) -> MediaSeasonName:
    if value in MEDIA_SEASON_NAME_VALUES:
        return cast(MediaSeasonName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MEDIA_SEASON_NAME_VALUES!r}")
