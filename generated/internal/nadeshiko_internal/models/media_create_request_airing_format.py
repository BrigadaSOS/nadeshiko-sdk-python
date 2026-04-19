from typing import Literal, cast

MediaCreateRequestAiringFormat = Literal["MOVIE", "ONA", "OVA", "SPECIAL", "TV"]

MEDIA_CREATE_REQUEST_AIRING_FORMAT_VALUES: set[MediaCreateRequestAiringFormat] = {
    "MOVIE",
    "ONA",
    "OVA",
    "SPECIAL",
    "TV",
}


def check_media_create_request_airing_format(value: str) -> MediaCreateRequestAiringFormat:
    if value in MEDIA_CREATE_REQUEST_AIRING_FORMAT_VALUES:
        return cast(MediaCreateRequestAiringFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEDIA_CREATE_REQUEST_AIRING_FORMAT_VALUES!r}"
    )
