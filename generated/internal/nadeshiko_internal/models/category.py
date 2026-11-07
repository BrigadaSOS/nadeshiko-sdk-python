from typing import Literal

Category = Literal["ANIME", "AUDIOBOOK", "JDRAMA", "YOUTUBE"]

CATEGORY_VALUES: set[Category] = {
    "ANIME",
    "AUDIOBOOK",
    "JDRAMA",
    "YOUTUBE",
}


def check_category(value: str) -> Category:
    if value in CATEGORY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATEGORY_VALUES!r}")
