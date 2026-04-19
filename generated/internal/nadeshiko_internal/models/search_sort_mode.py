from typing import Literal, cast

SearchSortMode = Literal["ASC", "DESC", "RANDOM", "RELEVANCE", "TIME_ASC", "TIME_DESC"]

SEARCH_SORT_MODE_VALUES: set[SearchSortMode] = {
    "ASC",
    "DESC",
    "RANDOM",
    "RELEVANCE",
    "TIME_ASC",
    "TIME_DESC",
}


def check_search_sort_mode(value: str) -> SearchSortMode:
    if value in SEARCH_SORT_MODE_VALUES:
        return cast(SearchSortMode, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SEARCH_SORT_MODE_VALUES!r}")
