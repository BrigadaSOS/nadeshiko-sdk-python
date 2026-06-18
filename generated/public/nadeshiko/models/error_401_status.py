from typing import Literal

Error401Status = Literal[401]

ERROR_401_STATUS_VALUES: set[Error401Status] = {
    401,
}


def check_error_401_status(value: int) -> Error401Status:
    if value in ERROR_401_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ERROR_401_STATUS_VALUES!r}")
