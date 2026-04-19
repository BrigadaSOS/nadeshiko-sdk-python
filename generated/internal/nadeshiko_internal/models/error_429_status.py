from typing import Literal, cast

Error429Status = Literal[429]

ERROR_429_STATUS_VALUES: set[Error429Status] = {
    429,
}


def check_error_429_status(value: int) -> Error429Status:
    if value in ERROR_429_STATUS_VALUES:
        return cast(Error429Status, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ERROR_429_STATUS_VALUES!r}")
