from typing import Literal

GetCoveredWordsFilter = Literal["ALL", "COVERED", "UNCOVERED"]

GET_COVERED_WORDS_FILTER_VALUES: set[GetCoveredWordsFilter] = {
    "ALL",
    "COVERED",
    "UNCOVERED",
}


def check_get_covered_words_filter(value: str) -> GetCoveredWordsFilter:
    if value in GET_COVERED_WORDS_FILTER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_COVERED_WORDS_FILTER_VALUES!r}"
    )
