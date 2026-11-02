from typing import Literal

Error503Code = Literal["SERVICE_OVERLOADED"]

ERROR_503_CODE_VALUES: set[Error503Code] = {
    "SERVICE_OVERLOADED",
}


def check_error_503_code(value: str) -> Error503Code:
    if value in ERROR_503_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ERROR_503_CODE_VALUES!r}")
