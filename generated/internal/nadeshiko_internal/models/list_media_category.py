from typing import Literal

ListMediaCategory = Literal["ANIME", "JDRAMA", "YOUTUBE"]

LIST_MEDIA_CATEGORY_VALUES: set[ListMediaCategory] = {
    "ANIME",
    "JDRAMA",
    "YOUTUBE",
}


def check_list_media_category(value: str) -> ListMediaCategory:
    if value in LIST_MEDIA_CATEGORY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_MEDIA_CATEGORY_VALUES!r}")
