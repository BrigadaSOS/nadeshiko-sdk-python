from typing import Literal

CreateReportRequestReason = Literal[
    "DUPLICATE_MEDIA",
    "DUPLICATE_SEGMENT",
    "IMAGE_ISSUE",
    "INAPPROPRIATE_CONTENT",
    "LOW_QUALITY_AUDIO",
    "MISSING_EPISODES",
    "NSFW_NOT_TAGGED",
    "OTHER",
    "WRONG_AUDIO",
    "WRONG_EPISODE_NUMBER",
    "WRONG_JAPANESE_TEXT",
    "WRONG_TIMING",
    "WRONG_TITLE",
    "WRONG_TRANSLATION",
]

CREATE_REPORT_REQUEST_REASON_VALUES: set[CreateReportRequestReason] = {
    "DUPLICATE_MEDIA",
    "DUPLICATE_SEGMENT",
    "IMAGE_ISSUE",
    "INAPPROPRIATE_CONTENT",
    "LOW_QUALITY_AUDIO",
    "MISSING_EPISODES",
    "NSFW_NOT_TAGGED",
    "OTHER",
    "WRONG_AUDIO",
    "WRONG_EPISODE_NUMBER",
    "WRONG_JAPANESE_TEXT",
    "WRONG_TIMING",
    "WRONG_TITLE",
    "WRONG_TRANSLATION",
}


def check_create_report_request_reason(value: str) -> CreateReportRequestReason:
    if value in CREATE_REPORT_REQUEST_REASON_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_REPORT_REQUEST_REASON_VALUES!r}"
    )
