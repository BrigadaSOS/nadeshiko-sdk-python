from typing import Literal, cast

ReportStatus = Literal["DISMISSED", "FIXED", "OPEN", "PROCESSING"]

REPORT_STATUS_VALUES: set[ReportStatus] = {
    "DISMISSED",
    "FIXED",
    "OPEN",
    "PROCESSING",
}


def check_report_status(value: str) -> ReportStatus:
    if value in REPORT_STATUS_VALUES:
        return cast(ReportStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_STATUS_VALUES!r}")
