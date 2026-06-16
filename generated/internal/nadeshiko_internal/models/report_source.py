from typing import Literal

ReportSource = Literal["AUTO", "USER"]

REPORT_SOURCE_VALUES: set[ReportSource] = {
    "AUTO",
    "USER",
}


def check_report_source(value: str) -> ReportSource:
    if value in REPORT_SOURCE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_SOURCE_VALUES!r}")
