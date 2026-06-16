from typing import Literal

MediaCreateRequestStorage = Literal["LOCAL", "R2"]

MEDIA_CREATE_REQUEST_STORAGE_VALUES: set[MediaCreateRequestStorage] = {
    "LOCAL",
    "R2",
}


def check_media_create_request_storage(value: str) -> MediaCreateRequestStorage:
    if value in MEDIA_CREATE_REQUEST_STORAGE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEDIA_CREATE_REQUEST_STORAGE_VALUES!r}"
    )
