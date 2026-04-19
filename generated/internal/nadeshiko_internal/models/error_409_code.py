from typing import Literal, cast

Error409Code = Literal["ACCOUNT_CONFLICT", "DUPLICATE_KEY"]

ERROR_409_CODE_VALUES: set[Error409Code] = {
    "ACCOUNT_CONFLICT",
    "DUPLICATE_KEY",
}


def check_error_409_code(value: str) -> Error409Code:
    if value in ERROR_409_CODE_VALUES:
        return cast(Error409Code, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ERROR_409_CODE_VALUES!r}")
