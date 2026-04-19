from typing import Literal, cast

ReportTargetEpisodeType = Literal["EPISODE"]

REPORT_TARGET_EPISODE_TYPE_VALUES: set[ReportTargetEpisodeType] = {
    "EPISODE",
}


def check_report_target_episode_type(value: str) -> ReportTargetEpisodeType:
    if value in REPORT_TARGET_EPISODE_TYPE_VALUES:
        return cast(ReportTargetEpisodeType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_TARGET_EPISODE_TYPE_VALUES!r}"
    )
