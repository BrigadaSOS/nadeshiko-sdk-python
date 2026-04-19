from typing import Literal, cast

Error429Code = Literal["QUOTA_EXCEEDED", "RATE_LIMIT_EXCEEDED"]

ERROR_429_CODE_VALUES: set[Error429Code] = {
    "QUOTA_EXCEEDED",
    "RATE_LIMIT_EXCEEDED",
}


def check_error_429_code(value: str) -> Error429Code:
    if value in ERROR_429_CODE_VALUES:
        return cast(Error429Code, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ERROR_429_CODE_VALUES!r}")
