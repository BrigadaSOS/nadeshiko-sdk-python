from typing import Literal, cast

IncludeExpansion = Literal["media"]

INCLUDE_EXPANSION_VALUES: set[IncludeExpansion] = {
    "media",
}


def check_include_expansion(value: str) -> IncludeExpansion:
    if value in INCLUDE_EXPANSION_VALUES:
        return cast(IncludeExpansion, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCLUDE_EXPANSION_VALUES!r}")
