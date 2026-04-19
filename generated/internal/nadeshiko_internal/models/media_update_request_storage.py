from typing import Literal, cast

MediaUpdateRequestStorage = Literal["LOCAL", "R2"]

MEDIA_UPDATE_REQUEST_STORAGE_VALUES: set[MediaUpdateRequestStorage] = {
    "LOCAL",
    "R2",
}


def check_media_update_request_storage(value: str) -> MediaUpdateRequestStorage:
    if value in MEDIA_UPDATE_REQUEST_STORAGE_VALUES:
        return cast(MediaUpdateRequestStorage, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEDIA_UPDATE_REQUEST_STORAGE_VALUES!r}"
    )
