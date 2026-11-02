from typing import Literal

RoadmapItemStatus = Literal[
    "CONSIDERING", "DECLINED", "IN_PROGRESS", "PLANNED", "PROPOSED", "RELEASED"
]

ROADMAP_ITEM_STATUS_VALUES: set[RoadmapItemStatus] = {
    "CONSIDERING",
    "DECLINED",
    "IN_PROGRESS",
    "PLANNED",
    "PROPOSED",
    "RELEASED",
}


def check_roadmap_item_status(value: str) -> RoadmapItemStatus:
    if value in ROADMAP_ITEM_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROADMAP_ITEM_STATUS_VALUES!r}")
