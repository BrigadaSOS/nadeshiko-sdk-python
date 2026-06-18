from typing import Literal

Error409Status = Literal[409]

ERROR_409_STATUS_VALUES: set[Error409Status] = {
    409,
}


def check_error_409_status(value: int) -> Error409Status:
    if value in ERROR_409_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ERROR_409_STATUS_VALUES!r}")
