from typing import Literal

MediaUpdateRequestAiringFormat = Literal["MOVIE", "ONA", "OVA", "SPECIAL", "TV", "YOUTUBE"]

MEDIA_UPDATE_REQUEST_AIRING_FORMAT_VALUES: set[MediaUpdateRequestAiringFormat] = {
    "MOVIE",
    "ONA",
    "OVA",
    "SPECIAL",
    "TV",
    "YOUTUBE",
}


def check_media_update_request_airing_format(value: str) -> MediaUpdateRequestAiringFormat:
    if value in MEDIA_UPDATE_REQUEST_AIRING_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEDIA_UPDATE_REQUEST_AIRING_FORMAT_VALUES!r}"
    )
