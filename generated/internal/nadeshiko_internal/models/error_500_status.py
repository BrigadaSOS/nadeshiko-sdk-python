from typing import Literal

Error500Status = Literal[500]

ERROR_500_STATUS_VALUES: set[Error500Status] = {
    500,
}


def check_error_500_status(value: int) -> Error500Status:
    if value in ERROR_500_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ERROR_500_STATUS_VALUES!r}")
