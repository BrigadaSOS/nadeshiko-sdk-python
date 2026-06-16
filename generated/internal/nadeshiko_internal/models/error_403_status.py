from typing import Literal

Error403Status = Literal[403]

ERROR_403_STATUS_VALUES: set[Error403Status] = {
    403,
}


def check_error_403_status(value: int) -> Error403Status:
    if value in ERROR_403_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ERROR_403_STATUS_VALUES!r}")
