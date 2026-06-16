from typing import Literal

MediaCreateRequestAiringFormat = Literal["MOVIE", "ONA", "OVA", "SPECIAL", "TV", "YOUTUBE"]

MEDIA_CREATE_REQUEST_AIRING_FORMAT_VALUES: set[MediaCreateRequestAiringFormat] = {
    "MOVIE",
    "ONA",
    "OVA",
    "SPECIAL",
    "TV",
    "YOUTUBE",
}


def check_media_create_request_airing_format(value: str) -> MediaCreateRequestAiringFormat:
    if value in MEDIA_CREATE_REQUEST_AIRING_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEDIA_CREATE_REQUEST_AIRING_FORMAT_VALUES!r}"
    )
