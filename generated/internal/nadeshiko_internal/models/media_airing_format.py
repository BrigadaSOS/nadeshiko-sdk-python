from typing import Literal, cast

MediaAiringFormat = Literal["MOVIE", "ONA", "OVA", "SPECIAL", "TV"]

MEDIA_AIRING_FORMAT_VALUES: set[MediaAiringFormat] = {
    "MOVIE",
    "ONA",
    "OVA",
    "SPECIAL",
    "TV",
}


def check_media_airing_format(value: str) -> MediaAiringFormat:
    if value in MEDIA_AIRING_FORMAT_VALUES:
        return cast(MediaAiringFormat, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MEDIA_AIRING_FORMAT_VALUES!r}")
