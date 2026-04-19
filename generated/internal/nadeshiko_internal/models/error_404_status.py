from typing import Literal, cast

Error404Status = Literal[404]

ERROR_404_STATUS_VALUES: set[Error404Status] = {
    404,
}


def check_error_404_status(value: int) -> Error404Status:
    if value in ERROR_404_STATUS_VALUES:
        return cast(Error404Status, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ERROR_404_STATUS_VALUES!r}")
