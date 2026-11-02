from typing import Literal

RoadmapItemWriteStatus = Literal["CONSIDERING", "IN_PROGRESS", "PLANNED", "RELEASED"]

ROADMAP_ITEM_WRITE_STATUS_VALUES: set[RoadmapItemWriteStatus] = {
    "CONSIDERING",
    "IN_PROGRESS",
    "PLANNED",
    "RELEASED",
}


def check_roadmap_item_write_status(value: str) -> RoadmapItemWriteStatus:
    if value in ROADMAP_ITEM_WRITE_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ROADMAP_ITEM_WRITE_STATUS_VALUES!r}"
    )
