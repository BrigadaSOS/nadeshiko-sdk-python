from typing import Literal

Error401Code = Literal[
    "AUTH_CREDENTIALS_EXPIRED", "AUTH_CREDENTIALS_INVALID", "AUTH_CREDENTIALS_REQUIRED"
]

ERROR_401_CODE_VALUES: set[Error401Code] = {
    "AUTH_CREDENTIALS_EXPIRED",
    "AUTH_CREDENTIALS_INVALID",
    "AUTH_CREDENTIALS_REQUIRED",
}


def check_error_401_code(value: str) -> Error401Code:
    if value in ERROR_401_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ERROR_401_CODE_VALUES!r}")
