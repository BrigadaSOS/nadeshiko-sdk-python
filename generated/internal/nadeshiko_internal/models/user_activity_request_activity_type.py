from typing import Literal, cast

UserActivityRequestActivityType = Literal["ANKI_EXPORT", "SEARCH", "SEGMENT_PLAY", "SHARE"]

USER_ACTIVITY_REQUEST_ACTIVITY_TYPE_VALUES: set[UserActivityRequestActivityType] = {
    "ANKI_EXPORT",
    "SEARCH",
    "SEGMENT_PLAY",
    "SHARE",
}


def check_user_activity_request_activity_type(value: str) -> UserActivityRequestActivityType:
    if value in USER_ACTIVITY_REQUEST_ACTIVITY_TYPE_VALUES:
        return cast(UserActivityRequestActivityType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {USER_ACTIVITY_REQUEST_ACTIVITY_TYPE_VALUES!r}"
    )
