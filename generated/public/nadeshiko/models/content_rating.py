from typing import Literal

ContentRating = Literal["EXPLICIT", "QUESTIONABLE", "SAFE", "SUGGESTIVE"]

CONTENT_RATING_VALUES: set[ContentRating] = {
    "EXPLICIT",
    "QUESTIONABLE",
    "SAFE",
    "SUGGESTIVE",
}


def check_content_rating(value: str) -> ContentRating:
    if value in CONTENT_RATING_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTENT_RATING_VALUES!r}")
