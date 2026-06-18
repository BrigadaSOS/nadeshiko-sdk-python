from typing import Literal

SearchFiltersLanguagesType0Item = Literal["EN", "ES"]

SEARCH_FILTERS_LANGUAGES_TYPE_0_ITEM_VALUES: set[SearchFiltersLanguagesType0Item] = {
    "EN",
    "ES",
}


def check_search_filters_languages_type_0_item(value: str) -> SearchFiltersLanguagesType0Item:
    if value in SEARCH_FILTERS_LANGUAGES_TYPE_0_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SEARCH_FILTERS_LANGUAGES_TYPE_0_ITEM_VALUES!r}"
    )
