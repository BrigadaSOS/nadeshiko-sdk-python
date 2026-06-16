from typing import Literal

CollectionType = Literal["ANKI_EXPORT", "USER"]

COLLECTION_TYPE_VALUES: set[CollectionType] = {
    "ANKI_EXPORT",
    "USER",
}


def check_collection_type(value: str) -> CollectionType:
    if value in COLLECTION_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COLLECTION_TYPE_VALUES!r}")
