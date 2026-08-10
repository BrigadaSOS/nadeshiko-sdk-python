from typing import Literal

SegmentRevisionActor = Literal["AGENT", "HUMAN"]

SEGMENT_REVISION_ACTOR_VALUES: set[SegmentRevisionActor] = {
    "AGENT",
    "HUMAN",
}


def check_segment_revision_actor(value: str) -> SegmentRevisionActor:
    if value in SEGMENT_REVISION_ACTOR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SEGMENT_REVISION_ACTOR_VALUES!r}"
    )
