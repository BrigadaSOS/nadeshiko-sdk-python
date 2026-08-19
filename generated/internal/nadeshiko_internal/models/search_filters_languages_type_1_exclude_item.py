from typing import Literal

SearchFiltersLanguagesType1ExcludeItem = Literal["EN", "en", "es", "ES"]

SEARCH_FILTERS_LANGUAGES_TYPE_1_EXCLUDE_ITEM_VALUES: set[SearchFiltersLanguagesType1ExcludeItem] = {
    "EN",
    "en",
    "es",
    "ES",
}


def check_search_filters_languages_type_1_exclude_item(
    value: str,
) -> SearchFiltersLanguagesType1ExcludeItem:
    if value in SEARCH_FILTERS_LANGUAGES_TYPE_1_EXCLUDE_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SEARCH_FILTERS_LANGUAGES_TYPE_1_EXCLUDE_ITEM_VALUES!r}"
    )
