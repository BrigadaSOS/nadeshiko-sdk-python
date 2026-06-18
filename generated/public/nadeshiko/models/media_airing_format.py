from typing import Literal

MediaAiringFormat = Literal["MOVIE", "ONA", "OVA", "SPECIAL", "TV", "YOUTUBE"]

MEDIA_AIRING_FORMAT_VALUES: set[MediaAiringFormat] = {
    "MOVIE",
    "ONA",
    "OVA",
    "SPECIAL",
    "TV",
    "YOUTUBE",
}


def check_media_airing_format(value: str) -> MediaAiringFormat:
    if value in MEDIA_AIRING_FORMAT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MEDIA_AIRING_FORMAT_VALUES!r}")
