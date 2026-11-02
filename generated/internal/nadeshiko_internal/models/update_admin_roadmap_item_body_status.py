from typing import Literal

UpdateAdminRoadmapItemBodyStatus = Literal[
    "CONSIDERING", "DECLINED", "IN_PROGRESS", "PLANNED", "PROPOSED", "RELEASED"
]

UPDATE_ADMIN_ROADMAP_ITEM_BODY_STATUS_VALUES: set[UpdateAdminRoadmapItemBodyStatus] = {
    "CONSIDERING",
    "DECLINED",
    "IN_PROGRESS",
    "PLANNED",
    "PROPOSED",
    "RELEASED",
}


def check_update_admin_roadmap_item_body_status(value: str) -> UpdateAdminRoadmapItemBodyStatus:
    if value in UPDATE_ADMIN_ROADMAP_ITEM_BODY_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ADMIN_ROADMAP_ITEM_BODY_STATUS_VALUES!r}"
    )
