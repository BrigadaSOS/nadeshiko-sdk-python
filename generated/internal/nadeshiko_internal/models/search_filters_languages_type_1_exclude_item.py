from typing import Literal, cast

SearchFiltersLanguagesType1ExcludeItem = Literal["EN", "en", "ES", "es"]

SEARCH_FILTERS_LANGUAGES_TYPE_1_EXCLUDE_ITEM_VALUES: set[SearchFiltersLanguagesType1ExcludeItem] = {
    "EN",
    "en",
    "ES",
    "es",
}


def check_search_filters_languages_type_1_exclude_item(
    value: str,
) -> SearchFiltersLanguagesType1ExcludeItem:
    if value in SEARCH_FILTERS_LANGUAGES_TYPE_1_EXCLUDE_ITEM_VALUES:
        return cast(SearchFiltersLanguagesType1ExcludeItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SEARCH_FILTERS_LANGUAGES_TYPE_1_EXCLUDE_ITEM_VALUES!r}"
    )
