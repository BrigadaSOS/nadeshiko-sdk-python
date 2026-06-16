from typing import Literal

SearchPaginationEstimatedTotalHitsRelation = Literal["AT_LEAST", "EXACT"]

SEARCH_PAGINATION_ESTIMATED_TOTAL_HITS_RELATION_VALUES: set[
    SearchPaginationEstimatedTotalHitsRelation
] = {
    "AT_LEAST",
    "EXACT",
}


def check_search_pagination_estimated_total_hits_relation(
    value: str,
) -> SearchPaginationEstimatedTotalHitsRelation:
    if value in SEARCH_PAGINATION_ESTIMATED_TOTAL_HITS_RELATION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SEARCH_PAGINATION_ESTIMATED_TOTAL_HITS_RELATION_VALUES!r}"
    )
