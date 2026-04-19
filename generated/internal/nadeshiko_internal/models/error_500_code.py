from typing import Literal, cast

Error500Code = Literal["INTERNAL_SERVER_EXCEPTION"]

ERROR_500_CODE_VALUES: set[Error500Code] = {
    "INTERNAL_SERVER_EXCEPTION",
}


def check_error_500_code(value: str) -> Error500Code:
    if value in ERROR_500_CODE_VALUES:
        return cast(Error500Code, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ERROR_500_CODE_VALUES!r}")
