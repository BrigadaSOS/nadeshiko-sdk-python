from typing import Literal

RoadmapItemKind = Literal["CONTENT", "FEATURE"]

ROADMAP_ITEM_KIND_VALUES: set[RoadmapItemKind] = {
    "CONTENT",
    "FEATURE",
}


def check_roadmap_item_kind(value: str) -> RoadmapItemKind:
    if value in ROADMAP_ITEM_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROADMAP_ITEM_KIND_VALUES!r}")
