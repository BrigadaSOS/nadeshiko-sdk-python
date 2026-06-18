from typing import Literal

Error400Code = Literal["INVALID_JSON", "INVALID_REQUEST", "VALIDATION_FAILED"]

ERROR_400_CODE_VALUES: set[Error400Code] = {
    "INVALID_JSON",
    "INVALID_REQUEST",
    "VALIDATION_FAILED",
}


def check_error_400_code(value: str) -> Error400Code:
    if value in ERROR_400_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ERROR_400_CODE_VALUES!r}")
