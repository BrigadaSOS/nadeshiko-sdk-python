from typing import Literal, cast

Error400Status = Literal[400]

ERROR_400_STATUS_VALUES: set[Error400Status] = {
    400,
}


def check_error_400_status(value: int) -> Error400Status:
    if value in ERROR_400_STATUS_VALUES:
        return cast(Error400Status, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ERROR_400_STATUS_VALUES!r}")
