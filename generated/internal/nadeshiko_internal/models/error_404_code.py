from typing import Literal

Error404Code = Literal["NOT_FOUND"]

ERROR_404_CODE_VALUES: set[Error404Code] = {
    "NOT_FOUND",
}


def check_error_404_code(value: str) -> Error404Code:
    if value in ERROR_404_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ERROR_404_CODE_VALUES!r}")
