from typing import Literal

RoadmapItemWriteKind = Literal["CONTENT", "FEATURE"]

ROADMAP_ITEM_WRITE_KIND_VALUES: set[RoadmapItemWriteKind] = {
    "CONTENT",
    "FEATURE",
}


def check_roadmap_item_write_kind(value: str) -> RoadmapItemWriteKind:
    if value in ROADMAP_ITEM_WRITE_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ROADMAP_ITEM_WRITE_KIND_VALUES!r}"
    )
