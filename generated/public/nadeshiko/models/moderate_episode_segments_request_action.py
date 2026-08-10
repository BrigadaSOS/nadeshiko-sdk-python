from typing import Literal

ModerateEpisodeSegmentsRequestAction = Literal["setStatus", "shiftTimings"]

MODERATE_EPISODE_SEGMENTS_REQUEST_ACTION_VALUES: set[ModerateEpisodeSegmentsRequestAction] = {
    "setStatus",
    "shiftTimings",
}


def check_moderate_episode_segments_request_action(
    value: str,
) -> ModerateEpisodeSegmentsRequestAction:
    if value in MODERATE_EPISODE_SEGMENTS_REQUEST_ACTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MODERATE_EPISODE_SEGMENTS_REQUEST_ACTION_VALUES!r}"
    )
