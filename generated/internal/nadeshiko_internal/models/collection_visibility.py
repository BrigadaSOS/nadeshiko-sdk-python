from typing import Literal

CollectionVisibility = Literal["PRIVATE", "PUBLIC"]

COLLECTION_VISIBILITY_VALUES: set[CollectionVisibility] = {
    "PRIVATE",
    "PUBLIC",
}


def check_collection_visibility(value: str) -> CollectionVisibility:
    if value in COLLECTION_VISIBILITY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COLLECTION_VISIBILITY_VALUES!r}")
