from typing import Literal, cast

Category = Literal["ANIME", "JDRAMA"]

CATEGORY_VALUES: set[Category] = {
    "ANIME",
    "JDRAMA",
}


def check_category(value: str) -> Category:
    if value in CATEGORY_VALUES:
        return cast(Category, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATEGORY_VALUES!r}")
