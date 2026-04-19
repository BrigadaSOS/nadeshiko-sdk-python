from typing import Literal, cast

ListMediaCategory = Literal["ANIME", "JDRAMA"]

LIST_MEDIA_CATEGORY_VALUES: set[ListMediaCategory] = {
    "ANIME",
    "JDRAMA",
}


def check_list_media_category(value: str) -> ListMediaCategory:
    if value in LIST_MEDIA_CATEGORY_VALUES:
        return cast(ListMediaCategory, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_MEDIA_CATEGORY_VALUES!r}")
