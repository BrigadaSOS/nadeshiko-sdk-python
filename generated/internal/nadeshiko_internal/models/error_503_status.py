from typing import Literal

Error503Status = Literal[503]

ERROR_503_STATUS_VALUES: set[Error503Status] = {
    503,
}


def check_error_503_status(value: int) -> Error503Status:
    if value in ERROR_503_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ERROR_503_STATUS_VALUES!r}")
