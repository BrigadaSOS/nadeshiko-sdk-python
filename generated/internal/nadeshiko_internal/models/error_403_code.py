from typing import Literal

Error403Code = Literal["ACCESS_DENIED", "INSUFFICIENT_PERMISSIONS"]

ERROR_403_CODE_VALUES: set[Error403Code] = {
    "ACCESS_DENIED",
    "INSUFFICIENT_PERMISSIONS",
}


def check_error_403_code(value: str) -> Error403Code:
    if value in ERROR_403_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ERROR_403_CODE_VALUES!r}")
