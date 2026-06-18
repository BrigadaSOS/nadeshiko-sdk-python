from typing import Literal

AnnouncementType = Literal["INFO", "MAINTENANCE", "WARNING"]

ANNOUNCEMENT_TYPE_VALUES: set[AnnouncementType] = {
    "INFO",
    "MAINTENANCE",
    "WARNING",
}


def check_announcement_type(value: str) -> AnnouncementType:
    if value in ANNOUNCEMENT_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ANNOUNCEMENT_TYPE_VALUES!r}")
